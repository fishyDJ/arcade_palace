# 8/3/2023 
from tkinter import *
from PIL import Image, ImageTk
import time

class Game():
  def __init__(self, grid):
    self.root = Tk() #  creates window
    self.root.title("Connect 4")
    self.root.geometry("1022x875") # window size

    self.clicked = 0

    self.grid = grid.copy() #  stores grid positions 
    self.squares = [] #  stores squares 

    self.turn = False #  turn // True = AI's turn
    self.directions = [(0, 1, 4, 6), (-1, 1, 4, 6), (1, 0, 7, 4), (1, 1, 4, 6)] # column, row, max right, max up 

    #images
    self.load = Image.open(R'Games\Connect 4\Assets\blanktile.png')
    self.blank_square = ImageTk.PhotoImage(self.load)
    self.load = Image.open(R'Games\Connect 4\Assets\bluetile.png')
    self.blue_square = ImageTk.PhotoImage(self.load)
    self.load = Image.open(R'Games\Connect 4\Assets\purpletile.png')
    self.purple_square = ImageTk.PhotoImage(self.load)

    self.column = 0 #  Puts squares on window
    self.row = -1
    self.smallsquares = []
    for i in range(42): 
      self.row += 1
      if i % 6 == 0 and i !=0: #  Sets grid width 
        self.column += 1
        self.row = 0
        self.squares.append(self.smallsquares)
        self.smallsquares = []
      self.square = Button(self.root, image= self.blank_square, command= lambda t= (self.column, self.row): self.button_press(t)) #  square appearance command= lambda t= (self.column, self.row): self.button_press(t) 
      self.square.grid(column= self.column, row= self.row)
      self.smallsquares.append(self.square)
    self.squares.append(self.smallsquares)
    #self.starter = Button(self.root, command= self.click())
    #self.starter.place(x=50, y=50)

  def button_press(self, location): # button press 
    if not self.turn:
      verticle_position = None
      for i in range(5, -1, -1,): #  checks row to pick what height to place the piece 
        if self.grid[location[0]][i] == None:
          verticle_position = i
          break
      if verticle_position != None: 
        self.squares[location[0]][verticle_position].configure(image= self.blue_square)  #  piece color 
        self.grid[location[0]][verticle_position] = self.turn
        if self.win_check(self.grid, False):
          time.sleep(3)
          self.root.destroy()
        self.root.update()
        self.turn = True
        self.ai()
  '''
  def click(self):
    #self.starter.destroy()
    self.root.update()
    self.ai()
  '''
  def ai(self):
    verticle_position = None
    if self.turn:
      aiColumn = self.minimax(self.grid, self.turn, 0, 5) 
    else: 
      aiColumn = self.minimax(self.grid, self.turn, 0, 2) 

    for i in range(5, -1, -1,): #  checks row to pick what height to place the piece 
      if self.grid[aiColumn][i] == None:
        verticle_position = i
        break
    if self.turn:
      self.squares[aiColumn][verticle_position].configure(image= self.purple_square) #  piece color 
    else:
      self.squares[aiColumn][verticle_position].configure(image= self.blue_square)
    self.grid[aiColumn][verticle_position] = self.turn
    if self.win_check(self.grid, True):
      self.root.update()
      time.sleep(3)
      self.root.destroy()

    if self.turn:
      self.turn = False
    else:
      self.turn = True
    self.root.update()
    if self.win_check(self.grid, False):
      self.root.update()
      time.sleep(3)
      self.root.destroy()
    #self.ai()

  def win_check(self, grid, turnn):
    for direction in range(len(self.directions)):  # direction 
      for startingRow in range(self.directions[direction][3]):  # starting row
        for startingColumn in range(self.directions[direction][2]):  # starting column 
          for columnr in range(4):  # iteration after starting 
            row = startingRow + columnr * self.directions[direction][0]
            column = startingColumn + columnr * self.directions[direction][1]
            if row == 6:
              break
            if grid[column][row] != turnn:
              break
            elif columnr == 3: 
              return(True)
    
  def minimax(self, griiid, Maximizing, depth, turnsAhead):  # minmax ai
    scores = []
    rrow = []
    griid = []
    tie = 0

    for col in range(7):
      rrow = []
      for row in range(6):
        rrow.append(griiid[col][row])
        if row == 5:
          griid.append(rrow)

    if Maximizing: # scores 
      if self.win_check(griid, True):  
        scores.append(100 - depth)

    else:
      if self.win_check(griid, False):
        scores.append(-100 + depth)
         
    for column in range(7):
      for i in range(5, -1, -1,): #  checks row to pick what height to place the piece 
        if griid[column][i] == None:
          if Maximizing:
            if depth > turnsAhead:
              return(0)
            newgrid = griid.copy()
            newgrid[column][i] = True
            scores.append(self.minimax(newgrid, False, depth+1, turnsAhead))
            break
          elif not Maximizing:
            if depth > turnsAhead:
              return(0)
            newgrid = griid.copy()
            newgrid[column][i] = False
            scores.append(self.minimax(newgrid, True, depth+1, turnsAhead))
            break
        else:
          tie += 1
 
    for i in range(len(scores)):
      if scores[i] is None:
        scores[i] = 0

    if tie == 42:
      scores.append(-depth)

    elif Maximizing and depth > 0: # scores 
      return(max(scores))
    elif not Maximizing and depth > 0:
      return(min(scores))
    elif depth == 0:
      if sum(scores) != 0:
        if Maximizing:
          return(scores.index(max(scores)))
        if not Maximizing:
          return(scores.index(min(scores)))
      else:
        for location in range(7):
          for i in range(5, -1, -1,): #  checks row to pick what height to place the piece 
            if self.grid[location[0]][i] is None:
              return(location)

#  Main
grid = [
  [None,None,None,None,None,None],[None,None,None,None,None,None],[None,None,None,None,None,None],[None,None,None,None,None,None],
  [None,None,None,None,None,None],[None,None,None,None,None,None],[None,None,None,None,None,None]
  ] #  columns left to right, first number is top. 
  
game = Game(grid)

game.root.mainloop()
