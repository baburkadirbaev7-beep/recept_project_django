from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Recipe


def recipe_list(request):
    recipes = Recipe.objects.select_related("category").all()
    categories = Category.objects.all()

    category_slug = request.GET.get("category", "").strip()
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)

    query = request.GET.get("q", "").strip()
    if query:
        search_filter = Q()
        for word in {query, query.lower(), query.capitalize()}:
            search_filter |= (
                Q(title__icontains=word)
                | Q(description__icontains=word)
                | Q(ingredients__icontains=word)
            )
        recipes = recipes.filter(search_filter)

    context = {
        "recipes": recipes,
        "categories": categories,
        "active_category": category_slug,
        "query": query,
    }
    return render(request, "recipe_app/recipe_list.html", context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_app/recipe_detail.html", {"recipe": recipe})
