from django.contrib import admin
from .models import (
    Service,
    Project,
    NewsArticle,
    HomepageSlide,
    TeamMember,
    SiteSettings,
)


admin.site.site_header = "MindTree Website Administration"
admin.site.site_title = "MindTree Admin"
admin.site.index_title = "Website Management Console"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    list_filter = (
        "is_active",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "status",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published_date",
        "is_published",
        "updated_at",
    )

    list_editable = (
        "is_published",
    )

    list_filter = (
        "is_published",
        "published_date",
    )

    search_fields = (
        "title",
        "summary",
        "content",
    )


@admin.register(HomepageSlide)
class HomepageSlideAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "media_type",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "media_type",
        "is_active",
    )

    search_fields = (
        "title",
        "subtitle",
        "description",
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "role",
        "biography",
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "contact_email",
        "phone",
        "updated_at",
    )

    fieldsets = (
        (
            "Company Information",
            {
                "fields": (
                    "company_name",
                    "contact_email",
                    "secondary_email",
                    "phone",
                    "whatsapp_number",
                    "uk_address",
                    "nigeria_address",
                )
            },
        ),
        (
            "Social Media",
            {
                "fields": (
                    "facebook_url",
                    "youtube_url",
                    "linkedin_url",
                    "instagram_url",
                )
            },
        ),
    )
