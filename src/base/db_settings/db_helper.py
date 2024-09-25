import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.base.settings import settings
from pymongo import AsyncMongoClient
# from contextlib import asynccontextmanager
# from motormongo import DataBase
#
#
# class DatabaseHelper:
#     """Класс для работы с базой данных
#     """
#     def __init__(self, url: str, echo: bool = False):
#         self.connection_string = url
#         self.client = None
#
#     # @asynccontextmanager
#     # async def get_session(self):
#     #
#     #     self.client: AsyncMongoClient = AsyncMongoClient(self.connection_string)
#     #
#     #     try:
#     #         await self.client.server_info()
#     #         yield self.client[settings.db_name]
#     #     finally:
#     #         await self.client.close()
#
#     @asynccontextmanager
#     async def get_session(self):
#
#         self.client: DataBase = DataBase.connect(uri=self.connection_string, db=settings.db_name)
#
#         try:
#             yield self.client
#         finally:
#             await self.client.close()
#
#
# db_helper = DatabaseHelper(settings.database_url)