
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Section(models.Model):

    name_section = models.CharField(verbose_name='Name', max_length=20, unique=True)
    color = models.CharField(verbose_name='Color', max_length=20)
    description = models.CharField(verbose_name='Description', max_length=50)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
