from multiprocessing import Process, Queue
import time

from actor import Actor
# import pyximport; pyximport.install()
# from actor_c import Actor

class Pinger(Actor):
    def receive(self, message):
        # print("ping")
        pong.inbox.put('ping')

class Ponger(Actor):
    def receive(self, message):
        global count, startTimestamp
        global ping, pong
        count += 1
        if count > 100000:
            print(time.time() - startTimestamp)
            msg.put('end')
            return;
        else :
            ping.inbox.put('pong')

msg = Queue()
ping = Pinger()
pong = Ponger()
startTimestamp = time.time()
count = 0

ping.start()
pong.start()

ping.inbox.put('start')

while msg.get() is None:
    pass

ping.terminate()
pong.terminate()
msg.close()
ping.join()
pong.join()
