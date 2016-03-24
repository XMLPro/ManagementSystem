from django.contrib import admin
from .models import CustomUser, Equipment, Search, TagManagement
from .models import Reserved, Request, Vote, Log, Tag

admin.site.register(CustomUser)
admin.site.register(Equipment)
admin.site.register(Search)
admin.site.register(Reserved)
admin.site.register(Request)
admin.site.register(Vote)
admin.site.register(Log)
admin.site.register(TagManagement)
admin.site.register(Tag)
