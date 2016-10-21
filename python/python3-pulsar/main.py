"""Simple actor message passing"""
from pulsar import arbiter, spawn, send, ensure_future, Config

import time

def start(arbiter, **kw):
    ensure_future(app(arbiter))


async def app(arbiter):
    # Spawn a new actor
    proxy = await spawn(name='actor1')
    print(proxy.name)

    count = 1
    startTimestamp = time.time()
    # Ping in actor1
    while count < 100000:
        count = await send(proxy, 'run', ping, count)
        #
        #await send(proxy, 'run', pingSimple)
        #count += 1

    print(time.time() - startTimestamp)

    # Stop the application
    arbiter.stop()

def ping(actor, value):
    return value + 1

def pingSimple(actor):
    return


if __name__ == '__main__':
    cfg = Config()
    cfg.parse_command_line()
    arbiter(cfg=cfg, start=start).start()
