import abc


class BaseEvent(abc.ABC):

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass
