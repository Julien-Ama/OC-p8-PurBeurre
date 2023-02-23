from django.core.management.base import BaseCommand
from django.db import IntegrityError

from progress.bar import ShadyBar

from search.models import Product, Category, Favorite
from search.api import Api


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """Feeds the database with data from API"""

        print("Cleaning database")
        self.clear_db()
        self.stdout.write(
            self.style.SUCCESS("DONE")
        )

        # Launches import of data from API
        print("Data importation from API")
        myapi = Api()
        # products = myapi.avoid_empty()
        print(products) # test products -------------------------------------------------

        if products is not None:
            print("bbbbbbbbbb") # test bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            self.stdout.write(
                self.style.SUCCESS("DONE")
            )
        else:
            self.stdout.write(
                self.style.ERROR("ERROR")
            )
            return
        print("aaaaaaaaaaaaaa") # test aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        with ShadyBar(
            "Inserting to database : ",
            max=len(products), suffix="%(percent)d%%"
        ) as bar:
            for product in products:
                print("1111111") # test 111111111111111111111111111111111111111111111
                name = product.get(
                    "product_name_fr"
                    )[:150].strip().lower().capitalize()
                brands = product.get("brands")[:150].upper()
                barcode = product.get("code")[:13].strip()
                url = product.get("url")
                image_url = product.get("image_url")
                image_small_url = product.get("image_small_url")
                nutriscore = product.get("nutriscore_grade")[0].upper()
                categories = [
                    name.strip().lower().capitalize()
                    for name in product["categories"].split(",")
                ]
                print("222222222") # test 222222222222222222222222222222222222222222222222
                # Get some of the nutriments keys/values
                nutriments_list = [
                    "energy_100g",
                    "sugars_100g",
                    "sodium_100g",
                    "fat_100g",
                    "salt_100g",
                ]
                print("33333333") # test 33333333333333333333333333333333333333333333333
                nutriments_dict = {}

                for nutriment in nutriments_list:
                    print("44444444444") # test 4444444444444444444444444444444444444444
                    nutriment_value = product.get("nutriments").get(nutriment)
                    if isinstance(nutriment_value, float) is True:
                        value = nutriment_value
                    else:
                        value = 0
                    nutriments_dict[nutriment] = value
                print("55555555555") # test 555555555555555555555555555555555555555555555
                product_obj = Product(
                    name=name,
                    brands=brands,
                    barcode=barcode,
                    url=url,
                    image_url=image_url,
                    image_small_url=image_small_url,
                    nutriscore=nutriscore,
                    energy_100g=nutriments_dict.get("energy_100g"),
                    sugars_100g=nutriments_dict.get("sugars_100g"),
                    sodium_100g=nutriments_dict.get("sodium_100g"),
                    fat_100g=nutriments_dict.get("fat_100g"),
                    salt_100g=nutriments_dict.get("salt_100g"),
                )

                try:
                    product_obj.save()
                    print("666666666666") # test 6666666666666666666666666666666666666666

                    # Save categories, linking them to Product obj
                    saved_categories = []
                    for category in categories:
                        cat_obj = Category(name=category)
                        if category not in saved_categories:
                            # Avoid duplicated categories
                            saved_categories.append(category)
                            try:
                                cat_obj.save()
                            except IntegrityError:  # Avoid duplicated cat
                                cat_obj = Category.objects.get(name=category)
                                print("777777777") # test 7777777777777777777777777777777

                            # add() Django method to link manytomany relation
                            product_obj.categories.add(cat_obj)
                            product_obj.save()
                            print("888888888888888") # test 88888888888888888888888888888
                except IntegrityError:
                    continue
                bar.next()
        self.stdout.write(
            self.style.SUCCESS("DONE")
        )
        print("99999999999999999") # test 99999999999999999999999999999999999999999999999
    def clear_db(self):
        """Clears the database"""

        product_obj = Product.objects.all()
        product_obj.delete()

        cat_obj = Category.objects.all()
        cat_obj.delete()

        favorite_obj = Favorite.objects.all()
        favorite_obj.delete()
