# -*- coding:utf-8 -*-

from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=200)
    subject_id = models.ForeignKey(Subjects)

    def __str__(self):
        return self.name + " -> " + str(self.subject_id)

class Tasks(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    variables = models.TextField()
    ask = models.TextField()
    variant_id = models.ForeignKey(Variant)

    def __str__(self):
        return str(self.number) + " -> " + str(self.variant_id)
