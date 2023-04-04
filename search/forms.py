from django import forms


class MainSearchForm(forms.Form):
    """"""
    product_search = forms.CharField(
        label="",
        max_length=70,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Entrez un produit",
                "type": "text",
                "class": "form-control",
                "autofocus": "autofocus",
                "id": "input_autocomplete"
            }
        )
    )
