from django.db import models
from others.models import MainBanner, SEOData
from projects.service import optimize_image


class TeamMember(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    position = models.CharField(max_length=256, verbose_name='Position')
    image = models.ImageField(upload_to='aboutUs/team/', verbose_name='Team Member Image')
    bio = models.TextField(verbose_name='Bio')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'


class Essence(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='aboutUs/essence/', verbose_name='Image')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Essence'
        verbose_name_plural = 'Our Essences'


class AboutUsPage(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    welcome_section = models.TextField(verbose_name='Welcome Section')
    welcome_section_stats = models.JSONField(verbose_name='Stats', default=list, help_text='{"value": "data", "label": "data"},')
    founder_image = models.ImageField(upload_to='aboutUs/founder/', verbose_name='Founder Image')
    founder_words = models.TextField(verbose_name='Founder Words')
    our_team_section_description = models.TextField(verbose_name='Our Team Section Description')
    team_members = models.ManyToManyField(TeamMember, blank=True, verbose_name='Team Members')
    our_essence_section_title = models.CharField(max_length=128, verbose_name='Our Essence Section Title')
    our_essence_section_description = models.CharField(max_length=512, verbose_name='Our Essence Section Description')
    our_essence = models.ManyToManyField(Essence, blank=True, verbose_name='Our Essence')
    services_section_title = models.TextField(verbose_name='Services Section Title')
    services_section_description = models.TextField(verbose_name='Services Section Description')
    interior_design_service_description = models.TextField(verbose_name='Interior Design Service Description')
    interior_design_service_image = models.ImageField(upload_to='aboutUs/services/', verbose_name='Interior Design Service Image')
    fit_out_service_description = models.TextField(verbose_name='Fit Out Service Description')
    fit_out_service_image = models.ImageField(upload_to='aboutUs/services/', verbose_name='Fit Out Service Image')
    architecture_service_description = models.TextField(verbose_name='Architecture Service Description')
    architecture_service_image = models.ImageField(upload_to='aboutUs/services/', verbose_name='Architecture Service Image')

    def save(self, *args, **kwargs):
        if self.interior_design_service_image:
            optimized_image = optimize_image(self.interior_design_service_image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.interior_design_service_image = optimized_image
        if self.fit_out_service_image:
            optimized_image = optimize_image(self.fit_out_service_image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.fit_out_service_image = optimized_image
        if self.architecture_service_image:
            optimized_image = optimize_image(self.architecture_service_image, max_size=(1920, 1080), format='WEBP',
                                             quality=85)
            if optimized_image:
                self.architecture_service_image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return 'About Us Page Configurations'

    class Meta:
        verbose_name = 'About Us Page'
        verbose_name_plural = 'About Us Page'