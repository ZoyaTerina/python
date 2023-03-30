import requests
import random
class User:
    def __init__(self):
        self.__lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque odio lectus, commodo accumsan lacus et, rutrum aliquet quam. Sed eget leo eget eros euismod laoreet sit amet vitae massa. Donec dignissim, eros sit amet iaculis fringilla, augue metus mattis ante, in molestie dui est eget mauris. Sed sed tincidunt mi, a interdum lectus. Fusce at erat sed leo mollis vulputate."
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__data["Login"]
        self.__password = self.__data["Password"]
        self.imya = self.__data["FirstName"]
        self.familiya = self.__data["LastName"]
        self.posts = [self.__lorem[random.randint(0, 35):random.randint(36, 70)]]























































