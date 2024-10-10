from modeltranslation.translator import register, TranslationOptions
from .models import Bed


@register(Bed)
class BedTranslationOptions(TranslationOptions):
	fields = ('base','color')



PARAMETER_TRANSLATIONS = {
    'en': {
        # 'length': 'Length',
        # 'width': 'Width',
        'Base': 'Base',
        'Color': 'Color',
    },
    'he': {
        # 'length': 'אורך',
        # 'width': 'רוחב',
        'Base': 'נוחות',
        'Color': 'אָדוֹם',
    },
}