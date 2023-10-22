from ru.travelfood.simple_ui import NoSQL as noClass
"""
https://uitxt.readthedocs.io/ru/latest/gettingstarted.html#python
Все переменные, события, команды передаются через стек hashMap и возвращаются через него же. 
Помещать в hashMap нужно функцией put(key,value), читать функцией get(key), проверять существование функцией containsKey(key) а удалять remove(key). 
Имейте ввиду что это не словарь Python а Java-объект, вызываемый из Python.
"""
class hashMap:
    def get(self, key: str) -> str:
        """
        Получение значения из hashMap
        """
        pass

    def put(self, key: str, value: str):
        """
        Внесение значения в hashMap
        """
        pass

    def remove(self, key: str):
        """
        Удаление ключа из словаря
        """
        pass
    
    def containsKey(self, key: str) -> bool:
        """
        Проверка на вхождение ключа в словарь
        """
        pass