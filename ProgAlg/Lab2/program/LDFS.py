from colorama import Fore
from curses.textpad import rectangle
from maze import *
import os


class LDFS:
    def __init__(self):
        self.iterat = 0
        self.state = 1
        self.mem_st = 0
        self.stop = 0

    def search(self, m, x, y, start, end):
        self.iterat = 0
        self.mem_st = 0
        self.stop = 0
        self.state = 0

        limit =  x*y//3
        
        m_copy = m
        dir_map = self.new_map(m)

        priority = ["bottom", "right", "top", "left"]

        path = [start]
        cells = [start]
        movement = [start]
        memory = [start]
        
        while len(movement) > 0:
            self.iterat+=1
            curr = movement.pop()

            if curr == end:
                # print("Yes, we have path!")
                break

            if len(movement) > self.mem_st:
                self.mem_st = len(movement)

            for direction in priority:
                if dir_map[curr][direction]:
                    if direction == "left":
                        nextStep = (curr[0], curr[1] - 1)
                    
                    elif direction == "top":
                        nextStep = (curr[0] - 1, curr[1])

                    elif direction == "right":
                        nextStep = (curr[0], curr[1] + 1)

                    else:
                        nextStep = (curr[0] + 1, curr[1])

                    if nextStep in cells:
                        memory.append(nextStep)
                        continue
                    
                    cells.append(nextStep)
                    movement.append(nextStep)
                    path.append(nextStep)
                    memory.append(nextStep)

                    if len(path) - 1 == limit:
                        self.stop+=1

                    if self.iterat > 1 and m_copy[curr[0]][curr[1]] != 's':
                        m_copy[curr[0]][curr[1]] = 'P'
                    
            
        # виводимо шлях в консоль

        self.state += printPath(path)
        self.mem_st += len(movement)

        
        printMaze(m_copy, x, y)

    def new_map(self, m):
        dir_map = {}

        for i in range(len(m)):
            for j in range(len(m[i])):
                x = i
                y = j
                curr = (x, y)
                dir_map[curr] = {"left": self.is_dir(m, i, j-1),
                                 "top": self.is_dir(m, i-1, j),
                                 "right": self.is_dir(m, i, j+1),
                                 "bottom": self.is_dir(m, i+1, j)}


        return dir_map
 
    def is_dir(self, m, x, y):
        if x>=len(m) or x<0 or y>=len(m[x]) or y<0:
            return False
        return True if m[x][y] == "c" or m[x][y] == "E" else False
