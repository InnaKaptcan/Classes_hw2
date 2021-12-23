import json
from keyword import iskeyword


class DictUnpacking:
    def __init__(self, mapping):
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = DictUnpacking(value)
            else:
                self.__dict__[key] = value


class ColorizeMixin:
    def __init__(self, text_color=32, bg_color=48):
        self.text_color = text_color
        self.bg_color = bg_color

    def __str__(self):
        return f'\033[1;{self.text_color};{self.bg_color}m {self.__repr__()}'


class Advert(ColorizeMixin, DictUnpacking):
    def __init__(self, text):
        ColorizeMixin.__init__(self)
        dict_transformed = DictUnpacking(text).__dict__
        if 'title' not in dict_transformed:
            raise ValueError('The is no title')
        if 'price' in dict_transformed:
            self.price = dict_transformed['price']
            self.__dict__.update(dict_transformed)

    def __repr__(self):
        return f'{self.title} | {self._price} ₽'

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('must be >= 0')
        self._price = new_price


if __name__ == '__main__':
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson_str1 = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    lesson_str2 = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    lesson_str3 = """{"title": "python"}"""
    lesson = json.loads(lesson_str2)
    lesson_ad = Advert(lesson)
    # print(lesson_ad.location.address)
    # print(lesson_ad.location.metro_stations)
    # print(lesson_ad.price)
    print(lesson)
    print(lesson_ad.class_)


