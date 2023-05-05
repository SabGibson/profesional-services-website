from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, ProfileEducation, ProfileEmployment,  ProfileProject, ProfileProjectImage, ProfileCertifications, ProfileSkill


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


class ProfileSkillSerializer(serializers.Serializer):
    class Meta:
        model = ProfileSkill
        fields = ('skill_name', 'description')


class ProfileCertificationsSerialier(serializers.Serializer):
    class Meta:
        model = ProfileCertifications
        fields = ('certification_name', 'description')


class ProfileEmploymentSerializer(serializers.Serializer):
    class Meta:
        model = ProfileEmployment
        fields = ('level', 'company_name', 'job_title', 'description',
                  'date_started', 'date_ended', 'is_present')


class ProfileEducationSerializer(serializers.Serializer):
    class Meta:
        model = ProfileEducation
        fields = ('level', 'institution_name', 'qualification_name', 'description',
                  'date_achieved')


class ProfileSerializer(serializers.ModelSerializer):
    projects = ProfileProjectSerializer(many=True)
    certifications = ProfileCertificationsSerialier(many=True)
    employment = ProfileEmploymentSerializer(many=True)
    education = ProfileEducationSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'image', 'education', 'employment',
                  'certifications', 'projects',)
