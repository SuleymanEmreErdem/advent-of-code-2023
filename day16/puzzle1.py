import time

file = [list(row) for row in open('input.txt', 'r').read().split('\n')]
beams = []
energized = set()

class Beam:
    def __init__(self, position, direction):
        if position[0] < 0 or position[0] >= len(file) or position[1] < 0 or position[1] >= len(file[0]):
            pass
        else:
            if file[position[0]][position[1]] in ('#', '.'):
                file[position[0]][position[1]] = '#'
        self.position = position
        if direction == 'N':
            self.direction = (-1, 0)
        elif direction == 'S':
            self.direction = (1, 0)
        elif direction == 'W':
            self.direction = (0, -1)
        elif direction == 'E':
            self.direction = (0, 1)

    def next_step(self):
        next_pos = (self.position[0], self.position[1])
        if next_pos[0] < 0 or next_pos[0] >= len(file) or next_pos[1] < 0 or next_pos[1] >= len(file[0]):
            return 1
        next_cell = file[next_pos[0]][next_pos[1]]
        if next_cell in ('.', '#'):
            file[next_pos[0]][next_pos[1]] = '#'
            self.position = (next_pos[0]+self.direction[0], next_pos[1]+self.direction[1])
            return 0
        elif next_cell == '|':
            energized.add(next_pos)
            if self.direction in ((0, -1), (0, 1)):
                beams.append(Beam((next_pos[0]-1, next_pos[1]), 'N'))
                beams.append(Beam((next_pos[0]+1, next_pos[1]), 'S'))
                return 1
            else:
                beams.append(Beam((next_pos[0]+self.direction[0], next_pos[1]), 'N' if self.direction == (-1, 0) else 'S'))
                return 1
        elif next_cell == '-':
            energized.add(next_pos)
            if self.direction in ((1, 0), (-1, 0)):
                beams.append(Beam((next_pos[0], next_pos[1]-1), 'W'))
                beams.append(Beam((next_pos[0], next_pos[1]+1), 'E'))
                return 1
            else:
                beams.append(Beam((next_pos[0], next_pos[1]+self.direction[1]), 'W' if self.direction == (0, -1) else 'E'))
                return 1
        elif next_cell == '\\':
            energized.add(next_pos)
            if self.direction == (-1, 0):
                beams.append(Beam((next_pos[0], next_pos[1]-1), 'W'))
            elif self.direction == (1, 0):
                beams.append(Beam((next_pos[0], next_pos[1]+1), 'E'))
            elif self.direction == (0, -1):
                beams.append(Beam((next_pos[0]-1, next_pos[1]), 'N'))
            elif self.direction == (0, 1):
                beams.append(Beam((next_pos[0]+1, next_pos[1]), 'S'))
            return 1
        elif next_cell == '/':
            energized.add(next_pos)
            if self.direction == (-1, 0):
                beams.append(Beam((next_pos[0], next_pos[1]+1), 'E'))
            elif self.direction == (1, 0):
                beams.append(Beam((next_pos[0], next_pos[1]-1), 'W'))
            elif self.direction == (0, -1):
                beams.append(Beam((next_pos[0]+1, next_pos[1]), 'S'))
            elif self.direction == (0, 1):
                beams.append(Beam((next_pos[0]-1, next_pos[1]), 'N'))
            return 1

        
beams.append(Beam((0, 0), ('E')))

if __name__=='__main__':
    start = time.time()
    dur = 1800
    while True:
        for j in beams.copy():
            d = j.next_step()
            if d:
                beams.remove(j)
        res = 0
        for i in file:
            res += i.count('#')
        print(len(energized) + res)
        if len(energized) + res == 7434:
            break
    end = time.time()
    print(end - start)
    