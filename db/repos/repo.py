from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    async def get(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, filters: dict):
        raise NotImplementedError

    @abstractmethod
    async def add(self, instance):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int):
        raise NotImplementedError