from django.core.exceptions import ValidationError
from projects.models import Project
from services.models import Service
from django.db import models
from django.core.validators import FileExtensionValidator

BANNER_SLIDE_TYPE_CHOICES = (
    ('image', 'Image'),
    ('video', 'Video'),
)

BANNER_SLIDE_ALIGNMENT_CHOICES = (
    ('left', 'Left'),
    ('center', 'Center'),
    ('right', 'Right'),
    ('split', 'Split'),
)

class BannerCTA(models.Model):
    text = models.CharField(max_length=100, help_text="Text for the CTA button (e.g., 'Read More')")
    url = models.CharField(max_length=200, help_text="URL the CTA button links to (e.g., '/about')")

    def __str__(self):
        return f"CTA: {self.text}"

    class Meta:
        verbose_name = "Main Banner CTA"
        verbose_name_plural = "Main Banner CTAs"

class BannerSlide(models.Model):
    type = models.CharField(
        max_length=10,
        choices=BANNER_SLIDE_TYPE_CHOICES,
        help_text="Type of slide content: image or video"
    )
    src = models.FileField(
        upload_to='banner_media/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4'])],
        help_text="Upload image (jpg, jpeg, png) or video (mp4) file"
    )
    title = models.CharField(max_length=200, help_text="Main title of the slide")
    subtitle = models.CharField(max_length=200, blank=True, null=True, help_text="Optional subtitle")
    description = models.TextField(blank=True, null=True, help_text="Optional description text")
    category = models.CharField(max_length=100, blank=True, null=True, help_text="Optional category (e.g., 'A TRENDY LUXURY')")
    cta = models.ForeignKey(
        BannerCTA,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Optional Call-to-Action for the slide"
    )
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Optional phone number (e.g., '+971 55 407 3275')")
    alignment = models.CharField(
        max_length=10,
        choices=BANNER_SLIDE_ALIGNMENT_CHOICES,
        default='left',
        help_text="Content alignment: left, center, right, or split"
    )
    social_links = models.BooleanField(default=False, help_text="Show social media links on the slide")
    order = models.PositiveIntegerField(default=0, help_text="Order of the slide in the banner")

    def __str__(self):
        return f"Slide: {self.title} ({self.id})"

    class Meta:
        verbose_name = "Main Banner Slide"
        verbose_name_plural = "Main Banner Slides"
        ordering = ['order']

class LuxuryBanner(models.Model):
    slides = models.ManyToManyField(BannerSlide, help_text="Slides included in this banner")
    autoplay = models.BooleanField(default=True, help_text="Enable autoplay for the banner")
    autoplay_speed = models.PositiveIntegerField(default=5000, help_text="Autoplay speed in milliseconds (e.g., 5000)")
    show_arrows = models.BooleanField(default=True, help_text="Show navigation arrows")
    show_dots = models.BooleanField(default=False, help_text="Show navigation dots")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Main banner'

    def save(self, *args, **kwargs):
        if LuxuryBanner.objects.exists() and not self.pk:
            raise ValidationError("Only one Main Banner object can be created.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Main Banner"
        verbose_name_plural = "Main Banners"

class AboutSection(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='home/sections/', verbose_name='Upload image')

    def __str__(self):
        return 'About Section'

    def save(self, *args, **kwargs):
        if AboutSection.objects.exists() and not self.pk:
            raise ValidationError("Only one About Section object can be created.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'

class AboutSectionBanner(models.Model):
    section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='about_banner_set')
    name = models.CharField(max_length=512, verbose_name='Banner name')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='home/sections/', verbose_name='Upload image')

class FeaturedServicesSection(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    image = models.ImageField(upload_to='home/services/', verbose_name='Upload image')

    def save(self, *args, **kwargs):
        if FeaturedServicesSection.objects.exists() and not self.pk:
            raise ValidationError("Only one Featured Services Section object can be created.")
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Featured Services'

    class Meta:
        verbose_name = 'Featured Services'
        verbose_name_plural = 'Featured Services'

class FeaturedServicesBanner(models.Model):
    section = models.ForeignKey(FeaturedServicesSection, on_delete=models.CASCADE, related_name='services_banner_set')
    name = models.CharField(max_length=512, verbose_name='Service name')
    description = models.TextField(verbose_name='Service description')
    image = models.ImageField(upload_to='home/services/', verbose_name='Upload image')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')

class ReviewsSection(models.Model):
    stars = models.IntegerField(verbose_name='Stars')
    review = models.TextField(verbose_name='Review')
    image = models.ImageField(upload_to='home/reviews/', verbose_name='Client image')
    client_fullname = models.CharField(max_length=512, verbose_name='Client fullname')
    client_position = models.CharField(max_length=512, verbose_name='Client position')

    def __str__(self):
        return 'Review - {}'.format(self.client_fullname)

    class Meta:
        verbose_name = 'Reviews'
        verbose_name_plural = 'Reviews'

class BeforeAfterSection(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    before_image = models.ImageField(upload_to='home/before-after/', verbose_name='Before image')
    after_image = models.ImageField(upload_to='home/after-before/', verbose_name='After image')

    def save(self, *args, **kwargs):
        if BeforeAfterSection.objects.exists() and not self.pk:
            raise ValidationError("Only one Before & After Section object can be created.")
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Before & After Banner Section'

    class Meta:
        verbose_name = 'Before After Section'
        verbose_name_plural = 'Before After Sections'

class FeaturedProjectsSection(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    image = models.ImageField(upload_to='home/featured-projects/', verbose_name='Upload image')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_set')

    def __str__(self):
        return 'Featured Project - {}'.format(self.project)

    class Meta:
        verbose_name = 'Featured Projects'
        verbose_name_plural = 'Featured Projects'

class AboutInteriorSection(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='home/about-interior/', verbose_name='Upload image')

    def save(self, *args, **kwargs):
        if AboutInteriorSection.objects.exists() and not self.pk:
            raise ValidationError("Only one About Interior Section object can be created.")
        super().save(*args, **kwargs)

    def __str__(self):
        return 'About Interior Section'

    class Meta:
        verbose_name = 'About Interior'
        verbose_name_plural = 'About Interiors'

class AboutInteriorBanner(models.Model):
    section = models.ForeignKey(AboutInteriorSection, on_delete=models.CASCADE, related_name='about_interior_banner_set')
    title = models.CharField(max_length=512, verbose_name='Title')
    description = models.TextField(verbose_name='Description')