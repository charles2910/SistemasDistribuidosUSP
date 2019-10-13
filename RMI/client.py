from datetime import datetime

import Pyro4


server = Pyro4.Proxy("PYRO:obj_29a852aa81c642a8945ac3af0c0e8fd3@192.168.0.157:9001")

def start_chatting():
    text = ''
    nick = input("Type your nickname: ")
    server.chat_new(nick)
    while (text != 'exit'):
        text = input("Type a text: ")
        now = datetime.now()
        server.send_message(text)
        print(f'sent at {now:%H:%M:%S} \n')

if __name__ == '__main__':
    try:
        start_chatting()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit