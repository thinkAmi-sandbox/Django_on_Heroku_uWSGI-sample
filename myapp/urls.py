from django.conf.urls import url
from .views import FruitsListView

urlpatterns = [
    url(r'^$', FruitsListView.as_view(), name='mylist'),
]