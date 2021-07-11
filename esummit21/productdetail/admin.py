from django.contrib import admin
from .models import Player,TEST_STATS,ODI_STATS,T20I_STATS,IPL_STATS
# Register your models here.

admin.site.register(Player)
admin.site.register(TEST_STATS)
admin.site.register(ODI_STATS)
admin.site.register(T20I_STATS)
admin.site.register(IPL_STATS)