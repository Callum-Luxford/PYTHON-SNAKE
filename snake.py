from turtle import Turtle

STARTING_POSTIONS = [(0,0),(-20,0),(-40,0)] # <- Starting Snake Coordinates.
MOVE_DISTANCE = 20 # <- Constant for move distance.

# Headings as Constants:
UP = 90 
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake: # <- Defining the Class for the Snake. 

    def __init__(self): # <- Init function.
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        
    def create_snake(self): # <- Creating the snake with it's,
                            #    shape, color and starting postions.
        """Creates the instanc of the Snake."""
        for position in STARTING_POSTIONS:
            self.add_square(position)

    def add_square(self,position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)
    
    def extend(self):
        """Add new square to the snake."""
        self.add_square(self.squares[-1].position())
        
    def move(self): # <- Snake 'move' function.
        """Allows the Snake to move."""
        # (for) loop, to loop through each item in the range of the,
        # length of the 'squares' list which is the snake itself,
        # -1 because the 'range' function does not include the last item,
        # which in-turn sets the start to 0, the end to also 0, and,
        # decrement each time by (-1).
        # Then set the new coordinates for each item:
        # For both X and Y we (-1) at the position to give us the second
        # to last position and then move those items to the new X and Y.
        # In short a backward loop, moving the items at the rear
        # to the item in the next forward position.
        for i in range(len(self.squares)-1, 0, -1,):
                new_x = self.squares[i-1].xcor()
                new_y = self.squares[i-1].ycor()
                self.squares[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def reset(self):
        for i in self.squares:
            i.goto(1000,1000) 
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]
        
    # The following functions are to determine the direction the snake can
    # move in and sets current rules for snake movement.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 