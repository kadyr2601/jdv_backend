from django.db import models
from others.models import MainBanner, SEOData
from projects.service import optimize_image


class InteriorDesignService(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    banner_title_gold = models.CharField(max_length=256, verbose_name='Main Banner title gold')
    banner_subtitle = models.CharField(max_length=256, verbose_name='Main Banner subtitle')
    experience_header = models.CharField(max_length=256, verbose_name='Experience Header')
    experience_title = models.CharField(max_length=256, verbose_name='Experience Title')
    experience_description = models.TextField(verbose_name='Experience Description')
    experience_image = models.ImageField(upload_to='services/interior_design/', verbose_name='Experience Image')
    experience_stats = models.JSONField(verbose_name='Stats', default=list,
                                        help_text='{"value": "data", "label": "data"},')
    experience_slogan = models.CharField(max_length=256, verbose_name='Experience Slogan')
    our_expertise_title = models.CharField(max_length=256, verbose_name='Our Expertise Title')
    our_expertise_description = models.TextField(verbose_name='Our Expertise Description')
    our_methodology_title = models.CharField(max_length=256, verbose_name='Our Methodology Title')
    our_methodology_description = models.TextField(verbose_name='Our Methodology Description')

    def save(self, *args, **kwargs):
        if self.experience_image:
            optimized_image = optimize_image(self.experience_image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.experience_image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Interior Design Page Configurations'

    class Meta:
        verbose_name = 'Interior Design Page'
        verbose_name_plural = 'Interior Design Page'


class Expertise(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    slogan = models.CharField(max_length=50, verbose_name='Slogan')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='services/expertise/', verbose_name='Image')
    page = models.ForeignKey(InteriorDesignService, on_delete=models.CASCADE, verbose_name='Page', related_name='expertises')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Expertise'
        verbose_name_plural = 'Expertises'


class Methodology(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='services/methodology/', verbose_name='Image')
    page = models.ForeignKey(InteriorDesignService, on_delete=models.CASCADE, verbose_name='Page',
                             related_name='methodologies')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Methodology'
        verbose_name_plural = 'Methodologies'


class FitOutService(MainBanner, SEOData):
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    banner_title_gold = models.CharField(max_length=256, verbose_name='Main Banner title gold')
    banner_subtitle = models.CharField(max_length=256, verbose_name='Main Banner subtitle')
    about_service_title = models.CharField(max_length=256, verbose_name='About Service Title')
    about_service_description = models.TextField(verbose_name='About Service Description')
    about_service_image = models.ImageField(upload_to='services/fit_out/', verbose_name='About Service Image')
    fit_out_expertise_description = models.TextField(verbose_name='Fit Out Expertise Description')
    transformation_process_description = models.TextField(verbose_name='Transformation Process Description')
    specialized_services_description = models.TextField(verbose_name='Specialized Services Description')
    more_information_section_title = models.TextField(verbose_name='Additional Information Title')
    more_information_section_description = models.TextField(verbose_name='Additional Information Description')

    def save(self, *args, **kwargs):
        if self.about_service_image:
            optimized_image = optimize_image(self.about_service_image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.about_service_image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Fit Out Page Configurations'

    class Meta:
        verbose_name = 'Fit Out Page'
        verbose_name_plural = 'Fit Out Page'   


class FitOutExpertise(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='services/fit_out_expertise/', verbose_name='Image')
    page = models.ForeignKey(FitOutService, on_delete=models.CASCADE, verbose_name='Page', related_name='fit_out_expertises')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Fit Out Expertise'
        verbose_name_plural = 'Fit Out Expertises'


class TransformationProcess(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='services/transformation_process/', verbose_name='Image')
    page = models.ForeignKey(FitOutService, on_delete=models.CASCADE, verbose_name='Page',
                             related_name='transformation_processes')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Transformation Process'
        verbose_name_plural = 'Transformation Processes'


class SpecializedService(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    page = models.ForeignKey(FitOutService, on_delete=models.CASCADE, verbose_name='Page',
                             related_name='specialized_services')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Specialized Service'
        verbose_name_plural = 'Specialized Services'


class MoreInformationSection(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='services/more_information/', verbose_name='Image')
    page = models.ForeignKey(FitOutService, on_delete=models.CASCADE, verbose_name='Page',
                             related_name='more_information_sections')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'More Information Section'
        verbose_name_plural = 'More Information Sections'


class ArchitectureService(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    banner_title_gold = models.CharField(max_length=256, verbose_name='Main Banner title gold')
    banner_subtitle = models.CharField(max_length=256, verbose_name='Main Banner subtitle')
    our_approach_title = models.CharField(max_length=256, verbose_name='Our Approach Title')
    our_approach_description = models.TextField(verbose_name='Our Approach Description')
    our_approach_image = models.ImageField(upload_to='services/architecture/', verbose_name='Our Approach Image')
    our_approach_stats = models.JSONField(verbose_name='Stats', default=list,
                                          help_text='{"value": "data", "label": "data"},')
    our_approach_slogan = models.CharField(max_length=256, verbose_name='Our Approach Slogan')
    featured_project_name = models.CharField(max_length=256, verbose_name='Featured Project Name')
    featured_project_description = models.TextField(verbose_name='Featured Project Description')
    featured_project_image_big = models.ImageField(upload_to='services/architecture/', verbose_name='Featured Project Image big')
    featured_project_image_small = models.ImageField(upload_to='services/architecture/', verbose_name='Featured Project Image small')
    featured_project_image_small_second = models.ImageField(upload_to='services/architecture/', verbose_name='Featured Project Image small second')
    featured_project_location = models.CharField(max_length=256, verbose_name='Featured Project Location')
    featured_project_area = models.CharField(max_length=256, verbose_name='Featured Project Area')
    featured_project_year = models.CharField(max_length=256, verbose_name='Featured Project Year')
    featured_project_type = models.CharField(max_length=256, verbose_name='Featured Project Type')

    def save(self, *args, **kwargs):
        if self.our_approach_image:
            optimized_image = optimize_image(self.our_approach_image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.our_approach_image = optimized_image
        if self.featured_project_image_big:
            optimized_image = optimize_image(self.featured_project_image_big, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.featured_project_image_big = optimized_image
        if self.featured_project_image_small:
            optimized_image = optimize_image(self.featured_project_image_small, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.featured_project_image_small = optimized_image
        if self.featured_project_image_small_second:
            optimized_image = optimize_image(self.featured_project_image_small_second, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.featured_project_image_small_second = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Architecture Page Configurations'

    class Meta:
        verbose_name = 'Architecture Page'
        verbose_name_plural = 'Architecture Page'


class AdditionalExpertise(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    page = models.ForeignKey(ArchitectureService, on_delete=models.CASCADE, verbose_name='Page', related_name='additional_expertises')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Additional Expertise'
        verbose_name_plural = 'Additional Expertises'


class WorkProcess(models.Model):
    step = models.CharField(max_length=256, verbose_name='Step')
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    page = models.ForeignKey(ArchitectureService, on_delete=models.CASCADE, verbose_name='Page', related_name='work_processes')

    def __str__(self):
        return self.step

    class Meta:
        verbose_name = 'Work Process'
        verbose_name_plural = 'Work Processes'


class ArchitecturalService(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='services/architectural_service/', verbose_name='Image')
    page = models.ForeignKey(ArchitectureService, on_delete=models.CASCADE, verbose_name='Page', related_name='architectural_services')

    def save(self, *args, **kwargs):
        if self.image:
            optimized_image = optimize_image(self.image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.image = optimized_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Architectural Service'
        verbose_name_plural = 'Architectural Services'