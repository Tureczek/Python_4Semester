class Bird:

    def __init__(self, start, dir):
        """ Arg: a list of 2 points , a position of the nose """
        # position , a list of [x,y] points
        self.pos = start
        # left : 3; right : 1; up : 4 down : 2 
        self.dir = dir

        # list of all methods 
        self.methods = {'f': self.move_forward, 'l': self.turn_left, 'r': self.turn_right}

    def move_forward(self):
        if self.dir == 1:
            self.pos[1] = self.pos[1] + 1
        elif self.dir == 2:
            self.pos[0] = self.pos[0] + 1
        elif self.dir == 3:
            self.pos[1] = self.pos[1] - 1
        else:
            self.pos[0] = self.pos[0] - 1

    def turn_left(self):
        if self.dir == 1:
            self.dir = 4
        else:
            self.dir -= 1

    def turn_right(self):
        if self.dir == 4:
            self.dir = 1
        else:
            self.dir += 1

    def loose(self):
        return 'The bird lost the game!'

    def __repr__(self):
        return f'{self.__dict__}'


class Pig:
    def __init__(self, pos):
        self.pos = pos
        self.is_alive = True

    def die(self):
        return 'Uff the pig is dead'


class Board:

    def __init__(self):
        # create a bird at some postion
        self.bird = Bird([2, 2], 1)
        self.c = Bird.__dict__
        # create a pig at some position
        self.pig = Pig([2, 5])

    def run(self, cmd):
        for i in cmd:
            self.bird.methods[i]()

    def display(self):
        for i in range(1, 10):
            for j in range(1, 10):
                if (i, j) == tuple(self.bird.pos):
                    print('B', end=' ')
                elif (i, j) == tuple(self.pig.pos):
                    print('P', end=' ')
                else:
                    print('*', end=' ')
            print()


class Workspace:
    def __init__(self):
        self.moves = None

    def display(self):
        print('\nwhat steps do you want to perform?')
        print('Options: move forward (f), turn left (l), turn right (r)')
        print('Type "q" when finnished')

    def commands(self):
        l = []
        q = True
        while q:
            x = input('Move: ')
            if x == 'q':
                q = False
            else:
                l.append(x)

        return l


class Game:

    def main(self):
        b = Board()
        b.display()

        w = Workspace()
        w.display()

        l = w.commands()
        b.run(l)

        print(self.win(b))
        print(f'Birds position: {b.bird.pos}')
        print(f'Pigs position: {b.pig.pos}')

    def win(self, b):
        if b.bird.pos == b.pig.pos:
            return b.pig.die()
        else:
            return b.bird.loose()


g = Game()
g.main()