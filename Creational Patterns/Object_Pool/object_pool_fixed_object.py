import threading
import time
from random import random

class Proxy:
    def __init__(self, object, object_pool):
        self._object = object
        self._object_pool = object_pool

    def __enter__(self):
        return self._object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._object_pool._release_object(self._object)

class Object_Pool:
    _instance = None

    def __init__(self, objects):
        # Object Pool should be a singleton class
        if Object_Pool._instance is not None:
            print("This class has already created:", self.getInstance())

        self._list = []
        # Initialize the object pool
        for object in objects:
            self._list.append(object)

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = Object_Pool()
        return cls._instance

    def allocate_object(self):
        # Wait until object resource is ready
        while(len(self._list) <= 0):
            time.sleep(random())

        # Get the object instance from the queue.
        return Proxy(self._list.pop(), self)

    def _release_object(self, object):
        # Put the object instance back to the queue.
        self._list.append(object)


class Server():
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

class Client(threading.Thread):
    def __init__(self, id, obj_pool):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        with object_pool.allocate_object() as server:
            print('Client %d is using server %d' % (self.id, server.get_id()))
            time.sleep(random())  # Pretend to work for a second
            print('Client %d released server %d' % (self.id, server.get_id()))


if __name__ == '__main__':
    # Try to play around with the server v.s. client number.
    server_number = 5
    client_number = 10

    object_pool = Object_Pool([Server(server_id) for server_id in range(server_number)])

    for i in range(client_number):
        client = Client(i, object_pool)
        client.start()
