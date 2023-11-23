from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def tick(self):
        pass
