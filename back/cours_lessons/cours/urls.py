from django.urls import path
from .views import CourseListView, LessonListView

urlpatterns = [
    path('api/cours/', CourseListView.as_view(), name='course-list'),
]
