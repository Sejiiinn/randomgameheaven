from django.db import models
from login.models import user

# Create your models here.

class POST(models.Model):
    user_game_id = models.IntegerField(primary_key=True, max_length=11, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    user_game_title = models.CharField(max_length=50)
    user_game_content = models.TextField()
    user_game_img = models.ImageField()
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'user_game'
        app_label = 'recommendation'
        managed = True
