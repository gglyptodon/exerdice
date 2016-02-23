from __future__ import unicode_literals

from django.db import models
import json
import random
from django.db.models import signals

class ModelWithTimestamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Die(ModelWithTimestamp):

    def __unicode__(self):
        return str(self.name)

    def set_sides(self, x):
        self.sides = json.dumps(x)

    def get_sides(self, x):
        return json.loads(self.sides)
    sides = models.CharField(max_length=200)
    name = models.CharField(max_length=50, unique=True)

    def roll(self):
        return int(random.choice(json.loads(self.sides)))

    class Meta:
        verbose_name_plural = "dice"


class ExerciseDefinition(ModelWithTimestamp):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    assoc_dice = models.ForeignKey(to=Die)
    unit = models.CharField(max_length=50, null=True, blank=True)
    number_of_dice = models.IntegerField(default=1)

    def __unicode__(self):
        return str(self.name)

class ExerciseTask(ModelWithTimestamp):
    exercise = models.ForeignKey(to=ExerciseDefinition)
    amount = models.IntegerField(null=True, blank=True)
    datetime_performed = models.DateTimeField(null=True, blank=True)
    def str_for_display(self):
        if self.exercise.description:
            return "{}: {}".format(self.exercise.description, self.amount)

        return "{}: {}".format(self.exercise.name, self.amount)
    def __unicode__(self):
        return self.str_for_display()
#         tmp = ""
#         if self.amount:
#             tmp = str(self.amount)
#         if self.datetime_performed:
#             tmp += str(self.datetime_performed)
#         return str(self.exercise.name + " Amount: " + tmp)
# #:w

# class WorkoutTask(ModelWithTimestamp):
#      exercise_task = models.ForeignKey(ExerciseTask)
#      workout = models.ForeignKey(Workout)




class Workout(ModelWithTimestamp):
    exercise_tasks = models.ManyToManyField(to=ExerciseTask)

    def __unicode__(self):
        tmp = self.id
        if self.exercise_tasks:
            print(self.exercise_tasks)
            return str(self.exercise_tasks.all())
            #tmp = ",".join([str(x) for x in self.exercise_tasks])
            tmp = str(self.id)+",".join([str(val.name) for val in ExerciseTask.objects.all() if val in self.exercise_tasks.all()])

        return str(tmp)



def set_amount_randomly(sender, instance, created, **kwargs):
    ExerciseTask.objects.filter(pk=instance.pk).update()
    ed = instance.exercise #FK to ExerciseDefinition
    edd = ed.assoc_dice
    amount = 0
    print("amount!")
    for _ in xrange(ed.number_of_dice):
        amount += edd.roll()
    ExerciseTask.objects.filter(pk=instance.pk).update(amount=amount)


signals.post_save.connect(set_amount_randomly, sender=ExerciseTask)
# todo streak
# todo users
