from django.db import models


from users.models import User

class Category(models.Model):
    """Represents the category table"""

    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents the product table"""

    name = models.CharField(max_length=150, unique=True)
    brands = models.CharField(max_length=150)
    barcode = models.CharField(max_length=13, unique=True)
    nutriscore = models.CharField(max_length=1)
    url = models.URLField()
    image_url = models.URLField()
    image_small_url = models.URLField()
    energy_100g = models.FloatField(default=0, null=True)  # can be empty
    sugars_100g = models.FloatField(default=0, null=True)
    sodium_100g = models.FloatField(default=0, null=True)
    fat_100g = models.FloatField(default=0, null=True)
    salt_100g = models.FloatField(default=0, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}, {self.nutriscore}"


class Favorite(models.Model):
    """Represents the favorite table
    product: linked to product by ForeignKey
    substitute: linked to product by ForeignKey
    user: linked to user by ForeignKey
    1 user can have different favorites
    """

    # CASCADE:if is deleted in Products'table,
    # will be deleted here NOT the opposite
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_product"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_substitute"
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_user"
    )

    def __str__(self):
        return (
            f"Produit: {self.product}, Substitut: {self.substitute}, User: {self.user}"
        )
