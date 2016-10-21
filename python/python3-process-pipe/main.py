from multiprocessing import Process, Pipe
import time

def actor_function(conn):
    count = conn.recv()
    while count < 1000000 and count > 0:
        # print(count)
        conn.send(count + 1)
        count = conn.recv()
    conn.send(-1)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    ping = Process(target=actor_function, args=(parent_conn,))
    pong = Process(target=actor_function, args=(child_conn,))
    ping.start()
    pong.start()

    count = 1
    startTimestamp = time.time()
    parent_conn.send(count)

    ping.join()
    pong.join()

    print(time.time() - startTimestamp)
