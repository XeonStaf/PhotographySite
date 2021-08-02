import vk_api
from vk_api.utils import get_random_id
from PhotographSite.settings import VK_BOT_TOKEN, VK_GROUP_ID
"""Есть возможность добавлять строчки сообщений для других людей. Main - основное"""

MessageText = {
    'main': {
        'Test': 'Это тестовое сообщение',
        'PhotoReady': 'Привет, {name}!\nТвои фото готовы, можешь найти их тут)\n{result_link} ',
        'ClientChasedPhoto': 'Спасибо за выбор снимков! Скоро я приступлю к обработке',
        'OpenAccessAgain': 'Привет, {name}!\nЯ заново открыл доступ для выбора)\n{chose_link}',
        'OpenAccess': 'Привет, {name}! \nЯ загрузил фотографии на сайт и ты можешь выбрать {num_chose} снимков.\nДля '
                      'этого перейди по ссылочке {chose_link}\n ',
        'Ready': '{username} сделал свой выбор по фотосесии {photoshoot}'
    }
}


def decorate_message(photoshoot, message):
    url = f'https://photoalex.herokuapp.com{photoshoot.get_absolute_url()}'
    params = {
        '{photoshoot}': photoshoot.__str__(),
        '{name}': str(photoshoot.linkUser.first_name),
        '{username}': photoshoot.linkUser.__str__(),
        '{num_chose}': str(photoshoot.num_choose),
        '{chose_link}': url,
        '{result_link}': str(photoshoot.result_link)
    }
    for param in params:
        message = message.replace(param, params[param])
    return message


def send_message(user_id, message, photoshoot):
    message = decorate_message(photoshoot, message)
    vk_session = vk_api.VkApi(token=VK_BOT_TOKEN)
    vk_session_api = vk_session.get_api()
    if vk_session_api.messages.isMessagesFromGroupAllowed(user_id=user_id, group_id=VK_GROUP_ID)['is_allowed']:
        vk_session_api.messages.send(user_id=str(user_id), message=message, random_id=get_random_id())
