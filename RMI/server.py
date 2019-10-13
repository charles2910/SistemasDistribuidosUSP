from datetime import datetime

import Pyro4

@Pyro4.expose
class Chat(object):
    
    def chat_new(self, nick):
      self.nick = nick
    
    def send_message(self, text):
        now = datetime.now()
        print(f'{self.nick} said: {text} - received at {now:%H:%M:%S} \n')

def start_server():
    daemon = Pyro4.Daemon(host="192.168.0.157",port=9001)
    uri = daemon.register(Chat)
    print("Ready. Object uri =", uri)
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit