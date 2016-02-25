from system.models import Equipment


def search(keywords, **kwargs):
    keywords = keywords.split()
    result = Equipment.objects.filter(
            equipment_name__icontains=keywords[0]).values_list('pk', flat=True)
    print(list(result))
    for keyword in keywords:
        result = Equipment.objects.filter(
                id__in=list(result),
                equipment_name__icontains=keyword).values_list('pk', flat=True)
    return Equipment.objects.filter(id__in=list(result))
