from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Slide, Options, Contact, About


# Apply summernote to all TextField in model.
class OptionsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Slide)
admin.site.register(Contact)
admin.site.register(About, OptionsModelAdmin)
admin.site.register(Options, OptionsModelAdmin)