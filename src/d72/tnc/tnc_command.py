import abc

class TncCommand(metaclass=abc.ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass