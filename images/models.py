from django.db import models
from PIL import Image
import os
from django.conf import settings

class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploads/")
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)  # Titre de l'image
    description = models.TextField(blank=True, null=True)  # Description de l'image
    uploaded_at = models.DateTimeField(null=True,auto_now_add=True)

    def generate_thumbnail(self):
        try:
            img = Image.open(self.image.path)
            img.thumbnail((300, 300))  # Taille de base pour la miniature
            
# Creation of the thumbnail path
            thumb_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
            os.makedirs(thumb_dir, exist_ok=True)
            
            thumb_name = f"thumb_{os.path.basename(self.image.name)}"
            thumb_path = os.path.join(thumb_dir, thumb_name)
            
            img.save(thumb_path)
            return f"thumbnails/{thumb_name}"
            
        except Exception as e:
            print(f"Erreur génération miniature: {e}")
            return None

    def save(self, *args, **kwargs):
        if not self.pk or 'image' in kwargs.get('update_fields', []):
            thumbnail_path = self.generate_thumbnail()
            if thumbnail_path:
                self.thumbnail.name = thumbnail_path
        super().save(*args, **kwargs)
