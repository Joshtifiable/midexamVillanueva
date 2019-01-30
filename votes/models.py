from django.db import models
from datetime import datetime
# Create your models here.

class Candidate(models.Model):
    firstname_text = models.CharField(max_length=100)
    lastname_text = models.CharField(max_length=100)
    #votes = models.ForeignKey(Vote,
    #            on_delete=models.CASCADE, related_name='votes')
    birthdate_field = models.DateTimeField('Date of Birth')
    platform_text = models.CharField(max_length=100)

    def __str__(self):
        return 'Candidate: {}'.format(self.firstname_text)
        return 'Candidate: {}'.format(self.lastname_text)
        return 'Candidate: {}'.format(self.birthdate_field)
        return 'Candidate: {}'.format(self.platform_text)


class Position(models.Model):
    name_text = models.CharField(max_length=100)
    description_text = models.CharField(max_length=250)

    def __str__(self):
        return 'Position: {}'.format(self.name_text)


class Vote(models.Model):
    #candidate = models.ForeignKey(Candidate,
    #            on_delete=models.CASCADE, related_name='candidate')
    votes_count = models.IntegerField(default=0)
    vote_date = models.DateTimeField('Date Voted')

    def __str__(self):
        return 'Vote: {}'.format(self.vote_choice)
