# website/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

# Model for Team Members
class TeamMember(models.Model):
    # Member's name
    name = models.CharField(max_length=200, verbose_name=_("Nom complet"))
    # Member's title/role
    title = models.CharField(max_length=200, verbose_name=_("Titre/Rôle"))
    # A short biography or description of expertise
    bio = models.TextField(verbose_name=_("Biographie"), blank=True, null=True)
    # Profile picture
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True, verbose_name=_("Photo"))
    # LinkedIn profile URL
    linkedin_url = models.URLField(blank=True, null=True, verbose_name=_("Lien LinkedIn"))

    class Meta:
        verbose_name = _("Membre de l'équipe")
        verbose_name_plural = _("Membres de l'équipe")
        # Order by name
        ordering = ['name']

    def __str__(self):
        return self.name

# Model for Services
class Service(models.Model):
    # Service title
    title_fr = models.CharField(max_length=200, verbose_name=_("Titre (Français)"))
    title_en = models.CharField(max_length=200, verbose_name=_("Titre (Anglais)"))
    # Detailed description of the service
    description_fr = models.TextField(verbose_name=_("Description (Français)"))
    description_en = models.TextField(verbose_name=_("Description (Anglais)"))
    # Optional: an icon for the service (could be a path to an SVG or a class name for a font icon)
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Icône (ex: icon-class or SVG path)"))

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        # Order by title
        ordering = ['title_fr']

    def __str__(self):
        return self.title_fr

# Model for Projects (Current and Future)
class Project(models.Model):
    # Project title
    title_fr = models.CharField(max_length=200, verbose_name=_("Titre (Français)"))
    title_en = models.CharField(max_length=200, verbose_name=_("Titre (Anglais)"))
    # Short description of the project
    description_fr = models.TextField(verbose_name=_("Description (Français)"))
    description_en = models.TextField(verbose_name=_("Description (Anglais)"))
    # Date of the project/event
    date = models.DateField(blank=True, null=True, verbose_name=_("Date du projet/événement"))
    # Location of the project/event
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Lieu"))
    # URL for more details about the project
    project_url = models.URLField(blank=True, null=True, verbose_name=_("Lien du projet"))
    # Featured image for the project
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, verbose_name=_("Image du projet"))
    # Flag to indicate if it's a current project or a future perspective
    is_current = models.BooleanField(default=True, verbose_name=_("Projet actuel"))

    class Meta:
        verbose_name = _("Projet")
        verbose_name_plural = _("Projets")
        # Order by date descending
        ordering = ['-date']

    def __str__(self):
        return self.title_fr

# Model for Partners
class Partner(models.Model):
    # Partner's name
    name = models.CharField(max_length=200, verbose_name=_("Nom du partenaire"))
    # Partner's logo
    logo = models.ImageField(upload_to='partner_logos/', verbose_name=_("Logo du partenaire"))
    # Partner's website URL
    website_url = models.URLField(blank=True, null=True, verbose_name=_("Lien du site web"))
    # Description of the partnership
    description_fr = models.TextField(blank=True, null=True, verbose_name=_("Description (Français)"))
    description_en = models.TextField(blank=True, null=True, verbose_name=_("Description (Anglais)"))

    class Meta:
        verbose_name = _("Partenaire")
        verbose_name_plural = _("Partenaires")
        # Order by name
        ordering = ['name']

    def __str__(self):
        return self.name

# Model for Blog/News Posts
class BlogPost(models.Model):
    # Post title
    title_fr = models.CharField(max_length=255, verbose_name=_("Titre (Français)"))
    title_en = models.CharField(max_length=255, verbose_name=_("Titre (Anglais)"))
    # Content of the post
    content_fr = models.TextField(verbose_name=_("Contenu (Français)"))
    content_en = models.TextField(verbose_name=_("Contenu (Anglais)"))
    # Publication date
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de publication"))
    # Author of the post
    author = models.CharField(max_length=100, verbose_name=_("Auteur"))
    # Featured image for the post
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name=_("Image de l'article"))

    class Meta:
        verbose_name = _("Article de blog/Actualité")
        verbose_name_plural = _("Articles de blog/Actualités")
        # Order by publication date descending
        ordering = ['-publication_date']

    def __str__(self):
        return self.title_fr

# Model for Gallery Images/Videos
class GalleryItem(models.Model):
    # Title/caption for the item
    title_fr = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Titre (Français)"))
    title_en = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Titre (Anglais)"))
    # Type of media (Image or Video)
    MEDIA_CHOICES = [
        ('image', _('Image')),
        ('video', _('Vidéo')),
    ]
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default='image', verbose_name=_("Type de média"))
    # Image file
    image_file = models.ImageField(upload_to='gallery_images/', blank=True, null=True, verbose_name=_("Fichier image"))
    # Video URL (e.g., YouTube, Vimeo)
    video_url = models.URLField(blank=True, null=True, verbose_name=_("Lien vidéo (YouTube, Vimeo, etc.)"))
    # Date when the item was added
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date d'ajout"))

    class Meta:
        verbose_name = _("Élément de galerie")
        verbose_name_plural = _("Éléments de galerie")
        # Order by upload date descending
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title_fr if self.title_fr else f"Gallery Item {self.id}"

# Model for general organization information (About, Vision, Mission, Contact details)
class OrganizationInfo(models.Model):
    # About Us section
    about_us_fr = models.TextField(verbose_name=_("À propos de nous (Français)"))
    about_us_en = models.TextField(verbose_name=_("À propos de nous (Anglais)"))
    # Vision
    vision_fr = models.TextField(verbose_name=_("Notre vision (Français)"))
    vision_en = models.TextField(verbose_name=_("Notre vision (Anglais)"))
    # Mission
    mission_fr = models.TextField(verbose_name=_("Notre mission (Français)"))
    mission_en = models.TextField(verbose_name=_("Notre mission (Anglais)"))
    # Values (could be a JSONField if structured, but a simple text field for now)
    values_fr = models.TextField(verbose_name=_("Nos valeurs (Français)"))
    values_en = models.TextField(verbose_name=_("Nos valeurs (Anglais)"))

    # Contact Information
    address = models.CharField(max_length=255, verbose_name=_("Adresse"))
    phone_number = models.CharField(max_length=50, verbose_name=_("Numéro de téléphone"))
    whatsapp_number = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Numéro WhatsApp"))
    email = models.EmailField(verbose_name=_("Adresse e-mail"))
    linkedin_url = models.URLField(blank=True, null=True, verbose_name=_("Lien LinkedIn"))
    # Placeholder for Google Maps iframe/link
    google_maps_embed_url = models.URLField(blank=True, null=True, verbose_name=_("Lien d'intégration Google Maps"))

    class Meta:
        verbose_name = _("Informations sur l'organisation")
        verbose_name_plural = _("Informations sur l'organisation")

    def __str__(self):
        return "Informations Générales de Skills 4 Africa"

# Model for Contact Form Submissions
class ContactSubmission(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Nom"))
    email = models.EmailField(verbose_name=_("E-mail"))
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Sujet"))
    message = models.TextField(verbose_name=_("Message"))
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de soumission"))

    class Meta:
        verbose_name = _("Soumission de contact")
        verbose_name_plural = _("Soumissions de contact")
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Message de {self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"