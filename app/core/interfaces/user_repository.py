from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

class UserRepository(ABC):
    
    @abstractmethod
    async def get_by_email(self, email: str):
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID):
        pass
    
    @abstractmethod
    async def create(self, username: str, email: str, hashed_password: str):
        pass

    @abstractmethod
    async def check_username(self, username: str):
        pass

    @abstractmethod
    async def update_profile(self, first_name: str, last_name: str, avatar_url: str, age: int):
        pass

    @abstractmethod
    async def change_password(self, password: str):
        pass