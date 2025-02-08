from django.contrib import admin


from .models import Category, Post, Location


class PostAdmin(admin.ModelAdmin):
    """PostAdmin."""

    list_display = (
        'title',
        'text',
        'author',
        'pub_date',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'text',
        'category'
    )
    search_fields = ('title', 'text')
    list_filter = ('category', 'author')
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
