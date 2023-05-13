from django.contrib.auth.models import User
from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    bio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def username(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


class ProfileEducation(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='education')
    level = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    qualification_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_achieved = models.DateField()

    def __str__(self) -> str:
        return f"{self.institution_name} : {self.qualification_name} - {self.description}"

    class Meta:
        ordering = ('-date_achieved',)


class ProfileEmployment(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='employment')
    level = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_started = models.DateField()
    date_ended = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.company_name} : {self.job_title} - {self.description}"

    class Meta:
        ordering = ('-date_started',)


class ProfileCertification(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='certifications')
    certification_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_achieved = models.DateField()

    def __str__(self) -> str:
        return f"{self.certification_name}"

    class Meta:
        ordering = ('-date_achieved',)


class ProfileSkill(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.skill_name}"


class ProfileProject(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.project_name}"


class ProfileProjectImage(models.Model):

    profile = models.ForeignKey(
        ProfileProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
