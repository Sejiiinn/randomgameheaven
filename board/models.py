from django.db import models

class Main(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_title = models.CharField(max_length = 50)
    game_content = models.CharField(max_length = 255)
    game_img = models.CharField(max_length = 255)

    class Meta():
        db_table = 'game'
        app_label = 'main'
        managed = False