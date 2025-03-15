from django.urls import path

from django.urls import path
from .views import ImageListView,ImageUpdateView, ImageDetailView, ImageUploadView, delete_image

urlpatterns = [
    path("", ImageListView.as_view(), name="image_list"),
        path("image/<int:pk>/update/", ImageUpdateView.as_view(), name="image_update"),

    path("upload/", ImageUploadView.as_view(), name="image_upload"),
    path("image/<int:pk>/", ImageDetailView.as_view(), name="image_detail"),
    path("image/<int:pk>/delete/", delete_image, name="image_delete"),
]
