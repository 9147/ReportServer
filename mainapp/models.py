from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

class LearningOutcome(models.Model):
    code=models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    choice = models.ManyToManyField('Choice', blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.code

class Choice(models.Model):
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.choice

class Section(models.Model):
    learning_outcome = models.ManyToManyField('LearningOutcome', blank=True, related_name='section_learning_outcome')
    access = models.ForeignKey('Teacher', blank=True, related_name='section_access', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FeedbackPage(models.Model):
    name = models.CharField(max_length=100)
    sections = models.ManyToManyField('FeedbackSection', blank=True, related_name='feedback_page_section')
    signature = models.ManyToManyField('Signature', blank=True, related_name='feedback_page_signature')

    def __str__(self):
        return str(self.id)

class FeedbackSection(models.Model):
    name=models.CharField(max_length=100)
    Fields=models.ManyToManyField('FeedbackField', blank=True, related_name='feedback_section_fields')

    def __str__(self):
        return self.name

class FeedbackField(models.Model):
    name=models.CharField(max_length=100)
    options=models.ManyToManyField('FeedbackFieldsChoice', blank=True, related_name='feedback_field_options')

    def __str__(self):
        return self.name
    
class FeedbackFieldsChoice(models.Model):
    choice=models.CharField(max_length=100)

    def __str__(self):
        return self.choice

class Signature(models.Model):
    name=models.CharField(max_length=100)
    required=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DevelopmentPage(models.Model):
    id = models.AutoField(primary_key=True)
    development_goal = models.CharField(max_length=100)
    key_components = models.CharField(max_length=100)
    sections = models.ManyToManyField('Section', blank=True, related_name='development_page_section')
    remarks = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class ReportField(models.Model):
    name = models.CharField(max_length=100)
    TEXT = 'text'
    IMAGE = 'image'
    DATE = 'date'
    TIME = 'time'
    INTEGER = 'integer'
    DATETIME = 'datetime'

    avaliable_types = {
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
        (DATE, 'Date'),
        (TIME, 'Time'),
        (INTEGER, 'Integer'),
        (DATETIME, 'Date and Time'),
    }
    type_of_field = models.CharField(max_length=100, choices=avaliable_types, default=TEXT)
    position_x = models.FloatField()  # X-coordinate position of the field on the page
    position_y = models.FloatField()  # Y-coordinate position of the field on the page
    # can be null
    width = models.FloatField(blank=True,null=True)  # Width of the field
    height = models.FloatField(blank=True,null=True)  # Height of the field
    multi_field = models.BooleanField(default=False)  # If the field can be repeated
    # Add other fields like field type, order, etc.

    def __str__(self):
        return self.name



class ReportPage(models.Model):
    report_fields = models.ManyToManyField('ReportField')
    no_of_fields = models.IntegerField()
    page_name = models.CharField(max_length=100)
    page_background = models.ImageField(upload_to='mainapp/static/backgrounds/')

    def __str__(self):
        return self.page_name

class Class(models.Model):
    name = models.CharField(max_length=100)
    cover_page = models.ForeignKey('ReportPage',related_name='class_cover_page', on_delete=models.CASCADE)
    cover_page_access = models.ForeignKey("Teacher",related_name='class_cover_page_access', on_delete=models.SET_NULL, null = True, blank=True)
    first_page = models.ForeignKey('ReportPage',related_name='class_first_page', on_delete=models.CASCADE)
    first_page_access = models.ForeignKey("Teacher",related_name='class_first_page_access', on_delete=models.SET_NULL, null = True, blank=True)
    Image_page = models.ForeignKey('ImagePage',related_name='class_image_page', on_delete=models.SET_NULL, null=True, blank=True)
    development_page = models.ManyToManyField('DevelopmentPage', blank=True, related_name='class_development_page')
    feedback_page = models.ForeignKey('FeedbackPage', blank=True, related_name='class_feedback_page', on_delete=models.SET_NULL, null=True)
    default_background = models.ImageField(upload_to='mainapp/static/backgrounds/', blank=True, null=True)
    # Add other fields as needed

    def __str__(self):
        return self.name

class ImagePage(models.Model):
    image = models.ImageField(upload_to='mainapp/static/backgrounds/')
    images=models.ManyToManyField('Image', blank=True, related_name='image_page_images')

    def __str__(self):
        return str(self.id)

class Image(models.Model):
    title = models.CharField(max_length=100)
    height = models.FloatField()
    width = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user

class Teacher(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    classes = models.ManyToManyField('Class', blank=True)
    superuser = models.BooleanField(default=False) # a superuser

    objects = UserManager()
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin








