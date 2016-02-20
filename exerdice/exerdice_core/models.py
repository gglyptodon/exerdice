from __future__ import unicode_literals

from django.db import models
import json
import random

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
        return random.choice(self.sides)

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
    def __unicode__(self):
        return str(self.name)
    exercise = models.ForeignKey(to=ExerciseDefinition)
    datetime_performed = models.DateTimeField()
    def __unicode__(self):
        tmp = ""
        if self.datetime_performed:
            tmp = str(self.datetime_performed)
        return str(self.exercise.name + "_task" + tmp)

# todo streak
# todo users
