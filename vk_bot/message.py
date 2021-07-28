import vk, vk_api
from vk_api.utils import get_random_id
"""Есть возможность добавлять строчки сообщений для других людей. Main - основное"""

MessageText = {
    'main' : {
        'Test' : 'Это тестовое сообщение',
        'PhotoReady' : 'Привет, {name}!\nТвои фото готовы, можешь найти их тут)\n{result_link} ',
        'ClientChasedPhoto' : 'Спасибо за выбор снимков! Скоро я приступлю к обработке',
        'OpenAccessAgain': 'Привет, {name}!\nЯ заново открыл доступ для выбора)\n{chose_link}',
        'OpenAccess' : 'Привет, {name}! \nЯ загрузил фотографии на сайт и ты можешь выбрать {num_chose} снимков.\nДля этого перейди по ссылочке {chose_link}\n ',
        'Ready' : '{username} сделал свой выбор по фотосесии {photoshoot}'
    }
}


def decorate_message(photoshoot, message):
    url = f'http://127.0.0.1:8000{photoshoot.get_absolute_url()}'
    params = {
        '{photoshoot}' : photoshoot.__str__(),
        '{name}' : str(photoshoot.linkUser.first_name),
        '{username}' : photoshoot.linkUser.__str__(),
        '{num_chose}' : str(photoshoot.num_choose),
        '{chose_link}' : url,
        '{result_link}' : str(photoshoot.result_link)
    }
    for param in params:
        message = message.replace(param, params[param])
    return message


token = "b1e7fd311fc53a7c0b5a169a0e3f058c45f6c641b8fd639297e9dd5adbbcd7a7ebeced2f7419f4ecbe753"



def send_message(user_id, message, photoshoot):
    message = decorate_message(photoshoot, message)
    vk_session = vk_api.VkApi(token=token)
    vk_session_api = vk_session.get_api()
    vk_session_api.messages.send(user_id=str(user_id), message=message, random_id=get_random_id())


