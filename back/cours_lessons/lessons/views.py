from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Lesson

@csrf_exempt
def get_lessons(request, course_id):
    if request.method == 'GET':
        lessons = Lesson.objects.filter(course_id=course_id)
        data = {
            'lessons': list(lessons.values())
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
