import gevent
from gevent.queue import Queue
from gevent import Greenlet
from actor import Actor
import time

class Pinger(Actor):
    def receive(self, message):
        pong.inbox.put('ping')
        gevent.sleep(0)

class Ponger(Actor):
    def receive(self, message):
        global count, startTimestamp
        count += 1
        if count > 1000000:
            print(time.time() - startTimestamp)
            gevent.kill(ping)
            gevent.kill(pong)
        else :
            ping.inbox.put('pong')
        gevent.sleep(0)

ping = Pinger()
pong = Ponger()
startTimestamp = int(time.time())
count = 0

ping.start()
pong.start()

ping.inbox.put('start')
gevent.joinall([ping, pong])
