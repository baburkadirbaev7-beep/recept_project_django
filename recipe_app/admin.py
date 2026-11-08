from django.contrib import admin
from .models import Category, Recipe

admin.site.site_header = "Панель управления рецептами"
admin.site.site_title = "Кулинарная книга"
admin.site.index_title = "Управление рецептами и категориями"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at")
    list_filter = ("category",)
    date_hierarchy = "published_at"
