from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.CharField(max_length=255, blank=True)
    gamertag = models.CharField(max_length=255, blank=True)
    paypal = models.EmailField(max_length=255, blank=True)
    team = models.ForeignKey("hoster.Team", on_delete=models.CASCADE, null=True, blank=True)
    paid = models.ManyToManyField("hoster.Tournament", related_name='paid', blank=True)
    tier = models.IntegerField(null=True, blank=True, default=4)

    class Meta:
        db_table = "Profile"

    def __str__(self):
        return self.user.username