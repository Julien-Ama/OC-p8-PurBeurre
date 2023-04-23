from django.test import TestCase

from search.models import Product, Category, Favorite
from users.models import User
from search.forms import MainSearchForm
from search.management.commands.feed_db import Command
from search.api import Api


class ModelsTestCase(TestCase):
    def test_product_str(self):
        product = Product.objects.create(
            name="Prince",
            brands="LU,PRINCE,MONDELEZ",
            barcode="7622210449283",
            nutriscore="D",
            url="https://fr.openfoodfacts.org/produit/"
                "7622210449283/prince-lu",
            image_url="https://static.openfoodfacts.org/images/products/"
                      "762/221/044/9283/front_fr.415.400.jpg",
            image_small_url="https://static.openfoodfacts.org/images/products/"
                            "762/221/044/9283/front_fr.415.200.jpg",
            energy_100g=0.0,
            sugars_100g=0.0,
            sodium_100g=0.232,
            fat_100g=0.0,
            salt_100g=0.58,
        )
        self.assertEqual(str(product), "Prince, D")

    def test_category_str(self):
        category = Category.objects.create(
            name="Snacks",
        )
        self.assertEqual(str(category), "Snacks")

    def test_favorite_str(self):
        product = Product.objects.create(
            name="Prince",
            barcode="7622210449283",
            nutriscore="D"
        )
        substitute = Product.objects.create(
            name="Biscuit sésame",
            barcode="3175680011480",
            nutriscore="C"
        )
        user = User.objects.create(
            username="username1",
            email="username1@gmail.com",
            password="password1"
        )
        favorite = Favorite.objects.create(
            product=product, substitute=substitute, user=user
        )
        self.assertEqual(
            str(favorite),
            f"Produit: {favorite.product}, "
            f"Substitut: {favorite.substitute}, "
            f"User: {favorite.user}",
        )

    # def test_autocomplete(self):
    #     # mainSearchForm = MainSearchForm.widget_attrs(
    #     #     input="pr"
    #     # )
    #     # self.assertEqual(str(mainSearchForm), "Prince chocolat biscuits")
    #     myapi = Api()
    #
    #     product = myapi.avoid_empty()
    #     # print(str(product))
    #     # name = product("product_name_fr")[:150].strip().lower().capitalize()
    #     for t in product:
    #         name = t.get("product_name_fr")[:150].strip().lower().capitalize()
    #     print(name)
    #     # print(product(name=name))
    #     # print()
    #     # mycommand = Command()
    #     # print(mycommand.handle(name))
    #     products = Product.objects.all()
    #     print(products)
