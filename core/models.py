from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap icon class, e.g. bi-cloud"
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Project(models.Model):
    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ongoing"
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title


class NewsArticle(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=400, blank=True)
    content = models.TextField()

    featured_image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True
    )

    published_date = models.DateTimeField(
        blank=True,
        null=True
    )

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_date", "-created_at"]
        verbose_name = "News Article"
        verbose_name_plural = "News & Updates"

    def __str__(self):
        return self.title


class HomepageSlide(models.Model):
    MEDIA_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Uploaded Video"),
        ("youtube", "YouTube Video"),
    ]

    title = models.CharField(max_length=200)

    subtitle = models.CharField(
        max_length=250,
        blank=True
    )

    description = models.TextField(blank=True)

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPE_CHOICES,
        default="image"
    )

    image = models.ImageField(
        upload_to="slider/images/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="slider/videos/",
        blank=True,
        null=True,
        help_text="Upload MP4/WebM video files."
    )

    youtube_url = models.URLField(
        blank=True,
        help_text="Optional YouTube video URL."
    )

    poster_image = models.ImageField(
        upload_to="slider/posters/",
        blank=True,
        null=True,
        help_text="Optional preview image for video slides."
    )

    button_text = models.CharField(
        max_length=100,
        blank=True
    )

    button_url = models.CharField(
        max_length=250,
        blank=True
    )

    secondary_button_text = models.CharField(
        max_length=100,
        blank=True
    )

    secondary_button_url = models.CharField(
        max_length=250,
        blank=True
    )

    autoplay = models.BooleanField(default=True)
    muted = models.BooleanField(default=True)
    loop_video = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "title"]
        verbose_name = "Homepage Slide"
        verbose_name_plural = "Homepage Slides"

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=200)

    role = models.CharField(
        max_length=200
    )

    biography = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True
    )

    linkedin_url = models.URLField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Team Member"
        verbose_name_plural = "Team / Leadership"

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    company_name = models.CharField(
        max_length=200,
        default="MindTree Technology Solution"
    )

    facebook_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    whatsapp_number = models.CharField(
        max_length=50,
        blank=True
    )

    contact_email = models.EmailField(blank=True)

    secondary_email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    uk_address = models.CharField(
        max_length=300,
        blank=True
    )

    nigeria_address = models.CharField(
        max_length=300,
        blank=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.company_name
