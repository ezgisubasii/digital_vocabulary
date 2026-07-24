from django.db import models
from profiles.models import Profile

# Create your models here.
class Vocabulary(models.Model):
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name= 'vocabularies')
    name = models.CharField(max_length= 100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.profile.user.username})"
    
class Word(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete= models.CASCADE, related_name= 'words')
    text = models.CharField(max_length= 100)
    meaning = models.CharField(max_length=100)
    example_sentence = models.TextField(blank=True)

    def __str__(self): # we can use this method to return a string representation of the Word object, which can be useful for debugging and displaying the object in the Django admin interface.
        return self.text