class IObserver():
    def update(self, subject):
        pass

    def response(self):
        pass


class InsertIntoTableOne(IObserver):
    def __init__(self):
        self._data = ''

    def update(self, subject):
        self._data = subject._data

    def response(self):
        print(self._data)


class InsertIntoTableTwo(IObserver):
    def __init__(self):
        self._data = ''

    def update(self, subject):
        self._data = subject._data

    def response(self):
        print(self._data)