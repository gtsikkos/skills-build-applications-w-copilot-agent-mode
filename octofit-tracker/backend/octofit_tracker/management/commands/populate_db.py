from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='Run', duration=30, distance=5)
        app_models.Activity.objects.create(user=batman, type='Swim', duration=45, distance=2)
        app_models.Activity.objects.create(user=superman, type='Bike', duration=60, distance=20)
        app_models.Activity.objects.create(user=captain, type='Run', duration=25, distance=4)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='A quick morning run', suggested_for=marvel)
        app_models.Workout.objects.create(name='Strength Training', description='Heavy lifting', suggested_for=dc)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
