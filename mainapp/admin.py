from .models import Class, ReportPage, ReportField, LearningOutcome, Choice, Section, DevelopmentPage, FeedbackField, FeedbackFieldsChoice, FeedbackPage, FeedbackSection, Signature, Image , ImagePage
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['username','superuser']
    list_filter = ['username','superuser']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('classes','name')}),
        ('Permissions', {'fields': ('superuser','staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password_2')}
        ),
    )
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name','cover_page','cover_page_access','first_page','first_page_access']


@admin.register(ReportPage)
class ReportPageAdmin(admin.ModelAdmin):
    list_display= ['page_name','page_background','no_of_fields']

    def __str__(self):
        return self.page_name

@admin.register(ReportField)
class ReportFieldAdmin(admin.ModelAdmin):
    list_display = ['name','type_of_field','position_x','position_y','width','height','multi_field']

    def __str__(self):
        return self.name


@admin.register(LearningOutcome)
class LearningOutcomeAdmin(admin.ModelAdmin):
    list_display = ['code','name']

    def __str__(self):
        return self.code

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice']

    def __str__(self):
        return self.choice

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name

@admin.register(DevelopmentPage)
class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ['id','development_goal','key_components',"remarks"]

    def __str__(self):
        return self.development_goal
    
@admin.register(FeedbackField)
class FeedbackFieldAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name
    
@admin.register(FeedbackFieldsChoice)
class FeedbackFieldsChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice']

    def __str__(self):
        return self.choice

@admin.register(FeedbackPage)
class FeedbackPageAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name    
    
@admin.register(FeedbackSection)
class FeedbackSectionAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','x','y','width','height']

    def __str__(self):
        return self.title
    
@admin.register(ImagePage)
class ImagePageAdmin(admin.ModelAdmin):
    list_display = ['image','id']

    def __str__(self):
        return self.name




