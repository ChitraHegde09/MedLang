from django.db import models
from django.contrib.auth.models import User

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Phrase(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    english = models.TextField()
    kannada = models.TextField()
    audio_file = models.FileField(upload_to="audio/", blank=True, null=True)
    def __str__(self):
        return f"{self.english} - {self.kannada}"

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    learned_on = models.DateTimeField(auto_now_add=True)
