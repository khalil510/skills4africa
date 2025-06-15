# website/admin.py

from django.contrib import admin
from .models import (
    TeamMember, Service, Project, Partner, BlogPost, GalleryItem,
    OrganizationInfo, ContactSubmission
)

admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Partner)
admin.site.register(BlogPost)
admin.site.register(GalleryItem)
admin.site.register(OrganizationInfo)
admin.site.register(ContactSubmission)