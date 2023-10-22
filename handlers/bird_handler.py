import json
from db import DB
from hashMap import hashMap
from ru.travelfood.simple_ui import NoSQL as noClass

db_all_birds: DB = noClass("birds")

#Процесс "Птицы" 
#Экраны 
def birds_list(hashMap: hashMap, _files=None, _data=None):
    """
    Экран "Птицы"
    """
    #https://uitxt.readthedocs.io/ru/latest/common_functions.html
    birds_cards = {
    "customcards": {
        "options": {
          "search_enabled": True,
          "save_position": True
        },

        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                            "type": "Picture",
                            "Value": "@bird_picture",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 1
                        },
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "Value": "@bird_name",
                                    "NoRefresh": False,
                                    "TextSize": "16",
                                    "TextColor": "#000000",
                                    "gravity_horizontal": "left",
                                },
                                {
                                    "type": "TextView",
                                    "Value": "@bird_color",
                                    "NoRefresh": False,
                                    "TextSize": "16",
                                    "TextColor": "#000000",
                                    "gravity_horizontal": "left",
                                },
                            ]
                        },
                    ]
                },
            ]
        }
        }
    }

    birds_cards["customcards"]["cardsdata"] = []

    #Получаемы из JSON всех доступных птиц
    keys_str = db_all_birds.getallkeys()
    keys = json.loads(str(keys_str).encode("utf-8"))
    for key in keys:
        bird = get_bird_data_by_key(key=key)
        bird["bird_name"] = "Название птицы: " + key
        bird["bird_color"] = "Цвет перьев птицы: " + bird.get("bird_color")
        birds_cards["customcards"]["cardsdata"].append(bird)
    hashMap.put(
        "cardsbirds",
        json.dumps(birds_cards, ensure_ascii=False)
    )
    return hashMap


# Обработчики кнопок для процесса птицы

#Добавить кнопку добавления птицы
def show_add_bird_screen(hashMap: hashMap, _files=None, _data=None):
    """
    Запуск экрана с добавление птицы
    """
    hashMap.put("ShowScreen", "Добавление птицы")
    return hashMap

#Метод создать птицу
def create_bird(hashMap: hashMap, _files=None, _data=None):
    """
    Создание птицы
    """

    bird_name = hashMap.get("bird_name")
    if db_all_birds.get(bird_name):
        hashMap.put("toast", "Птица с данным названием уже базе.")
        return hashMap

    bird_color = hashMap.get("bird_color")

    if bird_name == "" or bird_color == "":
        hashMap.put("toast", "Введите все значения полей")
        return hashMap

    bird_data = {
        "bird_color": bird_color,
        "bird_picture": hashMap.get("photo"),
    }
    db_all_birds.put(
        bird_name,
        json.dumps(bird_data, ensure_ascii=False),
        True
    )

    hashMap.put("toast", f"Птица {bird_name} успешно создана.")


    return hashMap


def get_bird_data_by_key(key: str) -> dict:

    bird_data_str = db_all_birds.get(key)
    bird_data = json.loads(bird_data_str)
    bird = {
        "key": key,
        "bird_name": key,
        "bird_color": bird_data.get("bird_color"),
        "bird_picture": bird_data.get("bird_picture"),
    }
    return bird


def show_bird_screen(hashMap: hashMap, _files=None, _data=None):
    """
    Показать конкретную птицу из списка
    """

    hashMap.put("ShowScreen", "Птица")
    bird_name = hashMap.get("selected_card_key")

    bird_data = get_bird_data_by_key(key=bird_name)

    hashMap.put("bird_name", bird_data.get("bird_name"))
    hashMap.put("bird_color", bird_data.get("bird_color"))
    hashMap.put("bird_picture", bird_data.get("bird_picture"))

    return hashMap
