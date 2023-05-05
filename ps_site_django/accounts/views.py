from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def update(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
        serializer = self.get_serializer(
            profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['pk'])

        # Check if the requesting user is the same as the user associated with the profile
        if request.user == profile.user:
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied(
                "You do not have permission to delete this profile.")
