from django.contrib import admin
from django.urls import path
from myapp.views import booking_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', booking_view, name="booking"),
]
