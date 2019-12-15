from django.conf.urls import url
from items.views import profile

urlpatterns = [
    url(r'', profile, name='profile'),
]

  