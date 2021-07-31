from django.db import models
from photoshoots.models import photo_shoot
from django.dispatch import receiver
from photoshoots.utility import States_for_model
from .message import MessageText, send_message
from allauth.socialaccount.models import SocialAccount


@receiver(models.signals.pre_save, sender=photo_shoot)
def photo_shoot_change_status(sender, instance, **kwargs):
    try:
        old_state = photo_shoot.objects.get(pk=instance.pk).state
    except:
        old_state = 1
    new_state = instance.state
    if old_state != new_state:
        text_old_state = States_for_model[old_state - 1][1]
        text_new_state = States_for_model[new_state - 1][1]
        message = MessageText['main']
        user_id = SocialAccount.objects.get(user=instance.linkUser).uid
        photographer = '152855497'
        if text_new_state == "Отправлено":
            send_message(user_id, message['PhotoReady'], instance)

        if text_new_state == "Выбрано":
            send_message(user_id, message['ClientChasedPhoto'], instance)
            send_message(photographer, message['Ready'], instance)

        if text_new_state == "Необходимо Выбрать":
            if text_old_state == "Выбрано":
                send_message(user_id, message['OpenAccessAgain'], instance)
            else:
                send_message(user_id, message['OpenAccess'], instance)
