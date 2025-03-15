from django.core.mail import send_mail
from django.conf import settings
import logging

# Setup logging
logger = logging.getLogger(__name__)

def send_image_notification(action, image):
    subject = f"Image {action}"
    message = f"""
    Operation on the image: {action.upper()}
    
    Title: {image.title}
    ID: {image.id}
    Date: {image.uploaded_at}
    """
    
    try:
        # Checking the parameters
        if not hasattr(settings, 'ADMIN_EMAIL'):
            logger.error("ADMIN_EMAIL not configured in settings")
            return False

        # Sending with verification
        result = send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        
        logger.debug(f"Sending result: {result} message(s) sent")
        return result == 1
        
    except Exception as e:
        logger.exception(f"Critical sending error: {str(e)}")
        return False
