from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, ProfileEducation, ProfileEmployment,  ProfileProject, ProfileProjectImage, ProfileCertification, ProfileSkill


class ProfileProjectImageSerializer(serializers.Serializer):
    image_url = serializers.CharField(source='get_image', read_only=True)

    class Meta:
        model = ProfileProjectImage
        fields = ('id', 'image', 'image_url')


class ProfileProjectSerializer(serializers.ModelSerializer):
    images = ProfileProjectImageSerializer(many=True)

    class Meta:
        model = ProfileProject
        fields = ('id', 'project_name', 'description', 'images')


class ProfileSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSkill
        fields = ('id', 'skill_name', 'description')


class ProfileCertificationSerialier(serializers.ModelSerializer):
    class Meta:
        model = ProfileCertification
        fields = ('id', 'certification_name', 'description', 'date_achieved')


class ProfileEmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileEmployment
        fields = ('id', 'level', 'company_name', 'job_title', 'description',
                  'date_started', 'date_ended', 'is_present')


class ProfileEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileEducation
        fields = ('id', 'level', 'institution_name', 'qualification_name', 'description',
                  'date_achieved')


class ProfileSerializer(serializers.ModelSerializer):
    projects = ProfileProjectSerializer(many=True)
    certifications = ProfileCertificationSerialier(many=True)
    employment = ProfileEmploymentSerializer(many=True)
    education = ProfileEducationSerializer(many=True)
    skills = ProfileSkillSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'get_image', 'get_thumbnail', 'first_name', 'last_name', 'full_name', 'username', 'bio', 'education', 'employment',
                  'certifications', 'skills', 'projects',)
