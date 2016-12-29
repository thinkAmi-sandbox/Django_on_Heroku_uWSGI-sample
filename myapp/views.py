from django.views.generic import ListView
from .models import Fruits

class FruitsListView(ListView):
    model = Fruits

