# back/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from contact.views import contact_form_submission  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contact/', contact_form_submission, name='contact_form_submission'),
]
