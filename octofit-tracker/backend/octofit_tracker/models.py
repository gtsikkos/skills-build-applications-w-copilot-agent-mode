from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='workouts')
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"
