from django.db import models


class AudioFile(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'