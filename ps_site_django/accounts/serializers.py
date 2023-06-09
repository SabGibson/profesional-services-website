from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, ProfileEducation, ProfileEmployment,  ProfileProject, ProfileProjectImage, ProfileCertification, ProfileSkill


class ProfileProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(source='get_image', read_only=True)

    class Meta:
        model = ProfileProjectImage
        fields = ('id', 'project', 'image', 'image_url')


class ProfileProjectSerializer(serializers.ModelSerializer):
    images = ProfileProjectImageSerializer(many=True, read_only=True)

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
    date_ended = serializers.DateField(required=False, allow_null=True)

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
    image_url = serializers.CharField(source='get_image', read_only=True)
    thumbnail_url = serializers.CharField(
        source='get_thumbnail', read_only=True)
    projects = ProfileProjectSerializer(many=True, required=False)
    certifications = ProfileCertificationSerialier(many=True, required=False)
    employment = ProfileEmploymentSerializer(many=True, required=False)
    education = ProfileEducationSerializer(many=True, required=False)
    skills = ProfileSkillSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = ('id', 'image', 'thumbnail', 'image_url', 'thumbnail_url', 'first_name', 'last_name', 'full_name', 'username', 'bio', 'education', 'employment',
                  'certifications', 'skills', 'projects',)
