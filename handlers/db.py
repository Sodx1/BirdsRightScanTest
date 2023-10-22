from typing import Union
#https://uitxt.readthedocs.io/ru/latest/no_sql.html
class DB:
    def get(self, key: str) -> str:
        """
        Получает значение по ключу
        """
        pass

    def put(self, key: str, value: Union[str, bool, int], register: bool):
        """
        Помещает значение в указанный ключ
        """
        pass

    def delete(self, key: str):
        """
        Удаляет ключ
        """
        pass

    def getallkeys(self) -> str:
        """
        Получение всех ключей базы в виде строки формата JSON-массива строк
        """
        pass