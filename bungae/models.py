from django.db import models
from datetime import datetime
from login.models import user

# Create your models here.



class Board(models.Model):
    board_num = models.IntegerField(primary_key=True, max_length=10, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    title = models.TextField()
    content = models.TextField()
    cre_date = models.TimeField()
    board_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'board'
        app_label = 'bungae'
        managed = True
