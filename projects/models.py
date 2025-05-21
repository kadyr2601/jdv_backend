from django.db import models
from django.utils.text import slugify
from others.models import MainBanner, SEOData


class ProjectsPage(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')

    def __str__(self):
        return 'Projects Page Configurations'

    class Meta:
        verbose_name = 'Projects Page'
        verbose_name_plural = 'Projects Page'

class Project(models.Model):
    name = models.CharField(max_length=512, verbose_name='Project name')
    slug = models.SlugField(max_length=512, verbose_name='Project slug')
    cardImage = models.ImageField(upload_to='projects', verbose_name='Project card image')
    year = models.CharField(max_length=10, verbose_name='Project year')
    location = models.CharField(max_length=256, verbose_name='Project location')
    category = models.CharField(max_length=256, verbose_name='Project category', help_text='Residential or Commercial or etc')
    banner_image = models.ImageField(upload_to='gallery', verbose_name='Banner image')
    description = models.TextField(verbose_name='Project description')
    meta_title = models.CharField(max_length=55, verbose_name="Meta Title for SEO")
    meta_description = models.CharField(max_length=158, verbose_name="Meta Description for SEO")
    area = models.CharField(max_length=100, verbose_name='Project area')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    gallery = models.ImageField(upload_to='gallery', verbose_name='Gallery image')