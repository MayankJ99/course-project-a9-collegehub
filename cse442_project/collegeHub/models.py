from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
# Create your models here.


CurrentUser = get_user_model()


class User(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class Experiences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True, related_name='experience')


class Section(models.Model):
    name = models.CharField(max_length=30)
    experiences = models.ForeignKey(Experiences, on_delete=models.CASCADE, related_name='section')


class Specific(models.Model):
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    description = models.CharField(max_length=2000)
    bullet_section = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def get_bullet_list(self):
        return self.bullet_section.split(', ')






