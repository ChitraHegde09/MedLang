from django.contrib import admin
from .models import Symptom, Phrase, UserActivity
admin.site.register(Symptom)
admin.site.register(Phrase)
admin.site.register(UserActivity)
