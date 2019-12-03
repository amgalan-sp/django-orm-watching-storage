from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import is_visit_long
from datacenter.models import get_time
from datacenter.models import format_time

def storage_information_view(request):
    
    non_closed_visits = [
        {
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": format_time(timezone.now() - visit.entered_at),
            "is_strange": is_visit_long(visit)            
        } for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
