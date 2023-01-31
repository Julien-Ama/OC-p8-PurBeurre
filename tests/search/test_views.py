from django.test import TestCase, Client
from django.urls import reverse

# from search.forms import MainSearchForm
from search.models import Product
from users.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="password1234",
        )
        Product.objects.create(id=713, name="Nutella biscuits", nutriscore="E")
        self.home_url = reverse("search:home")
        self.products_list_url = reverse("search:products")
        self.product_details_url = reverse("search:product", args=[713])
        self.substitutes_list_url = reverse("search:substitutes", args=[713])
        self.favorites_list_url = reverse("search:favorites")
        self.legal_notice_url = reverse("search:legal_notice")

    def test_homepage(self):
        # check that reverse the home template
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/home.html")
        # check if home template contains this on HTML
        self.assertContains(response, "product_search")

    def test_products_page_POST(self):
        product_search = {"product_search": "input"}

        response = self.client.post(
            self.products_list_url, data=product_search
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/products.html")

    def test_product_details_page(self):
        response = self.client.get(self.product_details_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].name, "Nutella biscuits")
        self.assertTemplateUsed(response, "search/product.html")

    def test_substitutes_page(self):
        response = self.client.get(self.substitutes_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/substitutes.html")

    def test_save_substitute_as_favorite_success(self):
        self.client.force_login(self.user)
        product = Product.objects.create(
            name="Oasis framboise", nutriscore="E", barcode="1231231231231"
        )
        substitute = Product.objects.create(
            name="Maytea fraise", nutriscore="C", barcode="7897897897897"
        )
        url = reverse(
            "search:save_favorite",
            args=(
                product.id,
                substitute.id,
            ),
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_favorites_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.favorites_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/favorites.html")

    def test_legal_notice_page(self):
        response = self.client.get(self.legal_notice_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/legal_notice.html")
