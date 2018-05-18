class ISubject():
    def addObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notify(self):
        pass


class ProcessOne(ISubject):
    def __init__(self):
        self._observer = []
        self._data = 'processOne data'

    def addObserver(self, observer):
        self._observer.append(observer)

    def removeObserver(self, observer):
        self._observer.remove(observer)

    def notify(self):
        for observer in self._observer:
            observer.update(self)


class ProcessTwo(ISubject):
    def __init__(self):
        self._observer = []
        self._data = 'processTwo data'

    def addObserver(self, observer):
        self._observer.append(observer)

    def removeObserver(self, observer):
        self._observer.remove(observer)

    def notify(self):
        for observer in self._observer:
            observer.update(self)