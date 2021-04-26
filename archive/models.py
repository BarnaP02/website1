from django.db import models

import random

class Story(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=9)
    access_level = models.CharField(max_length=1)
    content = models.CharField(max_length=50000)

class user(models.Model):
    nev=models.CharField(max_length=20)
    jelszo=models.CharField(max_length=20)
    anonymus=models.IntegerField(default=0000)
    access_level=models.CharField(max_length=1, default=1)
    def form(POST):
        if user.objects.filter(nev = POST['name'], jelszo = POST['password']):
            return True
        else:
            return False
    def __str__(self):
        return self.nev
    def registration(POST):        
        return user.objects.create(nev=POST["name"], jelszo=["password"], anonymus=hash(POST["name"],POST["password"]))