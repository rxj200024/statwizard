from django.db import models

class Averages(models.Model):
    player_name = models.CharField(max_length=255)
    pts = models.FloatField()
    reb = models.FloatField()
    ast = models.FloatField()
    stl = models.FloatField()
    blk = models.FloatField()
    tov = models.FloatField()

    def __str__(self):
      return self.player_name