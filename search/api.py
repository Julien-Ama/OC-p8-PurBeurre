import time

import requests


class Api:
    """Represents the API used to get data from"""

    def __init__(self):
        self.products = []

        self.HEADERS = {
            "User-Agent": "P8_Pur_beurre - GNU/Linux - Version 0.1"
        }
        self.PAYLOAD = {
            "search_simple": 1,
            "action": "process",
            "tagtype_0": "countries",
            "tag_contains_0": "contains",
            "tag_0": "france",
            "sort_by": "unique_scans_n",
            "page_size": 750,
            "json": 1,
            # field make the request faster
            "fields": "product_name_fr,code,brands,nutriscore_grade,url,"
            "image_url,image_small_url,nutriments,categories",
        }
        self.get_products()

    def get_products(self):
        """Gets most popular products from OFF API"""

        # Manage time between requests
        r = ""
        while r == "":
            # Pause before new request
            time.sleep(1)
            try:
                r = requests.get(
                    "https://fr.openfoodfacts.org/cgi/search.pl?",
                    params=self.PAYLOAD,
                    headers=self.HEADERS,
                )
                break
            except ValueError:
                time.sleep(5)  # pause 5secounds
                continue

        if r.status_code == 200:
            # Cast products found to json as a list and assign into variable
            self.products = r.json()["products"]
        else:
            err = f"ERROR : {r.status_code}"
            print(err)

    def avoid_empty(self):
        """Avoid to get products that have some empty values"""

        full_products = []
        for p in self.products:
            if (
                p.get("product_name_fr")
                and p.get("code")
                and p.get("brands")
                and p.get("nutriscore_grade")
                and p.get("url")
                and p.get("categories")
                and p.get("image_url")
                and p.get("image_small_url")
                and p.get("nutriments")
                and p.get("nutriscore_grade") is not None
            ):

                full_products.append(p)

        return full_products
