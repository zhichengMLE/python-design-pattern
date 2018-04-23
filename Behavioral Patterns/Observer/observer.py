# The observer pattern is a software design pattern in which an object, called the subject,
# maintains a list of its dependents, called observers, and notifies them automatically of
# any state changes, usually by calling one of their methods.
# See more in wiki: https://en.wikipedia.org/wiki/Observer_pattern
#
# We will use Observer pattern to build a subscription system which notify all observers
# when you have updates.

# Observer Class
class Observer(object):
    def __init__(self, id):
        self._id = id

    def update(self, message):
        print("Observer %d get the update : %s" %(self._id, message))

# Subject Class: is being observed by Observer
class Subject(object):
    def __init__(self):
        self._observer_list = []
        self._message = ""

    def add_observer(self, observer):
        self._observer_list.append(observer)

    def set_message(self, message):
        self._message = message

    def notify_observers(self):
        for observer in self._observer_list:
            observer.update(self._message)

if __name__ == '__main__':
    subject = Subject()

    subject.add_observer(Observer(1))
    subject.add_observer(Observer(2))
    subject.add_observer(Observer(3))

    subject.set_message("This is the overview of 2016, ...")
    subject.notify_observers()

    subject.add_observer(Observer(4))
    subject.add_observer(Observer(5))

    subject.set_message("This is the overview of 2017, ...")
    subject.notify_observers()

    subject.add_observer(Observer(6))
    subject.set_message("This is the overview of 2018, ...")
    subject.notify_observers()
