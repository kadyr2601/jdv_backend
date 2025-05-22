from django.db import models
from projects.models import Project
from others.models import MainBanner, SEOData


class Testimonial(models.Model):
    category = models.CharField(max_length=512, verbose_name='Category', help_text='Hotel Lobby or etc')
    review = models.TextField(verbose_name='Review')
    fullname = models.CharField(max_length=512, verbose_name='Fullname')
    icon = models.ImageField(upload_to='home/testimonials/', verbose_name='Icon')
    stars = models.IntegerField(verbose_name='Stars')
    position = models.CharField(max_length=512, verbose_name='Position')
    background_image = models.ImageField(upload_to='home/testimonials/', verbose_name='Background Image of card')

    def __str__(self):
        return 'Testimonial - {}'.format(self.fullname)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class StrategySection(models.Model):
    title = models.CharField(max_length=512, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='home/strategy/', verbose_name='Upload image')
    cta_first_title = models.CharField(max_length=20, verbose_name='CTA 1 Title')
    cta_first_description = models.CharField(max_length=100, verbose_name='CTA 1 Description')
    cta_second_title = models.CharField(max_length=20, verbose_name='CTA 2 Title')
    cta_second_description = models.CharField(max_length=100, verbose_name='CTA 2 Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strategy Section'
        verbose_name_plural = 'Strategy Sections'


class HomePage(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    banner_subtitle = models.CharField(max_length=256, verbose_name='Main Banner subtitle')
    featured_projects = models.ManyToManyField(Project,
                                               verbose_name='Featured Projects',
                                               blank=True, help_text='Select no more than 6 projects and -> ')
    testimonials = models.ManyToManyField(Testimonial,
                                          verbose_name='Testimonials',
                                          blank=True, help_text='Select no more than 4 testimonials and -> ')
    strategy_section = models.ManyToManyField(StrategySection,
                                              verbose_name='Strategy section',
                                              blank=True, help_text='Select no more than 4 strategy section and -> ')

    def __str__(self):
        return 'Homepage Configurations'

    class Meta:
        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepage'
