from django.contrib import admin
from chat.models import Message

class MessageAdmin(admin.ModelAdmin):
  fields = ('text','created_at', 'author', 'receiver') #detail view
  search_fields = ('text',)

# Register your models here.
admin.site.register(Message)