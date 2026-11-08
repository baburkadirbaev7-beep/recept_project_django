from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe


def recipe_list(request):
    recipes = Recipe.objects.select_related("category").all()
    categories = Category.objects.all()

    category_slug = request.GET.get("category", "").strip()
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)

    context = {
        "recipes": recipes,
        "categories": categories,
        "active_category": category_slug,
    }
    return render(request, "recipe_app/recipe_list.html", context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_app/recipe_detail.html", {"recipe": recipe})
