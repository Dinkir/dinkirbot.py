import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkEventType, VkLongPoll
accessToken = '3e00eea1ccaf8559ab2a4ea80d2ad6782ec6fe069957fb6476fcea4cc56225e1b4d639ea57a857cc58cc4'
vk_session = vk_api.VkApi(token = accessToken)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
def send_mess(message):
	vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=message)
def init_mess(message):
	if command == "привет":
		send_mess("приветик)")
	if command == "как дела?":
		send_mess("шикарно! а у вас?")
	if command == "что ты умеешь":
		send_mess("меня пока что настраивают, так что не чего пока не могу... ;з)")
print('Бот включён')
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		command = event.text
		command = command.lower()
		init_mess(command)