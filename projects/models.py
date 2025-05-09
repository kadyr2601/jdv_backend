from django.db import models
from django.utils.text import slugify


class MainBanner(models.Model):
    title = models.CharField(max_length=256, verbose_name='Banner title')
    image = models.ImageField(upload_to='banners', verbose_name='Banner image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Projects page Banner'
        verbose_name_plural = 'Projects page Banner'


class Project(models.Model):
    title = models.CharField(max_length=256, verbose_name='Project name')
    slug = models.SlugField(max_length=256, verbose_name='Project slug')
    card_image = models.ImageField(upload_to='projects', verbose_name='Project card image')
    banner_image = models.ImageField(upload_to='gallery', verbose_name='Banner image')
    meta_title = models.CharField(max_length=55, verbose_name="Meta Title")
    meta_description = models.CharField(max_length=158, verbose_name="Meta Description")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    gallery = models.ImageField(upload_to='gallery', verbose_name='Gallery image')