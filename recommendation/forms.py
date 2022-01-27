from attr import fields
from django.forms import ModelForm
from recommendation.models import *


from recommendation.models import Post


class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user_game_id', 'user', 'user_game_title' , 'user_game_content', 'user_game_img', 'date_time']