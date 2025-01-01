from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
