from django.contrib import admin
from .models import *
# Register your models here.


class EducationInline(admin.TabularInline):
    model = ProfileEducation
    extra = 1


class EmploymentInline(admin.TabularInline):
    model = ProfileEmployment
    extra = 1


class CertificationInline(admin.TabularInline):
    model = ProfileCertification
    extra = 1


class ProjectImageInline(admin.TabularInline):
    model = ProfileProjectImage


class ProjectsAdmin(admin.ModelAdmin):
    model = ProfileProject
    inlines = [ProjectImageInline]
    extra = 1


class SkillsInline(admin.TabularInline):
    model = ProfileSkill
    extra = 1


class EducationInline(admin.TabularInline):
    model = ProfileEducation
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, SkillsInline,
               CertificationInline, EmploymentInline]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileProject, ProjectsAdmin)
