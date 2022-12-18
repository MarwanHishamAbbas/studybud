from django.db import models
from django.contrib.auth.models import User



class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) :
        return self.name


class Room(models.Model):
    # ForeignKey -> Depending on the User class
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # this attr can't be blank (in database table)
    participents = models.ManyToManyField(User, related_name='participents', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # auto_now -> take a date snapshot everytime this updated
    # auto_now_add -> take a date snanshot only once this created

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']

# Many to one relationship with room
class Message(models.Model):
    # CASCADE -> if User get deleted the Message will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class Meta: 
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.body[0:50]
