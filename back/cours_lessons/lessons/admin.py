from django.contrib import admin
from .models import Course, Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title',)
    list_filter = ('course',)

