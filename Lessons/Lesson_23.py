######### Chat_bot ###########

import requests
import random

privat_key = '5127302253:AAH2iCFI0n_ogoAnv3UR0-6VqFdvuq7xHfY'
# url = f' t.me/QA_IT_Education_bot[\{privat_key}/'
url = f'https://api.telegram.org/bot{privat_key}/'


def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            q = {'name': 'QA_IT_Education_bot', 'money': '0'}
            if get_message_text(update).lower() in q:
            # if get_message_text(update).lower() == 'hi' or get_message_text(
            #         update).lower() == 'hello' or get_message_text(update).lower() == 'hey':
                send_message(get_chat_id(update), "Greetings! Type 'Dice'")

            if q[get_message_text(update).lower()]:
                send_message(get_chat_id(update),q[get_message_text(update).lower()]
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
            elif get_message_text(update).lower() == 'name':
            else:
                send_message(get_chat_id(update), "Sorry, I don't undersand you :(")
            update_id += 1


if __name__ == '__main__':
    main()