from django.contrib import admin

from .models import Transaction, Categories, Organizations


admin.site.register(Transaction)
admin.site.register(Categories)
admin.site.register(Organizations)
