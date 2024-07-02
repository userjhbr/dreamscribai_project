from django.db import models

class Dream(models.Model):
    dream_text = models.TextField()
    health_status = models.CharField(max_length=100)
    relationships = models.CharField(max_length=100)
    feelings_during = models.CharField(max_length=100)
    feelings_after = models.CharField(max_length=100)
    dream_context = models.CharField(max_length=100)
    dream_frequency = models.CharField(max_length=100)
    culture_and_beliefs = models.CharField(max_length=100)
    psychological_state = models.CharField(max_length=100)

    def __str__(self):
        return self.dream_text[:50]  # Exibir os primeiros 50 caracteres do texto do sonho

