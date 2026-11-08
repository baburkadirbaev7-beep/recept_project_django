from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Слаг (URL)")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название блюда")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Категория",
    )
    description = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Ингредиенты")
    steps = models.TextField(verbose_name="Шаги приготовления")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
