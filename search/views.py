from django.db.models import Count
from django.shortcuts import render, redirect
# from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .forms import MainSearchForm
from .models import Product, Category, Favorite
from users.models import User


def home(request):
    """Displays the home page"""
    main_search_form = MainSearchForm()  # instanciate form
    context = {
        "main_search_form": main_search_form,
        # key: variables we access from template
    }
    return render(request, "search/home.html", context)


def legal_notice(request):
    """Displays the legal notice page with infos"""
    return render(request, "search/legal_notice.html")


def products(request):
    if request.method == "POST":
        product_search = request.POST['product_search']

        all_product = Product.objects.all().filter(
            name__contains=product_search.strip().lower().capitalize())[:6]
        context = {
            "title": product_search,
            "products": all_product
        }
        return render(request, "search/products.html", context)


def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {"product": product}
    return render(request, "search/product.html", context)


def substitutes(request, product_id):
    """Displays the result page with list of substitutes for the selected product

    Args:
        product_id (int): Id of the product"""
    product_query = Product.objects.get(pk=product_id)

    product_query_cat = Category.objects.filter(product__id=product_query.id)

    substitutes = (
        Product.objects.filter(categories__in=product_query_cat)
            .annotate(nb_cat=Count("categories"))
            .filter(nb_cat__gte=3)
            .filter(nutriscore__lt=product_query.nutriscore)
            .order_by("nutriscore")[:9]
    )

    context = {"product": product_query, "substitutes": substitutes}

    return render(request, "search/substitutes.html", context)


@login_required
def save_favorite(request, product_id, substitute_id):
    """Saves the substitute and product searched as favorite
    if user is logged in"""

    product = Product.objects.get(pk=product_id)
    substitute = Product.objects.get(pk=substitute_id)
    user = User.objects.get(pk=request.user.id)
    favorite = Favorite(product=product, substitute=substitute, user=user)

    try:
        favorite.save()
        return redirect("search:favorites")
    except IntegrityError:
        return redirect("search:home")


@login_required
def favorites(request):
    """Displays the favorites for the logged in user"""

    # Find favorites in DB according to user id
    favorites = Favorite.objects.filter(user_id=request.user.id)

    context = {
        "favorites": favorites,
    }

    return render(request, "search/favorites.html", context)
