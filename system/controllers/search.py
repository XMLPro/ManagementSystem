from system.models import Equipment

def search(keyword):
    result = Equipment.objects.filter(
        equipment_name__icontains=keyword)
    return result
