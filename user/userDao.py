

class User(object):

    def __init__(self):
        self.id = None
        self.name = None
        self.age = None

    def getId(self):
        return self.id

    def setId(self, value):
        self.id = value

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def delName(self):
        del self.name

    def getAge(self):
        return self.age

    def setAge(self, value):
        self.age = value

    def delAge(self):
        del self.age

    def __str__(self):
        return "id:" + self.id + ",name:" + self.name + ",age:" + str(self.age)


