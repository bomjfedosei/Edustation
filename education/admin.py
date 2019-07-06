from django.contrib import admin
from .models import BotDialog
from .models import Connections
from .models import Courses
from .models import Schools

# Register your models here.
admin.site.register(BotDialog)
admin.site.register(Connections)
admin.site.register(Courses)
admin.site.register(Schools)
