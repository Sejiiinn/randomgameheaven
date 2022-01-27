from django.db import models

# Create your models here.


class MovieQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    initial = models.CharField(max_length = 100, null = True)
    answer = models.CharField(max_length = 100, null = True)

    class Meta():
        db_table = 'movie_quiz'
        app_label = 'games'
        managed = False

