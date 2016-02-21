from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Die, ExerciseDefinition, ExerciseTask, Workout



class DieAdmin(admin.ModelAdmin):
    pass

class ExerciseTaskAdmin(admin.ModelAdmin):
    pass

class ExerciseDescriptionAdmin(admin.ModelAdmin):
    pass

class WorkoutAdmin(admin.ModelAdmin):
    pass

admin.site.register(Die, DieAdmin)
admin.site.register(ExerciseTask, ExerciseTaskAdmin)
admin.site.register(ExerciseDefinition, ExerciseDescriptionAdmin)
admin.site.register(Workout, WorkoutAdmin)