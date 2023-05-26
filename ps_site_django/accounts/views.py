from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProfileEducationViewSet(viewsets.ModelViewSet):
    queryset = ProfileEducation.objects.all()
    serializer_class = ProfileEducationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, instance):
        if instance.profile != self.request.user.profile:
            raise PermissionDenied("You can not delete this object")
        super().perform_destroy(instance)


class ProfileEmploymentViewSet(viewsets.ModelViewSet):
    queryset = ProfileEmployment.objects.all()
    serializer_class = ProfileEmploymentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, instance):
        if instance.profile != self.request.user.profile:
            raise PermissionDenied("You can not delete this object")
        super().perform_destroy(instance)


class ProfileProjectViewSet(viewsets.ModelViewSet):
    queryset = ProfileProject.objects.all()
    serializer_class = ProfileProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, instance):
        if instance.profile != self.request.user.profile:
            raise PermissionDenied("You can not delete this object")
        super().perform_destroy(instance)


class ProfileProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProfileProjectImage.objects.all()
    serializer_class = ProfileProjectImageSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProfileCertificationViewSet(viewsets.ModelViewSet):
    queryset = ProfileCertification.objects.all()
    serializer_class = ProfileCertificationSerialier
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, instance):
        if instance.profile != self.request.user.profile:
            raise PermissionDenied("You can not delete this object")
        super().perform_destroy(instance)


class ProfileSkillViewSet(viewsets.ModelViewSet):
    queryset = ProfileSkill.objects.all()
    serializer_class = ProfileSkillSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, instance):
        if instance.profile != self.request.user.profile:
            raise PermissionDenied("You can not delete this object")
        super().perform_destroy(instance)
