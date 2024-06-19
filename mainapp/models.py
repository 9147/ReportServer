from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
import random, string
from django.db import OperationalError

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

class developmentPageAccess(models.Model):
    Auth_teachers_access=models.ManyToManyField('Teacher', related_name='development_page_access', blank=True)


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

def generate_unique_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        try:
            if not Class.objects.filter(group_id=code).exists():
                return code
        except OperationalError:
            # The Class table doesn't exist yet, so we can't check if the code is unique.
            # In this case, just return the code.
            return code
        
class UniqueGroupId(models.Model):
    group_id = models.CharField(max_length=16, primary_key=True,editable=False,unique=True, default=generate_unique_code)
    group_devices = models.ManyToManyField('Device', blank=True, related_name='group_id_online_devices')

    def __str__(self):
        return self.group_id
    
    def save(self, *args, **kwargs):
        if not self.group_id:
            self.group_id = generate_unique_code()
        super().save(*args, **kwargs)

class Device(models.Model):
    device_ip = models.GenericIPAddressField(protocol='IPv6',primary_key=True, editable=False)
    last_seen = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # set the last_seen field to the current time
        self.last_seen = timezone.now()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.device_ip
    

def generate_unique_group_id():
    return UniqueGroupId.objects.create(group_id=generate_unique_code())

class Commit(models.Model):
    admission_no = models.CharField(max_length=255)
    commit_no = models.IntegerField(default=0)
    section_nos = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Class(models.Model):
    name = models.CharField(max_length=100,unique=True)
    cover_page = models.ForeignKey('ReportPage',related_name='class_cover_page', on_delete=models.CASCADE)
    cover_page_access = models.ForeignKey("Teacher",related_name='class_cover_page_access', on_delete=models.SET_NULL, null = True, blank=True)
    first_page = models.ForeignKey('ReportPage',related_name='class_first_page', on_delete=models.CASCADE)
    first_page_access = models.ForeignKey("Teacher",related_name='class_first_page_access', on_delete=models.SET_NULL, null = True, blank=True)
    Image_page = models.ForeignKey('ImagePage',related_name='class_image_page', on_delete=models.SET_NULL, null=True, blank=True)
    Image_page_access = models.ForeignKey("Teacher",related_name='class_image_page_access', on_delete=models.SET_NULL, null = True, blank=True)
    development_page = models.ManyToManyField('DevelopmentPage', blank=True, related_name='class_development_page')
    development_page_access = models.ManyToManyField('developmentPageAccess',related_name='development_page_access',blank=True)
    feedback_page = models.ForeignKey('FeedbackPage',related_name='class_feedback_page', on_delete=models.SET_NULL, null=True,blank=True)
    default_background = models.ImageField(upload_to='mainapp/static/backgrounds/', blank=True, null=True)
    group_id = models.ForeignKey('UniqueGroupId',related_name='class_group_id', on_delete=generate_unique_group_id,default=generate_unique_group_id, editable=False)
    commit_number=models.IntegerField('commit_number',default=0)
    commits=models.ManyToManyField('Commit', blank=True, related_name='class_commits', through='ClassCommit')
    # Add other fields as needed
    MAX_COMMIT_LIMIT = 100000  # Define your maximum commit limit here

    def save(self, *args, **kwargs):
        if self.commit_number >= self.MAX_COMMIT_LIMIT:
            self.commit_number = 0
        if not self.group_id:
            self.group_id = UniqueGroupId.objects.create(group_id=generate_unique_code())
        super().save(*args, **kwargs)


    def add_commit(self, commit):
        # Calculate the number of excess commits
        excess_commits_count = self.commits.count() - 99
        
        if excess_commits_count > 0:
            # Get the excess commits
            excess_commits = self.commits.all().order_by('schemecommit__added_at')[:excess_commits_count]
            # delete the excess commits
            excess_commits.delete()
        
        # Add the new commit
        self.commits.add(commit)
        # Ensure the SchemeCommit entry is created to track the addition time
        # ClassCommit.objects.create(scheme=self, commit=commit)


    def __str__(self):
        return self.name
    
class ClassCommit(models.Model):
    scheme = models.ForeignKey(Class, on_delete=models.CASCADE)
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('scheme', 'commit')






