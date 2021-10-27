import turtle

drawer = turtle .Turtle()

screen = turtle.Screen()


drawer.speed(0)
turtle.speed(0)

#set pensize and color/setup calculator window

drawer.pencolor("dark green")

drawer.pensize(3)

screen.setup(width=400, height=400)



#draw the axis

drawer.forward(200)

drawer.backward(400)

drawer.penup()

drawer.setposition(0, 200)

drawer.pendown()

drawer.setposition(0, -200)



#set position for hash marks

drawer.penup()

drawer.setposition(-200, 0)

drawer.pendown()



#def hash mark function

def draw_hash_marks():

    for i in range(40):

        drawer.left(90)

        drawer.forward(4)

        drawer.backward(8)

        drawer.forward(4)

        drawer.right(90)

        drawer.forward(10)



#make hash marks using function created

draw_hash_marks()

drawer.left(90)

drawer.forward(4)

drawer.backward(8)

drawer.right(90)

drawer.penup()

drawer.setposition(0, 200)

drawer.pendown()

drawer.right(90)

draw_hash_marks()



#set starting position

drawer.setposition(0, 0)



#def function for calculator boundaries 

def tracing():

    painter = turtle.Turtle()

    painter.speed(0)

    painter.penup()

    painter.setposition(-200, 200)

    painter.color("blue")

    painter.pensize(3)

    painter.pendown()

    for i in range(4):

        painter.forward(400)

        painter.right(90)

        print("boundaries: ", painter.pos())

    painter.pensize(1)



#def function for user input

def user_input():

  user_input = input("Enter a slope intercept form: ")

  print(user_input)

  return user_input



#def function that makes sure values are correct

def input_correction(first_equation):

  equationInput = first_equation

  correction_slope = False

  correction_y = False

  while correction_slope == False or correction_y == False:

    slope, y_intercept = format_variables(equationInput)

    if slope > 50:

      equationInput = input("oops, your slope is too big for our program! please input your whole function again. (same format)\n")

      slope, y_intercept = format_variables(equationInput)

    else:

      correction_slope = True

    if y_intercept > 200:

      equationInput = input("oops, your y-intercept is too big for our program! please input your whole function again. (same format)\n")

    else:

      correction_y = True

  return slope, y_intercept

def draw_line(slope, y_intercept):

  last_y = ((-200/slope)*slope)

  drawer.penup()

  drawer.setposition(-200/slope, last_y)

  print(drawer.pos())



  drawer.pendown()

  makearrow() 

  drawer.setposition(0, y_intercept)

  print(drawer.pos())

  #print(last_y)



  drawer.pendown()

  last_y = (((200)/slope)*slope)

  #print(last_y)

  drawer.setposition((200-y_intercept) /slope, last_y)

  print(drawer.pos())



#arrow function

def makearrow():

  drawer.right(50)

  drawer.pendown()

  drawer.fillcolor("red")

  drawer.begin_fill()

  drawer.forward(5) # draw base

  drawer.left(180)

  drawer.forward(10)

  drawer.left(120)

  drawer.forward(10)

  drawer.left(120)

  drawer.forward(10)



  drawer.pencolor("green")

  drawer.end_fill()



#split equation into values

def format_variables(equation):

  split1 = equation.split(" ")

  print(split1)

  slope = int((split1[2]).split("x")[0])

  y_intercept = int(split1[4])

  print(slope)

  print(y_intercept)

  return slope, y_intercept



#call functions to create calculator and line 

tracing()



equation = user_input()

slope, y_intercept = input_correction(equation)



drawer.pensize(1)

draw_line(slope, y_intercept)



screen.mainloop()
