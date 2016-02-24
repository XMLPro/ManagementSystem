from system.models import Equipment


def search(keywords, **kwargs):
    result = Equipment.objects.filter(
        equipment_name__icontains=keywords)
    return result
