from django.db import models


class SEOData(models.Model):
    Pages = (
        ('home', 'Home'),
        ('about', 'About Us'),
        ('projects', 'Projects'),
        ('contacts', 'Contact Us'),
    )
    page = models.CharField(
        max_length=100,
        choices=Pages,
        default='home',
        unique=True,
        verbose_name="Select page"
    )

    meta_title = models.CharField(max_length=70, verbose_name="Meta Title")
    meta_description = models.CharField(max_length=1052, verbose_name="Meta Description")
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name="Meta Keywords (через запятую)")

    og_title = models.CharField(max_length=95, blank=True, verbose_name="OG Title")
    og_description = models.CharField(max_length=300, blank=True, verbose_name="OG Description")
    og_image = models.ImageField(upload_to='seo/og_images/', blank=True, null=True, verbose_name="OG Image")
    og_url = models.URLField(blank=True, verbose_name="OG URL")

    def save(self, *args, **kwargs):
        if not self.og_title:
            self.og_title = self.meta_title
        if not self.og_description:
            self.og_description = self.meta_description
        if not self.og_url:
            base_url = "https://jdv.ae"
            self.og_url = base_url if self.page == "home" else f"{base_url}/{self.page}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_page_display()


    class Meta:
        verbose_name = "SEO данные"
        verbose_name_plural = "SEO данные"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

