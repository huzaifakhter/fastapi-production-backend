from abc import ABC, abstractmethod
from typing import Optional

class UserRepository(ABC):
    
    @abstractmethod
    async def get_by_email(self, email: str):
        pass
    
    @abstractmethod
    async def create(self, username: str, email: str, hashed_password: str):
        pass

    @abstractmethod
    async def check_username(self, username: str):
        pass