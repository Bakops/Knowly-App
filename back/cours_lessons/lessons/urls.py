from django.urls import path
from .views import CourseListView, LessonListView

urlpatterns = [
    path('api/courses/', CourseListView.as_view(), name='course-list'),
    path('api/lessons/', LessonListView.as_view(), name='lesson-list'),
]
