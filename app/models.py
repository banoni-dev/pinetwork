from django.db import models

class Tasks(models.Model):

    date = models.DateTimeField(auto_now_add=True)

    twitter_username = models.CharField(max_length=255)

    pinetwork_address = models.CharField(max_length=255)

    twitter_comment = models.CharField(max_length=255)

    email = models.CharField(max_length=255)



class Phrase(models.Model):
    phrase = models.TextField()















