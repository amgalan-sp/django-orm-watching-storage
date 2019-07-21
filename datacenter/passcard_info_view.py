from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import is_visit_long
from datacenter.models import get_time
from datacenter.models import format_time

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)

    this_passcard_visits = [
        {
            "entered_at": visit.entered_at,
            "duration": format_time(get_time(visit.leaved_at) - visit.entered_at),
            "is_strange": is_visit_long(visit)
        } for visit in Visit.objects.filter(passcard=passcard),
    ]
    context = {
        "passcard": passcard[0],
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
