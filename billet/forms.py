from django.forms import ModelForm
from allauth.account.forms import SignupForm
from flight.utils import DivErrorList
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



class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
      super(CustomSignUpForm, self).__init__(*args, **kwargs)
      self.error_class = DivErrorList