from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'photo', 'created', 'modified')
    list_editable = ('title', 'photo')

    fieldsets = (
        (None, {
            "fields": ('user', 'profile')
        }),
        ('POST', {
            "fields": (
                ('title', 'photo'),
                ('created', 'modified')
            ),
        }),
    )

    readonly_fields = ('created', 'modified')
