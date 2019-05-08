
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from cake import views
router = routers.SimpleRouter()
router.register(r'cake', views.CakeViewSet)

urlpatterns = router.urls