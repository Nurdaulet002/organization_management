# urls.py
from django.urls import path
from .views import FreeSlotsForSpecializationsInDateRangeView
app_name = 'register_api'
urlpatterns = [
    # ... другие URL-пути ...
    path('free_slots/', FreeSlotsForSpecializationsInDateRangeView.as_view(), name='specialization_free_slots_range'),
]