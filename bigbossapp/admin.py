from django.contrib import admin
from .models import addcontestent
from .models import regmodel,votingmodel
# Register your models here.
class adminreg(admin.ModelAdmin):
    list_display = ['username','password','firstname','lastname','email']
    list_filter = ['firstname']
    class Meta:
        model=regmodel
class admincontestents(admin.ModelAdmin):
    list_display = ['contestent_name','ocuupation','age','born','origin','gender','image']
    list_filter = ['ocuupation']
    class Meta:
        model=addcontestent
class adminvote(admin.ModelAdmin):
    list_display = ['contestent_name','votes']
    list_filter = ['contestent_name']
    class Meta:
        model=votingmodel
admin.site.register(regmodel,adminreg)
admin.site.register(addcontestent,admincontestents)
admin.site.register(votingmodel,adminvote)

