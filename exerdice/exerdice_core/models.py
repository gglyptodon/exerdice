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


    def __unicode__(self):
        tmp = ""
        if self.datetime_performed:
            tmp = str(self.datetime_performed)
        return str(self.exercise.name + "_task" + tmp)


class Workout(ModelWithTimestamp):
    exercise_tasks = models.ManyToManyField(to=ExerciseTask, null=True, blank=True)
    def __unicode__(self):
        tmp = self.id

        return str(tmp)

def set_amount_randomly(sender, instance, created, **kwargs):
    ExerciseTask.objects.filter(pk=instance.pk).update()
    ed = instance.exercise #FK to ExerciseDefinition
    edd = ed.assoc_dice
    print(edd)
    print(edd.sides)
    amount = 0
    print("amount!")
    for _ in xrange(ed.number_of_dice):
        amount += edd.roll()
    #instance.amount = amount
    ExerciseTask.objects.filter(pk=instance.pk).update(amount=amount)





def set_exercise_randomly(sender, instance, created, **kwargs):
    Workout.objects.filter(pk=instance.pk).update()
    num_exercise_tasks = random.randint(1,5) + random.randint(1,5)
    for _ in xrange(num_exercise_tasks):
        random_idx_ed = random.randint(0, ExerciseDefinition.objects.count() - 1)
        random_obj_ed = ExerciseDefinition.objects.all()[random_idx_ed]
        et = ExerciseTask()
        et.exercise = random_obj_ed
        et.save()
        instance.exercise_tasks.add(et)


signals.post_save.connect(set_exercise_randomly, sender=Workout)
signals.post_save.connect(set_amount_randomly, sender=ExerciseTask)
# todo streak
# todo users
