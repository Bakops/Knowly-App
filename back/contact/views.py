from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactFormSubmission


@csrf_exempt
def contact_form_submission(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            status = data.get('status')
            message = data.get('message')

            ContactFormSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                status=status,
                message=message
            )

            return JsonResponse({'message': 'Form submitted successfully!'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
