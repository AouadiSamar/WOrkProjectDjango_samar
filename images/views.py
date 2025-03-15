from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Image

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import UploadedImage
from .forms import ImageUploadForm

# List of images with thumbnails
class ImageListView(View):
    def get(self, request):
        images = UploadedImage.objects.all()
        return render(request, "images/image_list.html", {"images": images})

# Image details
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import UploadedImage
from .forms import ImageUploadForm
from django.core.mail import send_mail
from django.conf import settings

class ImageDetailView(View):
    def get(self, request, pk):
        image = get_object_or_404(UploadedImage, pk=pk)
        form = ImageUploadForm(instance=image)  # Pre-fill the form with current values
        return render(request, "images/image_detail.html", {"image": image, "form": form})

    def post(self, request, pk):
        image = get_object_or_404(UploadedImage, pk=pk)
        form = ImageUploadForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect("image_detail", pk=pk)  # Reload the same page with updated values
        return render(request, "images/image_detail.html", {"image": image, "form": form})

# Upload a new image
from django.shortcuts import render, redirect
from django.views import View
from .forms import ImageUploadForm
from .models import UploadedImage

class ImageUploadView(View):
    def get(self, request):
        form = ImageUploadForm()
        return render(request, "images/image_upload.html", {"form": form})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()

            # Send email if the image is uploaded
            send_mail(
                'New Image Uploaded',
                f'A new image titled "{image.title}" has been uploaded.',
                settings.DEFAULT_FROM_EMAIL,
                ['recipient@example.com'],  # You can Replace it 
                #with your email :Andre Nascimento Neonumy andre.nascimento@neonumy.com
                fail_silently=False,
            )

            return redirect("image_list")
        return render(request, "images/image_upload.html", {"form": form})


class ImageUpdateView(View):
    def get(self, request, pk):
        image = get_object_or_404(UploadedImage, pk=pk)
        return render(request, "images/image_detail.html", {"image": image})

    def post(self, request, pk):
        image = get_object_or_404(UploadedImage, pk=pk)
        form = ImageUploadForm(request.POST, request.FILES, instance=image)

        if form.is_valid():
            if 'image' in request.FILES:
                image.generate_thumbnail()
            form.save()

            # Send an email notification after the image is updated
            send_mail(
                'Image Updated',
                f'The image titled "{image.title}" has been updated.',
                settings.DEFAULT_FROM_EMAIL,
                ['recipient@example.com'],  # Replace with actual recipient email
                fail_silently=False,
            )

            return JsonResponse({
                "success": True,
                "title": image.title,
                "description": image.description,
                "image_url": image.image.url,
                "thumbnail_url": image.thumbnail.url if image.thumbnail else ""
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

# Delete an image
def delete_image(request, pk):
    image = get_object_or_404(UploadedImage, pk=pk)
    image.delete()
    return redirect("image_list")
from django.http import JsonResponse

from django.views.generic.edit import UpdateView
from .models import Image

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Image
from .forms import ImageUploadForm

class ImageUpdateView(View):
    def get(self, request, pk):
        image = get_object_or_404(Image, pk=pk)
        return render(request, "images/image_detail.html", {"image": image})


    def post(self, request, pk):
        image = get_object_or_404(UploadedImage, pk=pk)
        form = ImageUploadForm(request.POST, request.FILES, instance=image)
        
        if form.is_valid():
            if 'image' in request.FILES:
                image.generate_thumbnail()
            form.save()
            return JsonResponse({
                "success": True,
                "title": image.title,
                "description": image.description,
                "image_url": image.image.url,
                "thumbnail_url": image.thumbnail.url if image.thumbnail else ""
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})
