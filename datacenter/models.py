from django.db import models
from django.utils import timezone
import datetime


def get_time(time):
  if time:
    return time
  else:
    return timezone.now()


def is_visit_long(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at > datetime.timedelta(0, 3600)
    else:
        return timezone.now() - visit.entered_at > datetime.timedelta(0, 3600)


def format_time(time):
    return str(time).split(".")[0]


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
