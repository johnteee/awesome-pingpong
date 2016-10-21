from multiprocessing import Process, Queue
try:
    from Queue import Empty
except ImportError:
    from queue import Empty


class Actor(Process):

    def __init__(self, receive_timeout=None):
        Process.__init__(self)
        self.inbox = Queue()
        self.receive_timeout = receive_timeout

    def send(self, message):
        self.inbox.put_nowait(message)

    def receive(self, message):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def handle_timeout(self):
        pass


    def run(self):
        self.running = True
        while self.running:
            try:
                message = self.inbox.get(True, self.receive_timeout)
            except Empty:
                self.handle_timeout()
            else:
                self.receive(message)
