import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName())


x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name='Receive messages')
x.start()
y.start()
