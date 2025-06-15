# website/views.py

from rest_framework import viewsets
from .models import (
    TeamMember, Service, Project, Partner, BlogPost, GalleryItem,
    OrganizationInfo, ContactSubmission
)
from .serializers import (
    TeamMemberSerializer, ServiceSerializer, ProjectSerializer, PartnerSerializer,
    BlogPostSerializer, GalleryItemSerializer, OrganizationInfoSerializer,
    ContactSubmissionSerializer
)

class TeamMemberViewSet(viewsets.ModelViewSet):
    # Query all team members
    queryset = TeamMember.objects.all()
    # Use the TeamMemberSerializer for serialization
    serializer_class = TeamMemberSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class GalleryItemViewSet(viewsets.ModelViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer

class OrganizationInfoViewSet(viewsets.ModelViewSet):
    # For OrganizationInfo, we expect only one instance.
    # We'll override list and retrieve to ensure this.
    queryset = OrganizationInfo.objects.all()
    serializer_class = OrganizationInfoSerializer

    def get_object(self):
        # Always return the first (and likely only) instance
        return self.get_queryset().first()

    def list(self, request, *args, **kwargs):
        # If there's no OrganizationInfo, create a default one
        if not self.get_queryset().exists():
            OrganizationInfo.objects.create(
                about_us_fr="About us (French) - Default",
                about_us_en="About us (English) - Default",
                vision_fr="Vision (French) - Default",
                vision_en="Vision (English) - Default",
                mission_fr="Mission (French) - Default",
                mission_en="Mission (English) - Default",
                values_fr="Values (French) - Default",
                values_en="Values (English) - Default",
                address="Default Address",
                phone_number="+1234567890",
                email="info@example.com"
            )
        # Return only the first instance in a list (or an empty list if none)
        # This will simplify frontend logic for fetching singletons
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

from rest_framework.response import Response
class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer