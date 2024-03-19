from django.db import models

class Bills(models.Model):
    id_bill = models.IntegerField()
    title = models.TextField()
    primary_sponsor = models.IntegerField()
    

class Legislators(models.Model):
    id_legislator = models.IntegerField()
    name = models.TextField()
    

class Votes(models.Model):
    id_vote = models.IntegerField()
    id_bill = models.IntegerField()


class VotesResults(models.Model):
    id_results = models.IntegerField()
    id_legislator = models.IntegerField()
    id_vote = models.IntegerField()
    vote_type = models.IntegerField()

