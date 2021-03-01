from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationAdmin
import landing.translations

# Register your models here.
from models import Options, Contact, About, Phone, Partners, Features


# Apply summernote to all TextField in model.
class OptionsModelAdmin(SummernoteModelAdmin, TabbedTranslationAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

class TransAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Contact, OptionsModelAdmin)
admin.site.register(About, OptionsModelAdmin)
admin.site.register(Options, OptionsModelAdmin)
admin.site.register(Features, OptionsModelAdmin)
admin.site.register(Partners)
admin.site.register(Phone)