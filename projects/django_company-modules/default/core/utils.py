import json
from django.http import HttpResponse


def response_trigger(
    status_code: int, msg: str = None, event_instance=None, **hx_triggers
):
    # in the moment msg and event_instance are not being used, but they are here for future use

    return HttpResponse(
        status=status_code, headers={"HX-Trigger": json.dumps(hx_triggers)}
    )
