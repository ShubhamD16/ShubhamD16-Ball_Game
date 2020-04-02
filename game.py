
import numpy as np
from tkinter import *
import keyboard


def randdim():              # for giving random value of height and width
    x = int(np.random.randint(5, 10, 1))
    y = int(np.random.randint(25, 50, 1))
    return x, y


l1 = [0, randdim()]         # obstacle 1 [x coordinate,(dimensions)]
l2 = [200, randdim()]       # obstacle 2 [x coordinate,(dimensions)]
l3 = [400, randdim()]       # obstacle 3 [x coordinate,(dimensions)]
l4 = [600, randdim()]       # obstacle 4 [x coordinate,(dimensions)]
l5 = [800, randdim()]       # obstacle 5 [x coordinate,(dimensions)]
c = [200, (20, 20)]         # ball       [y coordinate,(dimensions)]
u = 0                       # boolean for upward jump
d = 0                       # boolean for downward jump
jump = 0                    # boolean for jump
point = 0                   # points
end = 0                     # for game over
    

def reset():                # for resetting values for new game (not used)
    global l1
    global l2
    global l3
    global l4
    global l5
    global c
    global u
    global d
    global jump
    global point

    jump = 0
    u = 0
    d = 0
    point = 0
    end = 0

    l1 = [0, randdim()]
    l2 = [200, randdim()]
    l3 = [400, randdim()]
    l4 = [600, randdim()]
    l5 = [800, randdim()]
    c = [200, (20, 20)]


def rect(l, canvas):        # for creating rectangular walls
    n = l[0]
    dim = l[1]
    y = 200
    canvas.create_rectangle(n, y, n + dim[0], y - dim[1], fill="#476042")


def circle(c, canvas):      #for creation of Ball
    n = 50
    dim = c[1]
    y = c[0]
    canvas.create_oval(n, y - dim[1], n + dim[0], y, fill="yellow")


def destroy():
    w.destroy()
    display()


def endfunct(w):            # for end Display
    w.create_text(350, 100, text='Game Over')


def touch(c):               #if ball touch the wall
    global l1
    global l2
    global l3
    global l4
    global l5
    global end

    if l1[0] < 75 and l1[0] > 25:
        for i in range(l1[1][1]):
            check = np.add(np.square(60 - l1[0]), np.square(c[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break
    if l2[0] < 75 and l2[0] > 25:
        for i in range(l2[1][1]):
            check = np.add(np.square(60 - l2[0]), np.square(c[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break

    if l3[0] < 75 and l3[0] > 25:
        for i in range(l3[1][1]):
            check = np.add(np.square(60 - l3[0]), np.square(c[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break

    if l4[0] < 75 and l4[0] > 25:
        for i in range(l4[1][1]):
            check = np.add(np.square(60 - l4[0]), np.square(c[0] - 210 + i))
            if check <= np.square(10):
                end = 1
                break

    if l5[0] < 75 and l5[0] > 25:
        for i in range(l5[1][1]):
            check = np.add(np.square(60 - l5[0]), np.square(c[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break


def logic():                # for placement of object
    global l1
    global l2
    global l3
    global l4
    global l5
    global c
    global u
    global d
    global jump
    global point

    if l1[0] <= 0:
        n = np.random.randint(50, 100)
        l1 = [950 + n, randdim()]
    else:
        l1[0] -= 1

    if l2[0] <= 0:
        n = np.random.randint(30, 70)
        l2 = [950 + n, randdim()]
    else:
        l2[0] -= 1

    if l3[0] <= 0:
        n = np.random.randint(30, 70)
        l3 = [950 + n, randdim()]
    else:
        l3[0] -= 1

    if l4[0] <= 0:
        n = np.random.randint(30, 70)
        l4 = [950 + n, randdim()]
    else:
        l4[0] -= 1

    if l5[0] <= 0:
        n = np.random.randint(30, 70)
        l5 = [950 + n, randdim()]
    else:
        l5[0] -= 1

    if keyboard.is_pressed(' '):            # for getting value from keyboard
        jump = 1
        if c[0] == 200:
            u = 0
            d = 0

    if jump == 1:           # for one complet jump

        if u < 80:          #upward movement
            c[0] = c[0] - 1
            u += 1

        if u == 80 and d < 80:      # downward movement
            c[0] = c[0] + 1
            d += 1

        if u == 80 and d == 80:     #check weather ball touch the ground
            jump = False

    if l1[0] == 50 or l2[0] == 50 or l3[0] == 50 or l4[0] == 50 or l5[0] == 50:     # calculate points
        point += 1

    touch(c)




def display():              # for display of game window
    global w
    global l1
    global l2
    global l3
    global l4
    global l5
    global c
    global point
    canvas_width = 700
    canvas_height = 400
    w.delete("all")
    w.create_line(0, 200, canvas_width, 200, fill="#400000")
    rect(l1, w)
    rect(l2, w)
    rect(l3, w)
    rect(l4, w)
    rect(l5, w)
    circle(c, w)
    w.create_text(40, 40, text=f'points ==> {point}')
    logic()
    print(point)

    if end == 0:
        w.after(30, display)
    elif end == 1:
        endfunct(w)


def game():                 # main game function
    global w
    master = Tk()

    canvas_width = 700
    canvas_height = 400
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    display()
    w.after(100, display)
    w.pack()
    mainloop()


game()

