"""
class Movecharacter:
    def move_fwd(self):
        print("move 1 step forward")

    def move_bwd(self):
        print("move 1 step backward")


class Jumpcharacter:
    def jump_1char(self):
        print("jump 1 step")

    def jump_2char(self):
        print("jump 2 step")


class Pokemon(Movecharacter,Jumpcharacter):
    pass


p = Pokemon()
p.move_fwd()
p.move_bwd()
p.jump_1char()
p.jump_2char()

"""
class Movecharacter:
    def move_fwd(self):
        print("move 1 step forward")

    def move_bwd(self):
        print("move 1 step backward")


class Jumpcharacter:
    def jump_1char(self):
        print("jump 1 step")

    def jump_2char(self):
        print("jump 2 step")


class Pokemon(Movecharacter,Jumpcharacter):
    def move_bwd(self):
        print("pokemon moving backward")


p = Pokemon()
p.move_bwd()
p.jump_1char()
print(Pokemon.mro())
