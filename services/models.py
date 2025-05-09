from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(max_length=256, verbose_name='Main Banner title')
    image = models.ImageField(upload_to='banners', verbose_name='Main Banner image')
    name = models.CharField(max_length=256, verbose_name='Service Name')
    page_title = models.CharField(max_length=512, verbose_name='Page Title')
    main_image = models.ImageField(upload_to='services/', verbose_name='Service Image')
    description = models.TextField(verbose_name='Description')
    slug = models.SlugField(max_length=256, verbose_name='Service slug')
    meta_title = models.CharField(max_length=55, verbose_name="Meta Title")
    meta_description = models.CharField(max_length=158, verbose_name="Meta Description")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Maintenance(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=512, verbose_name='Maintenance Title')
    image = models.ImageField(upload_to='maintenance/', verbose_name='Maintenance Image')
    text = models.TextField(
        help_text="Enter each bullet point on a new line"
    )

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenances'