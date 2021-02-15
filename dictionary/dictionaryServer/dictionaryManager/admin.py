from django.contrib import admin
from dictionaryManager.models import Dictionary

# Register your models here.
@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('word', 'definition', 'example', 'pos')
