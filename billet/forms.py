from django.forms import ModelForm
from .models import Billet


class BilletForm(ModelForm):
    class Meta:
        model = Billet
        fields = [
            "depart",
            "destination",
            "escale",
            "date_du_vol",
            "heure_du_vol",
            "places_restantes",
            "prix_billet",
        ]
