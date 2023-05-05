from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


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


class ProfileEmployment(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='employment')
    level = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    jobe_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_started = models.DateField()
    date_ended = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.company_name} : {self.jobe_title} - {self.description}"


class ProfileCertificates(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='certifications')
    certification_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_achieved = models.DateField()

    def __str__(self) -> str:
        return f"{self.certification_name}"


class ProfileSkills(models.Model):
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

    product = models.ForeignKey(
        ProfileProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image for {self.product.name}"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
