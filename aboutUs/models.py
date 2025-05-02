from django.db import models
from services.models import Service


class MainBanner(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    image = models.ImageField(verbose_name='Image', upload_to='aboutUs/banners/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Main Banner'
        verbose_name_plural = 'Main Banner'

class WelcomeSection(models.Model):
    title = models.CharField(max_length=1056, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='aboutUs/banners/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Welcome Section'
        verbose_name_plural = 'Welcome Section'

class FounderSection(models.Model):
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Founder image', upload_to='aboutUs/banners/')

    def __str__(self):
        return 'Founder Section'

    class Meta:
        verbose_name = 'Founder Section'
        verbose_name_plural = 'Founder Section'

class ServicesSection(models.Model):
    title = models.CharField(max_length=1056, verbose_name='Title')
    description = models.CharField(max_length=3056, verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Best Services Section'
        verbose_name_plural = 'Best Services Section'

class ServicesBanner(models.Model):
    section = models.ForeignKey(ServicesSection, on_delete=models.CASCADE, related_name='services_banner', verbose_name='Section')
    title = models.CharField(max_length=1052, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    services = models.ForeignKey(Service, on_delete=models.CASCADE)

class OptionalSection(models.Model):
    title = models.CharField(max_length=1052, verbose_name='Title')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strategy Section'
        verbose_name_plural = 'StrategySection'

class OptionalBanner(models.Model):
    section = models.ForeignKey(OptionalSection, on_delete=models.CASCADE, related_name='banners', verbose_name='Section')
    title = models.CharField(max_length=512, verbose_name='Name')
    percentage = models.IntegerField(verbose_name='Percentage')

class FAQSection(models.Model):
    question = models.TextField(verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ Section'
        verbose_name_plural = 'FAQ Section'