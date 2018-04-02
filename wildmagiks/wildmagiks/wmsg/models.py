from django.db import models

class WildMagicSurgeEffect(models.Model):
    effect = models.CharField(max_length=200)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.effect
