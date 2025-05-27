import turtle
from turtle import Turtle, Screen
import random
number_of_turtles = 0
all_turts = []
class EtchASketch:
    def __init__(self,name,color):
        global number_of_turtles
        self.t=Turtle()
        number_of_turtles += 1
        self.t.teleport(-turtle.window_width()/2, 100 - (number_of_turtles * 20))
        self.t.color(color)
        self.t.shape("turtle")
        self.t.speed(0)
        self.name=name
        all_turts.append(self)
    def w_pressed(self,steps):
        self.t.setheading(90)
        self.t.forward(steps)
    def d_pressed(self,steps):
        self.t.setheading(0)
        self.t.forward(steps)
    def a_pressed(self,steps):
        self.t.setheading(180)
        self.t.forward(steps)
    def s_pressed(self,steps):
        self.t.setheading(270)
        self.t.forward(steps)
    def clear_screen(self):
        self.t.clear()
        self.t.penup()
        self.t.home()
        self.t.pendown()

e1=EtchASketch("Timmy","Red")
e2=EtchASketch("Tommy","Blue")
e3=EtchASketch("Tina","Green")
e4=EtchASketch("Terry","Yellow")

choice_made=False

screen=Screen()
screen.setup(width=800, height=600)
screen.title("Turt Race")
userbet=screen.textinput("Who wins", "Enter your bet color: ")
choice_made=True

while(choice_made):
    if(e1.t.xcor() >= turtle.window_width()/2 or
       e2.t.xcor() >= turtle.window_width()/2 or
       e3.t.xcor() >= turtle.window_width()/2 or
       e4.t.xcor() >= turtle.window_width()/2):
        choice_made=False

        maxi= max(e1.t.xcor(), e2.t.xcor(), e3.t.xcor(), e4.t.xcor())
        if maxi == e1.t.xcor():
            if userbet == "Red":
                print("You win!")
            else:
                print("You lose!")
            print("Timmy is the winner!")
        elif maxi == e2.t.xcor():
            if userbet == "Blue":
                print("You win!")
            else:
                print("You lose!")
            print("Tommy is the winner!")
        elif maxi == e3.t.xcor():
                if userbet == "Green":
                    print("You win!")
                else:
                    print("You lose!")                   
                print("Tina is the winner!")
        elif maxi == e4.t.xcor():
            if userbet == "Yellow":
                print("You win!")
            else:
                print("You lose!")
            print("Terry is the winner!")
        break

    current=random.choice(all_turts)
    if current.name == "Timmy":
        e1.d_pressed(random.randint(1,10))
    elif current.name == "Tommy":
        e2.d_pressed(random.randint(1,10))
    elif current.name == "Tina":
        e3.d_pressed(random.randint(1,10))
    elif current.name == "Terry":
        e4.d_pressed(random.randint(1,10))




screen.exitonclick()