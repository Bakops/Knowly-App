from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Course

@csrf_exempt
def get_courses(request):
    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        search_query = request.GET.get('search', '')

        courses = Course.objects.filter(name__icontains=search_query)
        paginator = Paginator(courses, page_size)
        page_obj = paginator.get_page(page_number)

        data = {
            'courses': list(page_obj.object_list.values()),
            'total_pages': paginator.num_pages,
            'current_page': page_obj.number,
        }

        return JsonResponse(data, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
