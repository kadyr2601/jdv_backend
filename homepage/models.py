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
    stats = models.JSONField(verbose_name='Stats', default=list, help_text='{"value": "data", "label": "data"},')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strategy Section'
        verbose_name_plural = 'Strategy Sections'


class HomePage(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    banner_subtitle = models.CharField(max_length=256, verbose_name='Main Banner subtitle')

    featured_project_wide = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='homepages_as_featured_wide',
        verbose_name='Featured Project Wide'
    )
    featured_project_tall = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='homepages_as_featured_tall',
        verbose_name='Featured Project Tall'
    )
    featured_project_normal = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='homepages_as_featured_normal',
        verbose_name='Featured Project Normal'
    )
    featured_project_normal_second = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='homepages_as_featured_normal_second',
        verbose_name='Featured Project Normal Second'
    )
    featured_project_normal_third = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='homepages_as_featured_normal_third',
        verbose_name='Featured Project Normal Third'
    )
    featured_project_wide_second = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='homepages_as_featured_wide_second',
        verbose_name='Featured Project Wide Second'
    )

    featured_projects_description = models.TextField(verbose_name='Featured Projects section description')

    testimonials = models.ManyToManyField(
        Testimonial,
        verbose_name='Testimonials',
        blank=True,
        related_name='homepages',
        help_text='Select no more than 4 testimonials and -> '
    )
    testimonials_description = models.TextField(verbose_name='Testimonials section description')

    strategy_section = models.ManyToManyField(
        StrategySection,
        verbose_name='Strategy section',
        blank=True,
        related_name='homepages',
        help_text='Select no more than 4 strategy section and -> '
    )
    strategy_section_description = models.TextField(verbose_name='Strategy section description')


    def __str__(self):
        return 'Homepage Configurations'

    class Meta:
        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepage'
