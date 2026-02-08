from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

    def save(self, *args, **kwargs):
        # Send email notification when creating a new message
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            try:
                self.send_notification_email()
            except Exception as e:
                # Log error but don't fail the save operation
                print(f"Email notification failed: {e}")
                pass

    def send_notification_email(self):
        """Send email notification using Django's send_mail"""
        print(f"🎯 Processing new contact message from {self.name}...")
        
        try:
            subject = f"New Contact Message: {self.subject}"
            message = f"""
Name: {self.name}
Email: {self.email}
Subject: {self.subject}

Message:
{self.message}
"""
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            print(f"✅ Email notification sent successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Email sending failed: {e}")
            return False

    def mark_as_read(self):
        """Mark message as read"""
        self.is_read = True
        self.save(update_fields=['is_read'])
