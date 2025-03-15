# tests.py
from django.test import TestCase
from django.urls import reverse

class ImageViewsTestCase(TestCase):

    def test_image_list_view(self):
        # Perform a GET request to the 'image_list' view
        response = self.client.get(reverse('image_list'))
        
        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'images/image_list.html')
        
        # Check that the list of images is correctly passed to the context
        self.assertIn('images', response.context)
