from django.contrib import admin
from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Assurez-vous que ces champs existent dans le modèle Course
    search_fields = ('name',)
    list_filter = ('name',)  # Assurez-vous que 'name' est un champ valide pour le filtrage

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title',)
    list_filter = ('course',)
