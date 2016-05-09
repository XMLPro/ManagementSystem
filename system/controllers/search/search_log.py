from . import search_core as core
from system.models import Log


def search(keywords, **kwargs):
    equipment_list = core.search(keywords)
    return Log.objects.filter(
           equipment__in=equipment_list).order_by("borrowed_date")
