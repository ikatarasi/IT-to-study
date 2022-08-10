class Animal:
    
    def __init__(self, name):
        self.name = name

    
    def say(self):
        print("こんにちは！　私は" + self.name + "です。")


dog = Animal("いぬ")
cat = Animal("ねこ")


dog.say()
cat.say()
