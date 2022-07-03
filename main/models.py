from django.db import models

class event(models.Model):
    eventName = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    # poster = models.ImageField(null=True, blank=True, upload_to="images/")
    loc = models.CharField(max_length=50)
    fromDate = models.DateField()
    fromTime = models.TimeField()
    toDate = models.DateField()
    toTime = models.TimeField()
    regEndDate = models.DateField()
    regEndTime = models.TimeField()
    # posterLink = models.CharField(max_length=10000, blank=True)
    hostEmail = models.EmailField()
    hostPswd = models.CharField(max_length=50)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.eventName

class participant(models.Model):
    participantName = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    regType = models.CharField(max_length=10)
    noOfTickets = models.IntegerField()
    eventID = models.IntegerField()
    def __str__(self):
        return self.participantName