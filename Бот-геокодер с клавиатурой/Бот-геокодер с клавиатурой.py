import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from images import check_get_image


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device


def get_attachments(text, upload):
    res = True
    if check_get_image(text):
        image = "image.jpg"
    else:
        image = "error.png"
        res = False
    attachments = []
    upload_image = upload.photo_messages(photos=image)
    attachments.append(f"photo{upload_image[0]['owner_id']}_{upload_image[0]['id']}")
    return attachments, res


def main():
    login, password = "ваш логин", "ваш пароль"
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler,
        token="ваш токен",
        app_id=6287487
    )
    longpoll = VkBotLongPoll(vk_session, 225383346)
    upload = VkUpload(vk_session)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text = event.obj.message['text']
            vk = vk_session.get_api()
            res = get_attachments(text, upload)
            attachments = res[0]
            if res[1]:
                message = f'Это {text}. Что вы еще хотите увидеть?'
            else:
                message = "Проблемы с поиском местности"
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=message,
                             random_id=random.randint(0, 2 ** 64),
                             attachment=','.join(attachments))


if __name__ == '__main__':
    main()
