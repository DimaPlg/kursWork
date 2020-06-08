#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import get_pictures
import webbrowser
import necdot

token ='492391ef1936fb4dcafa450110cef1a9cddddf86c2657f27ab42eb84f2cb79b661ec0949da05aaf9ee950'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})
            elif response == "котик":
                attachment = get_pictures.get(vk_session, -23300841, session_api)
                vk_session.method("messages.send",
                                  {"user_id": event.user_id, 'message': " ", "attachment": attachment,
                                   "random_id": 0})
            elif response == "анекдот":
                attachment = nekdot.get(vk_session, -29103840, session_api)
                vk_session.method("messages.send",
                                  {"user_id": event.user_id, 'message': " ", "attachment": attachment,
                                   "random_id": 0})
            elif response == "пока":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Пока, друг!', 'random_id': 0})