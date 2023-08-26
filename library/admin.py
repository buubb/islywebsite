from django.contrib import admin
from .models import Library
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Library)
class LibraryAdmin(SummernoteModelAdmin) :
    summernote_fields = ('contents',)
    list_display = (
        'title',
        'contents',
        'writer',
        'writer_dttm',
        'updata_dttm'
    )
    list_display_links = list_display