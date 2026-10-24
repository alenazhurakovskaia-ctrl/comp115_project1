from turtle import *
from random import randint
 
def draw_background_day():
   """Draw the daytime sky (blue background)"""
   screen = getscreen()
   screen.bgcolor("light blue")
   
 
def draw_background_night():
   """Draw the night sky (dark gray background)"""
   screen = getscreen()
   screen.bgcolor("dark gray")
 

def draw_sun(): #Sun
   penup()
   goto(-200, 150)
   pendown()
   begin_fill()
   color('orange', 'yellow')
   for i in range(18):
       forward(40)
       left(100)
   end_fill()
 
def draw_moon():
   """Draw moon"""
   penup()
   goto(-200, 150)
   pendown()
   color("light gray")
   begin_fill()
   circle(25)
   end_fill()
 
def draw_stars():
   """Draw stars at the night sky"""
   color("white")
   for _ in range(30):
       penup()
       goto(randint(-400, 300), randint(100, 300))
       pendown()
       dot(randint(2, 5))
 

def draw_cloud(x, y, size=30):
   """
   Draw clouds
   x, y - coordinates of the cloud center
   size - size pf the cloud
   """
   
   speed(0)
   penup()
   goto(x, y)
   pendown()
   
   fillcolor("white")
   begin_fill()
   
   # Draw several overlapping circles to create a cloud shape.
   for offset in [0, size/3, -size/3, size/4, -size/4]:
       penup()
       goto(x + offset, y)
       pendown()
       circle(size/2)
   
   end_fill()
   hideturtle()
 

def draw_grass():
   """draw green grass"""
   penup()
   goto(-400, -100)
   pendown()
   color("green")
   begin_fill()
   for _ in range(2):
       forward(800)
       right(90)
       forward(300)
       right(90)
   end_fill()
 
def draw_bird(x, y):
   """Draw a bird as < at position (x, y)"""
   penup()
   goto(x, y)
   pendown()
   color("black")
   setheading(0)  #sets the turtle's direction to 0 degrees.
   left(45)
   forward(15)
   backward(15)
   right(90)
   forward(15)
 
def draw_tree(x, y):
   penup()
   goto(x, y)
   pendown()
   color("brown")
   begin_fill()
   setheading(0)
   for _ in range(2):
       forward(10)
       left(90)
       forward(20)
       left(90)
   end_fill()
   
   #Crown
   penup()
   goto(x + 5, y + 20)
   pendown()
   color("dark green")
   begin_fill()
   circle(20)
   end_fill()
 
def draw_building(x, y, width, height, floors):
   """Draw a main building"""
   #Main building 
   penup()
   goto(x, y)
   pendown()
   color("gray")
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   for _ in range(2):
       forward(width)
       left(90)
       forward(height * floors)
       left(90)
   end_fill()
   
   #Windows
   window_width = width // 5
   window_height = height // 3
   color("yellow")
   for floor in range(floors):
       for window in range(3):
           penup()
           goto(x + 10 + window * (window_width + 10), y + 10 + floor * height)
           pendown()
           begin_fill()
           setheading(0)  #sets the turtle's direction to 0 degrees.
           for _ in range(2):
               forward(window_width)
               left(90)
               forward(window_height)
               left(90)
           end_fill()
 
def draw_school():
   """draw a one-story school"""
   penup()
   goto(100, -100)
   pendown()
   color("pink")
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   for _ in range(2):
       forward(60)
       left(90)
       forward(80)
       left(90)
   end_fill()
   
   #The sign "School"
   penup()
   goto(110, -70)
   pendown()
   color("black")
   write("School", font=("Arial", 10, "normal"))
   #School roof
   penup()
   goto(100, -20)
   pendown()
   color("brown")
   begin_fill()
   goto(130, 20)
   goto(160, -20)
   goto(100, -20)
   end_fill()
 
def draw_pharmacy():
   """Draw a pharmacy with a red cross"""
   penup()
   goto(250, -100)
   pendown()
   color("white")
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   for _ in range(2):
       forward(60)
       left(90)
       forward(60)
       left(90)
   end_fill()
   
   #Red cross
   penup()
   goto(260, -70)
   pendown()
   color("red")
   pensize(5)
   setheading(0)
   forward(40)
   backward(20)
   left(90)
   forward(20)
   backward(40)
   pensize(1)
 
def draw_shop():
   """Draw a store with a roof and a sign"""
   #Building
   penup()
   goto(-50, -100)
   pendown()
   color("light yellow")
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   for _ in range(2):
       forward(60)
       left(90)
       forward(60)
       left(90)
   end_fill()
   
   # Roof
   penup()
   goto(10, -40)
   pendown()
   color("brown")
   begin_fill()
   goto(-20, 0)
   goto(-50, -40)
   goto(10, -40)
   end_fill()
   
   #Signboard
   penup()
   goto(-47, -50)
   pendown()
   color("black")
   write("Shop", font=("Arial", 10, "normal"))
 
def draw_road():
   """Draw a two-lane road"""
   #Asphalt
   penup()
   goto(-400, -150)
   pendown()
   color("black")
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   goto(400, -150)
   goto(400, -200)
   goto(-400, -200)
   goto(-400, -150)
   end_fill()
   
   #Markup
   color("yellow")
   penup()
   goto(-400, -170)
   pendown()
   setheading(0)
   for _ in range(8):
       forward(50)
       penup()
       forward(50)
       pendown()
 
def draw_car(x, y):
   """Draw a car in position(x, y)"""
   #Body
   penup()
   goto(x, y)
   pendown()
   color("red")
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   for _ in range(2):
       forward(60)
       left(90)
       forward(20)
       left(90)
   end_fill() 
   
   #Roof
   penup()
   goto(x + 10, y + 20)
   pendown()
   begin_fill()
   setheading(0)  #sets the turtle's direction to 0 degrees.
   for _ in range(2):
       forward(40)
       left(90)
       forward(10)
       left(90)
   end_fill()
   
   #Wheels
   for wheel in [10, 50]:
       penup()
       goto(x + wheel, y - 10)
       pendown()
       color("grey")
       begin_fill()
       circle(5)
       end_fill()
    
#Ask the user for the time of day
 
speed(0)
while True:
   time_of_day = input("Is it day or night now? (day/night/and press «Enter»): ").lower()
   if time_of_day in ['day', 'night']:
       break
   print("Please enter 'day' or 'night' and press «Enter»")  
 
# Reset turtle orientation at the start
setheading(0)
 
#Adjust the scene depending on the time of day
if time_of_day == "day":
   draw_background_day()
   draw_sun()
else:
   draw_background_night()
   draw_moon()
   draw_stars()
 
if time_of_day == "day":
   for _ in range(5):
       x = randint(-350, 350)
       y = randint(100, 250)
       size = randint(10, 40)
       draw_cloud(x, y, size)
 
#Draw common elements of the urban environment
draw_grass()
 
#Draw birds (daytime only)
if time_of_day == "day":
   for _ in range(5):
         draw_bird(randint(-300, 300), randint(50, 200))
 
#Draw trees
for x in [-350, -150, 50, 200, 350]:
   draw_tree(x, -100)
 
#Draw buildings
draw_building(-300, -100, 80, 80, 3)  #High-rise building
draw_school()  #School
draw_pharmacy()  #Pharmacy
draw_shop()  #Shop
 
#Draw road and car
draw_road()
draw_car(-200, -165)
 
#Finish work
hideturtle()
exitonclick()
 
 
