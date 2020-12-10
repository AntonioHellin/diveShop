from django.contrib import admin
from ordersManage.models import Client, Article, Order

class ClientsAdmin(admin.ModelAdmin): 
    list_display = ("name", "address", "email", "phone")
    search_fields = ("name", "email")

class ArticlesAdmin(admin.ModelAdmin):
    list_filter = ("name", "section")
    search_fields = ("name", "section")

class OrdersAdmin(admin.ModelAdmin):
    list_display = ("number", "date")
    list_filter = ("date", )
    date_hierarchy = "date"


admin.site.register(Client, ClientsAdmin)
admin.site.register(Article, ArticlesAdmin)
admin.site.register(Order, OrdersAdmin)
