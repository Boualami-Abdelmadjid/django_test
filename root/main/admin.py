from django.contrib import admin
from main.models import Receipt
from django.contrib.auth.models import User

# Register your models here.


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('user','store_name','purchase_date','item_list','total')
    search_fields = ('user__username',)


# admin.site.register(User)
admin.site.register(Receipt,ReceiptAdmin)

