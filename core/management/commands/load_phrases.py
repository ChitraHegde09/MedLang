import csv
from django.core.management.base import BaseCommand
from core.models import Symptom, Phrase

class Command(BaseCommand):
    help = 'Load sample phrases from CSV'

    def handle(self, *args, **kwargs):
        with open('sample_phrases.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                symptom_name = row['symptom'].strip()
                english = row['english'].strip()
                kannada = row['kannada'].strip()

                symptom, created = Symptom.objects.get_or_create(name=symptom_name)
                Phrase.objects.get_or_create(symptom=symptom, english=english, kannada=kannada)
                count += 1
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {count} phrases.'))
