from modeltranslation.translator import register, TranslationOptions
from .models import Category, Blog

@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)

@register(Blog)
class BlogTranslationOption(TranslationOptions):
    fields = ('title','subtitle','body','meta_description',)