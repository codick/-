from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_overview),
    path("get_reviews/", views.get_product_reviews),
    path("get_review/<int:pk>/", views.get_product_review),
    path("create_review/", views.create_product_review),
    path("update_review/<int:pk>/", views.update_product_review),
    path("delete_review/<int:pk>/", views.delete_product_review),
]