from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.conf import settings
import openai
from googletrans import Translator

openai.api_key = settings.OPENAI_API_KEY
translator = Translator()

@receiver(pre_save, sender=settings.BLOG)
def add_gpt_response(instance, *args, **kwargs):
    if not instance.body:
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": instance.title},
            {"role": "user", "content": instance.title},
        ])
        message = response.choices[0]['message']
        translate_ru = translator.translate("{}".format(message['content']),dest='ru')
        translate_uz = translator.translate("{}".format(message['content']),dest='uz')
        instance.body = "{}".format(message['content'])
        instance.body_en = "{}".format(message['content'])
        instance.body_ru = translate_ru.text
        instance.body_uz = translate_uz.text
        instance.save()