# website/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeamMemberViewSet, ServiceViewSet, ProjectViewSet, PartnerViewSet,
    BlogPostViewSet, GalleryItemViewSet, OrganizationInfoViewSet,
    ContactSubmissionViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'team', TeamMemberViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'gallery', GalleryItemViewSet)
router.register(r'organization-info', OrganizationInfoViewSet)
router.register(r'contact-submissions', ContactSubmissionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]