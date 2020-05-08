from django.contrib import admin
from movieapp.models import movie

# Register your models here.
class moviead(admin.ModelAdmin):
	list_display=['relyear','movname','hero','heroine','rating']
admin.site.register(movie,moviead)