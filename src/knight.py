class Knight:
    def __init__(self, name):
        self._name = name
        with open("py3basics_2.1/py3basics/DATA/knights.txt") as f:
            knights = f.read().splitlines()
            for knight in knights:
                name, title, fav_color, quest, comment = knight.split(":")
                if self._name == name:
                    self._title = title
                    self._favorite_color = fav_color
                    self._quest = quest
                    self._comment = comment
                    

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def title(self):
        return self.name
    @title.setter
    def title(self, title):
        self._title = title
    @property
    def favorite_color(self):
        return self.favorite_color
    @favorite_color.setter
    def favorite_color(self, favorite_color):
        self._favorite_color = favorite_color
    @property
    def quest(self):
        return self.quest
    @quest.setter
    def quest(self, quest):
        self._quest = quest
    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self, comment):
        self._comment = comment
    
    def printInfo(self):
        print(f"{self._title} {self._name} their favorite color is {self._favorite_color}, their quest is {self._quest}. {self._comment}")

