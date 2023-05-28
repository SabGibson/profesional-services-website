from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register('profile-education', ProfileEducationViewSet)
router.register('profile-employment', ProfileEmploymentViewSet)
router.register('profile-project', ProfileProjectViewSet)
router.register('profile-project-image', ProfileProjectImageViewSet)
router.register('profile-certification', ProfileCertificationViewSet)
router.register('profile-skill', ProfileSkillViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
