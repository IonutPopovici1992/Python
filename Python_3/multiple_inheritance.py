class Mario():

    def move(self):
        print('I am moving!')


class Shroom():

    def eat_shroom(self):
        print('Now I am big!')


class BigMario(Mario, Shroom):
    pass


character = BigMario()
character.move()
character.eat_shroom()
