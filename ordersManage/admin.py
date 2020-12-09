from django.contrib import admin
from ordersManage.models import Client, Article, Order

class ClientsAdmin(admin.ModelAdmin):
    
    list_display = ("name", "address", "email", "phone")
    search_fields = ("name", "email")

admin.site.register(Client, ClientsAdmin)
admin.site.register(Article)
admin.site.register(Order)
