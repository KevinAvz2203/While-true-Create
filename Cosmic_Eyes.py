import turtle
from turtle import *
import math
import random
import time
import winsound
from tkinter import CENTER
from random import *

# defines the width and height of the window
WIDTH, HEIGHT = 600, 600

# Global bools
is_nir_Spec = False
is_nir_Cam = False
is_nir_ISS = False
is_miri = False

# Two counter variables are created, one variable to count the number of taps and 
# the other one to count the image pairs.

totalTaps = 0
totalPairs = 0

# Declares background, number of tiles
# Creates the state of the tile
# Hide tiles
pic = 'pic.gif'
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

def finalScene():
    final = turtle.Screen() # Create the screen and assign its characteristics
    final.clearscreen()
    final.clear()
    final.setup(WIDTH, HEIGHT)
    final.bgcolor("black")
    final.title("COSMIC EYE") 
    final.bgpic("endjimmy.gif")
    final.update()
    time.sleep(2) # Set the background pic to use as a template 

    sy = "See you next time !!"

    a = -100
    b = -200 # Assign the x and y values to the paragraphs
    for frase in sy: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        for letter in sy: # Creates a loop that takes every letter in the words
            score_pen.write(letter, False, align="left", font=("Helvetica", 13, "normal"))
            score_pen.hideturtle()
            score_pen.fd(10) # Writes the sentences letter by letter

    time.sleep(2)

# Heading function: creates the heading text of the window
def head():
    uppertext = turtle.Turtle()
    uppertext.hideturtle()
    uppertext.penup()
    uppertext.setpos(-140, 260)
    uppertext.pendown()
    uppertext.pencolor("black")
    texto1 = "Help me solve the memory game"
    texto2 = " to uncover the past!"
    uppertext.penup()

    
    for letter1 in texto1:
        uppertext.write(letter1, align="center", font=("Pixelmix", 12, "bold"))
        uppertext.fd(10)
    uppertext.setpos(-100, 240)
    for letter2 in texto2:
        uppertext.write(letter2, align="center", font=("Pixelmix", 12, "bold"))
        uppertext.fd(10)

# Square function: draws purple squares with golden outline at (x, y)
def square(x, y):
    up()
    goto(x, y)
    down()
    color('#D4AF37', '#7945EF')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Index function: converts (x, y) coordinates to tiles index
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# XY function: converts tiles count to (x, y) coordinates
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Tap function: updates mark and hidden tiles based on tap
def tap(x, y):
    global totalTaps
    global totalPairs

    totalTaps += 1
    print("Total taps: ", totalTaps)

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]: # the state of the tile equals the spot
        state['mark'] = spot

    else: # adds 1 to the total pairs if a pair is found
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        totalPairs += 1

        # When all pairs are found, a message is displayed in the terminal
        if totalPairs == 1:
            print("We did it! We are now able to see the JWST picture.")
            picFact = turtle.Turtle()
            picFact.hideturtle()
            picFact.penup()
            picFact.setpos(-270, -220)
            picFact.pendown()
            picFact.pencolor("black")
            
            # information of the JWST is displayed at the bottom of the window 
            texto1 = "This picture of the JWST is called 'Stephan's Quintet'"
            texto2 = "because it's a group of five galaxies: NGC 7320, NGC 7317,"
            texto3 = "NGC 7318A, NGC 7318B, and NGC 7319. NGC 7320 is located"
            texto4 = "40 million light-years from Earth and the rest of the"
            texto5 = "galaxies are approximately 290 million light-years away!"
            texto6 = " Pictures like the one we discovered are actually from the past!"
            picFact.penup()
            
            for letter1 in texto1:
                picFact.write(letter1, align="center", font=("Pixelmix", 8, "bold"))
                picFact.fd(10)

            picFact.setpos(-290, -235)
            for letter2 in texto2:
                picFact.write(letter2, align="center", font=("Pixelmix", 8, "bold"))
                picFact.fd(10)

            picFact.setpos(-275, -250)
            for letter3 in texto3:
                picFact.write(letter3, align="center", font=("Pixelmix", 8, "bold"))
                picFact.fd(10)
            
            picFact.setpos(-265, -265)
            for letter4 in texto4:
                picFact.write(letter4, align="center", font=("Pixelmix", 8, "bold"))
                picFact.fd(10)
            
            picFact.setpos(-280, -280)
            for letter5 in texto5:
                picFact.write(letter5, align="center", font=("Pixelmix", 8, "bold"))
                picFact.fd(10)

            picFact.setpos(-315, -295)
            for letter6 in texto6:
                picFact.write(letter6, align="center", font=("Pixelmix", 8, "bold"))
                picFact.fd(10)

            time.sleep(3)
            

# Draw function: draws background image and tiles    
def draw():
    clear()
    goto(0, 0)
    shape(pic)
    stamp()

    for count in range(64): # draws tiles
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]: # draws numbers on tiles
        x, y = xy(mark)
        up()
        goto(x + 27, y+10)
        color('white')
        write(tiles[mark], font=('Pixelmix', 20, 'normal'), align= CENTER)

    update()
    ontimer(draw, 100)

def scene5():
    # calls the functions to start the game
    clearscreen()
    clear()
    shuffle(tiles)
    setup(650, 650, 370, 0)
    head()
    addshape(pic)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done() # when player closes the memory game, the final scene appears
    finalScene()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def scene4_2():
    pantalla2 = turtle.Screen() # Create the screen and assign its characteristics
    pantalla2.clear()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    pantalla2.bgpic("Infrared.gif")
    pantalla2.update()
    time.sleep(2) # Set the background pic to use as a template 

    frase1 = ["Why infrared?"] # Create arrays with every line of the sentences
    frase2 = ["Visible light is made from short, tight ","wavelengths,"]
    frase3 = ["Infrared light is made out of longer ","wavelengths, which past through dust more ",
            "easily."]
    frase4 = ["Consequently, the James Webb Space Telescope ","is able to have a “clear view” of the universe ",
            "of stars and planets “hidden” behind clouds ","of dust."] 

    a = -110
    b = 138 # Assign the x and y values to the paragraphs 

    for frase in frase1: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b) 
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 68 # Assign the x and y values to the paragraphs 
    for frase in frase2: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 20 # Assign the x and y values to the paragraphs 
    for frase in frase3: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase:# Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = -40 # Assign the x and y values to the paragraphs
    for frase in frase4: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

        # writes title and text
        score_pen = turtle.Turtle()
        score_pen.hideturtle()
        score_pen.penup()
        score_pen.setpos(-95, -250)
        score_pen.pendown()
        score_pen.pencolor("white")
        texto= "*Press 'A' to start"
        score_pen.penup()

        
    for letter1 in texto:
        score_pen.write(letter1, align="center", font=("Pixelmix", 10, "bold"))
        score_pen.fd(10)

    time.sleep(2)
    pantalla2.listen()
    pantalla2.onkey(scene5,'a')
    pantalla2.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def scene4_1():
    pantalla2 = turtle.Screen() # Create the screen and assign its characteristics
    pantalla2.clear()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    pantalla2.bgpic("Awesome2.gif") 
    pantalla2.update()
    time.sleep(2) # Set the background pic to use as a template 

    frase1 = ["You assembled the INTEGRATED ","SCIENCE INSTRUMENT MODULE!!"]
    frase2 = ["The ISIM is the heart of the James Webb Space ","Telescope, It contains the four main ",
            "instruments that will detect light from ", "distant stars, galaxies, and planets."]
    frase3 = ["The Webb’s four science instruments will ","receive the light collected by the telescope ",
            "and use its tools (cameras, spectrographs, ","coronagraphs, etc.) designed to maximize the ",
            "knowledge gained from every observation. Each ","instrument also has a field of view that is ",
            "unique in orientation, shape and area."]

    a = -110
    b = 150 # Assign the x and y values to the paragraphs 
    for frase in frase1: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 75
    for frase in frase2:
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16
        for frase in frase:
            for letter in frase:
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10)

    a = -220
    b = -10
    for frase in frase3:
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16
        for frase in frase:
            for letter in frase:
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10)

    time.sleep(2)
# Function to initialize and define the app window
def screen_turtle_s4():
    screen_S4 = turtle.Screen()
    screen_S4.clearscreen()
    screen_S4.clear()
    screen_S4.setup(WIDTH, HEIGHT)
    screen_S4.bgcolor("black")
    screen_S4.title("JWST Puzzle!")
    screen_S4.bgpic("fondo_drop2.gif")
    return screen_S4

# Save .gif files as possible options for Turtle objects
def registerShapes_S4():
    # Parts of the JWST
    pIsim = ["NIRspec.gif", "NIRcam.gif", "NIRISS.gif", "MIRI.gif"]
    for part in pIsim:
        turtle.register_shape(part)

    # Assembled by parts
    pArmedIsim = ["fondo_drop2.gif", "f1_ISIM.gif", "f2_ISIM.gif", "f3_ISIM.gif", "f4_ISIM.gif"]
    for pArmed in pArmedIsim:
        turtle.register_shape(pArmed)

    # Extra images
    imgExtras = ["jimmybee_happy.gif", "jimmybee_talk.gif"]
    for imgEx in imgExtras:
        turtle.register_shape(imgEx)

# Code for scene four
def fourth_scene():
    # Ghost Turtle (helps create dialog boxes and text)
    ghost = turtle.Turtle()
    ghost.clear()
    ghost.hideturtle()

    # Draw the box above
    ghost.penup()
    ghost.setpos(-300, 260)
    ghost.pendown()
    ghost.pencolor("grey")
    ghost.pensize(80)
    ghost.speed(0)
    ghost.forward(600)

# The following functions allow us to drag and drop each element individually --
def nir_Spec_fxn(x, y): 
    nir_Spec.ondrag(None)  
    nir_Spec.setheading(nir_Spec.towards(x, y)) # Rotates and moves forward mouse direction
    nir_Spec.goto(x, y) # Moves the object to the new coords
    nir_Spec.ondrag(nir_Spec_fxn) 

def nir_Cam_fxn(x, y): 
    nir_Cam.ondrag(None)  
    nir_Cam.setheading(nir_Cam.towards(x, y)) 
    nir_Cam.goto(x, y) 
    nir_Cam.ondrag(nir_Cam_fxn)

def nir_ISS_fxn(x, y): 
    nir_ISS.ondrag(None)  
    nir_ISS.setheading(nir_ISS.towards(x, y)) 
    nir_ISS.goto(x, y) 
    nir_ISS.ondrag(nir_ISS_fxn)

def miri_fxn(x, y): 
    miri.ondrag(None)  
    miri.setheading(miri.towards(x, y)) 
    miri.goto(x, y) 
    miri.ondrag(miri_fxn)

# --------------------------------------------------------------------------

# Does the comparison to determine if the object is within the range to be placed
def posi(turtle):
    return (turtle.xcor() >= -300 and turtle.xcor() <= 300) and (turtle.ycor() >= -300 and turtle.ycor() <= 300)

# In each click, the app will check y there is any item inside the area to be placed
def checkPos_S4(x, y):
    global is_nir_Spec
    global is_nir_Cam
    global is_nir_ISS
    global is_miri

    # If an items is in place, the proper part of the ISIM will appear as filled on screen 
    if(posi(nir_Spec)):
        is_nir_Spec = True
        nir_Spec.clear()
        nir_Spec.setpos(300, 300)
        nir_Spec.hideturtle()
        isim_figure.shape("f1_ISIM.gif")
        part_Info(1) # The app will display que info of this part of the telescope and their characteristics by calling the function part_Info

    if(is_nir_Spec and posi(nir_Cam)):
        is_nir_Cam = True
        nir_Cam.clear()
        nir_Cam.setpos(300, 300)
        nir_Cam.hideturtle()
        isim_figure.shape("f2_ISIM.gif")
        part_Info(2)

    if(is_nir_Cam and posi(nir_ISS)):
        is_nir_ISS = True
        nir_ISS.clear()
        nir_ISS.setpos(300, 300)
        nir_ISS.hideturtle()
        isim_figure.shape("f3_ISIM.gif")
        part_Info(3)

    if(is_nir_ISS and posi(miri)):
        isAntenna = True # END
        miri.clear()
        miri.setpos(300, 300)
        miri.hideturtle()
        isim_figure.shape("f4_ISIM.gif")
        part_Info(4)
        scene4_1()
        time.sleep(3)
        scene4_2()
        time.sleep(3)

    # HACER FINAL ------------------

# Creates the objects 
def createObjects_S4():
    # Generate and place the isim_figure in its pos
    isim_figure.shape("fondo_drop2.gif")
    isim_figure.penup()
    isim_figure.setpos(0,0)

    # Generate and place the nir_Spec in its pos
    nir_Spec.shape("NIRspec.gif")
    nir_Spec.left(90)
    nir_Spec.penup()
    nir_Spec.setpos(-WIDTH / 2 + 120, 260)
    nir_Spec.speed(0)

    # Generate and place the nir_Cam in its pos
    nir_Cam.shape("NIRcam.gif")
    nir_Cam.left(90)
    nir_Cam.penup()
    nir_Cam.setpos(-60, 260)
    nir_Cam.speed(0)

    # Generate and place the nir_ISS in its pos
    nir_ISS.shape("NIRISS.gif")
    nir_ISS.left(90)
    nir_ISS.penup()
    nir_ISS.setpos(60, 260)
    nir_ISS.speed(0)
    
    # Generate and place the miri in its pos
    miri.shape("MIRI.gif")
    miri.left(90)
    miri.penup()
    miri.setpos(180, 260)
    miri.speed(0)

    checking = turtle.Turtle()
    checking.clear()
    checking.hideturtle()
    checking.shape('circle')
    checking.fillcolor("blue")
    checking.penup()
    checking.speed(0)
    checking.setpos(-250, -150)
    checking.pencolor("white")
    checking.write("Check", align="center", font=("Pixelmix", 12, "bold"))
    checking.onclick(checkPos_S4)
    checking.showturtle()

def drawMessage_S4(txt):
    # Ghost Turtle (helps create dialog boxes in this case)
    
    # Draw the box at the bottom
    ghost = turtle.Turtle()
    ghost.clear()
    ghost.hideturtle()
    ghost.penup()
    ghost.setpos(-300, -250)
    ghost.pendown()
    ghost.pencolor("black")
    ghost.pensize(80)
    ghost.speed(0)
    ghost.forward(600)

    # We draw the all mighty jimmy Bee
    jimmyBee = turtle.Turtle()
    jimmyBee.clear()
    jimmyBee.hideturtle()
    jimmyBee.penup()
    jimmyBee.setpos(-250, -250)
    jimmyBee.shape("jimmybee_happy.gif")
    jimmyBee.showturtle()

    # Show the Jimmy Bee text
    ghost_INFO = turtle.Turtle()
    ghost_INFO.clear()
    ghost_INFO.hideturtle()
    ghost_INFO.penup()
    ghost_INFO.setpos(-210, -235)
    ghost_INFO.pendown()
    ghost_INFO.pencolor("white")
    ghost_INFO.penup()

    # This FOR loop allows us to write letter by letter
    for letter in txt:
        
        jimmyBee.shape("jimmybee_talk.gif")
        if ghost_INFO.xcor() < 290: # As long as the letters do not reach 290 pixels of the window (right limit)
            ghost_INFO.write(letter, align="left", font=("Pixelmix", 8, "bold"))
            jimmyBee.shape("jimmybee_happy.gif")
            ghost_INFO.fd(10)

        else: # When it reaches it, start writing on the bottom line
            ghost_INFO.setpos(-210, ghost_INFO.ycor() - 18)
            ghost_INFO.write(letter, align="left", font=("Pixelmix", 8, "bold"))
            jimmyBee.shape("jimmybee_happy.gif")
            ghost_INFO.fd(10)

        if letter == '.':
            time.sleep(1)
            ghost_INFO.clear()
            ghost_INFO.setpos(-210, -235)
    time.sleep(3)

def part_Info(num):

    txtNirSpec = "In order to study thousands of galaxies during its 5 to 10 year mission, the NIRSpec is designed to observe 100 objects simultaneously. The NIRSpec will be the first spectrograph in space that has this remarkable multi-object capability. NIRSpec's microshutter cells, each approximately as wide as a human hair, have lids that open and close when a magnetic field is applied. Each cell can be controlled individually, allowing it to be opened or closed to view or block a portion of the sky. A spectrograph (also sometimes called a spectrometer) is used to disperse light from an object into a spectrum. Analyzing the spectrum of an object can tell us about its physical properties, including temperature, mass, and chemical composition."
    txtNirCam = "The Near-Infrared Camera (NIRCam) is equipped with coronagraphs, instruments that allow astronomers to take pictures of very faint objects around a central bright object, like stellar systems. NIRCam's coronagraphs work by blocking a brighter object's light, making it possible to view the dimmer object nearby."
    txtNirISS = "The Fine Guidance Sensor (FGS) allows Webb to point precisely, so that it can obtain high-quality images. The Near Infrared Imager and Slitless Spectrograph part of the FGS/NIRISS will be used to investigate the following science objectives: first light detection, exoplanet detection and characterization, and exoplanet transit spectroscopy. While Hubble views the universe in visible and ultraviolet light, Webb focuses on infrared, a wavelength important for peering through gas and dust to see distant objects. After Spitzer blazed trails in the infrared, Webb will take us farther by virtue of a primary mirror that is nearly 60 times larger in area. Finally, Webb's mirror gives us Hubble's incredible resolution with even greater sensitivity, and it is fully adjustable in space."
    txtMiri = "The Mid-Infrared Instrument (MIRI) has both a camera and a spectrograph that sees light in the mid-infrared region of the electromagnetic spectrum, with wavelengths that are longer than our eyes see. MIRI covers the wavelength range of 5 to 28 microns. Its sensitive detectors will allow it to see the redshifted light of distant galaxies, forming stars, and faintly visible comets. The spectrograph will enable medium-resolution spectroscopy, providing new physical details of the distant objects it will observe."

    if num == 1:
        drawMessage_S4(txtNirSpec)

    elif num == 2:
        drawMessage_S4(txtNirCam)

    elif num == 3:
        drawMessage_S4(txtNirISS)

    elif num == 4:
        drawMessage_S4(txtMiri)

# Create our turtle Objects (outside and before main) that we will use
isim_figure = turtle.Turtle() # Background Turtle
nir_Spec = turtle.Turtle()
nir_Cam = turtle.Turtle()
nir_ISS = turtle.Turtle()
miri = turtle.Turtle()

def scene4():
    txtStart = "Commander! We now need to assemble the ISIM system to get this thing up and running, can you do it? I'm quite far away to do it myself, don't forget to click in check to verify you process!"

    # Call functions in order to be performed
    screen_S4 = screen_turtle_s4() # Creates and initializes the app window
    registerShapes_S4() # Saves que .gif into shapes
    
    drawMessage_S4(txtStart)
    fourth_scene() # Calls the fourth_scene
    createObjects_S4()

    # Calls to the funtions that drag and drop the items
    nir_Spec.ondrag(nir_Spec_fxn)
    nir_Cam.ondrag(nir_Cam_fxn)
    nir_ISS.ondrag(nir_ISS_fxn)
    miri.ondrag(miri_fxn)

    screen_S4.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def scene3_2():
    pantalla2 = turtle.Screen() # Create the screen and assign its characteristics
    pantalla2.clear()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    pantalla2.bgpic("JamesWebb3.gif")
    pantalla2.update()
    time.sleep(2) # Set the background pic to use as a template 

    frase1 = ["The James Webb Space Telescope, ","also known as Webb, works by ","studying the infrared light from ",
            "celestial objects, it's so big that ","to send it to space, the Webb ","Telescope team decided to make it "] # Create arrays with every line of the sentences
    frase2 = ["foldable, achieving this with the 18 hexagonal-","shaped mirror segments."]
    frase3 = ["Since July 2022, the Webb has brought us the ","neatest images ever captured by a telescope."]
    frase4 = ["Its creation represents ","a giant step forward ","in our understanding ","of the universe. "]
    frase5 = ["How did the universe ","begin? Are we alone ","in the cosmos?"] 

    a = -110
    b = 168 # Assign the x and y values to the paragraphs 

    for frase in frase1: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b) 
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 63 # Assign the x and y values to the paragraphs 
    for frase in frase2: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 15 # Assign the x and y values to the paragraphs 
    for frase in frase3: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase:# Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = 25
    b = -55 # Assign the x and y values to the paragraphs
    for frase in frase4: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 16 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = 25
    b = -130 # Assign the x and y values to the paragraphs
    for frase in frase5: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter


    # writes title and text
    score_pen.hideturtle()
    score_pen.penup()
    score_pen.setpos(-95, -240)
    score_pen.pendown()
    score_pen.pencolor("white")
    texto1 = "*Press 'A' to start"
    score_pen.penup()

    for letter1 in texto1:
        score_pen.write(letter1, align="center", font=("Pixelmix", 10, "bold"))
        score_pen.fd(10)

    pantalla2.listen()
    pantalla2.onkey(scene4,'a')
    pantalla2.mainloop()

def scene3_1():
    pantalla2 = turtle.Screen() # Create the screen and assign its characteristics
    pantalla2.clear()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    pantalla2.bgpic("Congrats2.gif")
    pantalla2.update()
    time.sleep(2) # Set the background pic to use as a template 

    frase1 = ["You assembled the","JAMES WEBB SPACE","TELESCOPE!!"] # Create arrays with every line of the sentences
    frase2 = ["This telescope was launched","on December 25th, 2021. To","achieve this, thousands of",
            "scientists, engineers and","technicians from 14 countries","worked together for almost 2",
            "decades."]
    frase3 = ["The James Webb Space Telescope is the largest","most powerful and precise telescope ever",
            "created!"]
    frase4 = ["One of the Webbs goals is to look “back in","time” to when galaxies where young, it will do",
            "this by observing galaxies at over 13 billion","light years away."]

    a = -110
    b = 140 # Assign the x and y values to the paragraphs 

    for frase in frase1: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b) 
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = 63 # Assign the x and y values to the paragraphs 
    for frase in frase2: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = -83 # Assign the x and y values to the paragraphs 
    for frase in frase3: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase:# Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    a = -220
    b = -160 # Assign the x and y values to the paragraphs
    for frase in frase4: # For every sentence in paragraphs
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(a, b)
        b = b - 18 # Subtract from the original y value to make the next sentence appear lower
        for frase in frase: # Create a loop that takes every word in the sentences
            for letter in frase: # Creates a loop that takes every letter in the words
                score_pen.write(letter, False, align="left", font=("PixelMix", 10, "normal"))
                score_pen.hideturtle()
                score_pen.fd(10) # Writes the sentences letter by letter

    time.sleep(2)

# Global bools 
isMirror1 = False
isMirror2 = False
isIsim = False
isAntenna = False
isMomentum_flap = False
isSolar_array = False
isSpacecraft_bus_star = False
isSunshield = False

# Function to initialize and define the app window
def screen_turtle():
    screen = turtle.Screen()
    screen.clearscreen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("black")
    screen.title("JWST Puzzle!")
    screen.bgpic("fondoFinal.gif")
    return screen

# Save .gif files as possible options for Turtle objects
def registerShapes():
    # Parts of the JWST
    pTelescope = ["mirror1.gif", "mirror2.gif", "ISIM.gif", "antenna.gif", "momentum_flap.gif", "solar_array.gif", "spacecraft_bus_star.gif", "sunshield.gif"]
    for part in pTelescope:
        turtle.register_shape(part)

    # Assembled by parts
    pArmedTelescope = ["f1JW.gif", "f2JW.gif", "f3JW.gif", "f4JW.gif", "f5JW.gif", "f6JW.gif", "f7JW.gif", "f8JW.gif"]
    for pArmed in pArmedTelescope:
        turtle.register_shape(pArmed)

    # Extra images
    imgExtras = ["jimmybee_happy.gif", "JWST_silueta.gif", "jimmybee_talk.gif"]
    for imgEx in imgExtras:
        turtle.register_shape(imgEx)

# Code for scene three
def third_scene():
    # Ghost Turtle (helps create dialog boxes and text)
    ghost = turtle.Turtle()
    ghost.hideturtle()

    # Draw the box above
    ghost.penup()
    ghost.setpos(-300, 260)
    ghost.pendown()
    ghost.pencolor("grey")
    ghost.pensize(80)
    ghost.speed(0)
    ghost.forward(600)

# The following functions allow us to drag and drop each element individually --

def mirror1_fxn(x, y): 
    mirror1.ondrag(None)
    mirror1.setheading(mirror1.towards(x, y)) # Rotates and moves forward mouse direction
    mirror1.goto(x, y) # Moves the object to the new coords
    mirror1.ondrag(mirror1_fxn) 

def mirror2_fxn(x, y): 
    mirror2.ondrag(None)  
    mirror2.setheading(mirror2.towards(x, y)) 
    mirror2.goto(x, y) 
    mirror2.ondrag(mirror2_fxn)

def isim_fxn(x, y): 
    isim.ondrag(None)  
    isim.setheading(isim.towards(x, y)) 
    isim.goto(x, y) 
    isim.ondrag(isim_fxn)

def antenna_fxn(x, y): 
    antenna.ondrag(None)  
    antenna.setheading(antenna.towards(x, y)) 
    antenna.goto(x, y) 
    antenna.ondrag(antenna_fxn)

def momentum_flap_fxn(x, y): 
    momentum_flap.ondrag(None)  
    momentum_flap.setheading(momentum_flap.towards(x, y)) 
    momentum_flap.goto(x, y) 
    momentum_flap.ondrag(momentum_flap_fxn)

def solar_array_fxn(x, y): 
    solar_array.ondrag(None)  
    solar_array.setheading(solar_array.towards(x, y)) 
    solar_array.goto(x, y) 
    solar_array.ondrag(solar_array_fxn)

def spacecraft_bus_star_fxn(x, y): 
    spacecraft_bus_star.ondrag(None)  
    spacecraft_bus_star.setheading(spacecraft_bus_star.towards(x, y)) 
    spacecraft_bus_star.goto(x, y) 
    spacecraft_bus_star.ondrag(spacecraft_bus_star_fxn)

def sunshield_fxn(x, y): 
    sunshield.ondrag(None)  
    sunshield.setheading(sunshield.towards(x, y)) 
    sunshield.goto(x, y) 
    sunshield.ondrag(sunshield_fxn)

# --------------------------------------------------------------------------

# Does the comparison to determine if the object is within the range to be placed
def posi(turtle):
    return (turtle.xcor() >= -159 and turtle.xcor() <= 159) and (turtle.ycor() >= -101 and turtle.ycor() <= 101)

# In each click, the app will check y there is any item inside the area to be placed
def checkPos(x, y):
    global isMirror1
    global isMirror2
    global isIsim
    global isAntenna
    global isMomentum_flap
    global isSolar_array
    global isSpacecraft_bus_star
    global isSunshield 

    # If an items is in place, the proper part of the JWST will appear as filled on screen 
    if(posi(mirror1)):
        isMirror1 = True
        mirror1.clear()
        mirror1.setpos(300, 300)
        mirror1.hideturtle()
        jwst_figure.shape("f1JW.gif")
        part_Info(1) # The app will display que info of this part of the telescope and their characteristics by calling the function part_Info

    if(isMirror1 and posi(mirror2)):
        isMirror2 = True
        mirror2.clear()
        mirror2.setpos(300, 300)
        mirror2.hideturtle()
        jwst_figure.shape("f2JW.gif")
        part_Info(2)

    if(isMirror2 and posi(isim)):
        isIsim = True
        isim.clear()
        isim.setpos(300, 300)
        isim.hideturtle()
        jwst_figure.shape("f3JW.gif")
        part_Info(3)

    if(isIsim and posi(antenna)):
        isAntenna = True
        antenna.clear()
        antenna.setpos(300, 300)
        antenna.hideturtle()
        jwst_figure.shape("f4JW.gif")
        part_Info(4)

    if(isAntenna and posi(momentum_flap)):
        isMomentum_flap = True
        momentum_flap.clear()
        momentum_flap.setpos(300, 300)
        momentum_flap.hideturtle()
        jwst_figure.shape("f5JW.gif")
        part_Info(5)

    if(isMomentum_flap and posi(solar_array)):
        isSolar_array = True
        solar_array.clear()
        solar_array.setpos(300, 300)
        solar_array.hideturtle()
        jwst_figure.shape("f6JW.gif")
        part_Info(6)

    if(isSolar_array and posi(spacecraft_bus_star)):
        isSpacecraft_bus_star = True
        spacecraft_bus_star.clear()
        spacecraft_bus_star.setpos(300, 300)
        spacecraft_bus_star.hideturtle()
        jwst_figure.shape("f7JW.gif")
        part_Info(7)

    if(isSpacecraft_bus_star and posi(sunshield)):
        isSunshield = True # END
        sunshield.clear()
        sunshield.setpos(300, 300)
        sunshield.hideturtle()
        jwst_figure.shape("f8JW.gif")
        part_Info(8)
        scene3_1()
        time.sleep(3)
        scene3_2()
        time.sleep(3)
    # Once the game is completed, isSunshield will be set as True, which means that the game is finished and will display que next part    

# Creates the objects 
def createObjects():
    # Generate and place the jwst_figure in its pos
    jwst_figure.shape("JWST_silueta.gif")
    jwst_figure.penup()
    jwst_figure.setpos(0,0)

    # Generate and place the mirror1 in its pos
    mirror1.shape("mirror1.gif")
    mirror1.left(90)
    mirror1.penup()
    mirror1.setpos(-233.34, 260) # -233.34
    mirror1.speed(0)

    # Generate and place the mirror2 in its pos
    mirror2.shape("mirror2.gif")
    mirror2.left(90)
    mirror2.penup()
    mirror2.setpos(-166.68, 260)
    mirror2.speed(0)

    # Generate and place the isim in its pos
    isim.shape("ISIM.gif")
    isim.left(90)
    isim.penup()
    isim.setpos(-100.02, 260)
    isim.speed(0)
    
    # Generate and place the antenna in its pos
    antenna.shape("antenna.gif")
    antenna.left(90)
    antenna.penup()
    antenna.setpos(-33.36, 260)
    antenna.speed(0)

    # Generate and place the momentum_flap in its pos
    momentum_flap.shape("momentum_flap.gif")
    momentum_flap.left(90)
    momentum_flap.penup()
    momentum_flap.setpos(33.36, 260)
    momentum_flap.speed(0)

    # Generate and place the solar_array in its pos
    solar_array.shape("solar_array.gif")
    solar_array.left(90)
    solar_array.penup()
    solar_array.setpos(100.02, 260)
    solar_array.speed(0)

    # Generate and place the spacecraft_bus_star in its pos
    spacecraft_bus_star.shape("spacecraft_bus_star.gif")
    spacecraft_bus_star.left(90)
    spacecraft_bus_star.penup()
    spacecraft_bus_star.setpos(166.68, 260)
    spacecraft_bus_star.speed(0)

    # Generate and place the sunshield in its pos
    sunshield.shape("sunshield.gif")
    sunshield.left(90)
    sunshield.penup()
    sunshield.setpos(233.34, 260)
    sunshield.speed(0)

    checking = turtle.Turtle()
    checking.hideturtle()
    checking.shape('circle')
    checking.fillcolor("blue")
    checking.penup()
    checking.speed(0)
    checking.setpos(-250, -150)
    checking.pencolor("white")
    checking.write("Check", align="center", font=("Pixelmix", 12, "bold"))
    checking.onclick(checkPos)
    checking.showturtle()

def drawMessage(txt):
    # Ghost Turtle (helps create dialog boxes in this case)
    
    # Draw the box at the bottom
    ghost = turtle.Turtle()
    ghost.hideturtle()
    ghost.penup()
    ghost.setpos(-300, -250)
    ghost.pendown()
    ghost.pencolor("black")
    ghost.pensize(80)
    ghost.speed(0)
    ghost.forward(600)

    # We draw the all mighty jimmy Bee
    jimmyBee = turtle.Turtle()
    jimmyBee.hideturtle()
    jimmyBee.penup()
    jimmyBee.setpos(-250, -250)
    jimmyBee.shape("jimmybee_happy.gif")
    jimmyBee.showturtle()

    # Show the Jimmy Bee text
    ghost_INFO = turtle.Turtle()
    ghost_INFO.hideturtle()
    ghost_INFO.penup()
    ghost_INFO.setpos(-210, -235)
    ghost_INFO.pendown()
    ghost_INFO.pencolor("white")
    ghost_INFO.penup()

    # This FOR loop allows us to write letter by letter
    for letter in txt:
        
        jimmyBee.shape("jimmybee_talk.gif")
        if ghost_INFO.xcor() < 290: # As long as the letters do not reach 290 pixels of the window (right limit)
            ghost_INFO.write(letter, align="left", font=("Pixelmix", 8, "bold"))
            jimmyBee.shape("jimmybee_happy.gif")
            ghost_INFO.fd(10)

        else: # When it reaches it, start writing on the bottom line
            ghost_INFO.setpos(-210, ghost_INFO.ycor() - 18)
            ghost_INFO.write(letter, align="left", font=("Pixelmix", 8, "bold"))
            jimmyBee.shape("jimmybee_happy.gif")
            ghost_INFO.fd(10)

        # In case we encounter a dot, the system will erase que previous text written after a second and continue writing on a fixed position
        if letter == '.':
            time.sleep(1)
            ghost_INFO.clear()
            ghost_INFO.setpos(-210, -235)
    time.sleep(3)

# This function allow us to manage the different texts that will be displayed during the playthrough
def part_Info(num):

    txtMirror1 = "The primary mirror consists of 18 hexagonal segments made of beryllium, which is both strong and light. IT has the function to intercept red and infrared light traveling through space, this light is then reflected and then analyzed to obtain the images. The detail it can see is directly related to the size of the surface area that collects the light of the objects observed in this case the hexagons are extremely big (1,32 meters of diameter)"
    txtMirror2 = "The second mirror is where the cosmos light hits the telescope. It is supported by three 25 feet long struts that are extended from the primary mirror. This mirror is perfectly rounded and  convex so the reflective surface bulges toward a light source."
    txtISIM = "The Integrated Science Instrument Module, also known as the ISIM contains the four main instruments that will detect light from galaxies, distant stars, and planets. These four instruments are extremely sensitive and precise.  It can be said that the ISIM “It's the heart of the Telescope”."
    txtAntenna = "The high gain antenna is the main data antenna and main mean of communication between the telescope and the controllers on Earth. Also, the Webbs science data and imagery is transmitted to Earth from this antenna."
    txtMomentum = "The momentum trim flap helps balance pressure from solar radiation on Webb's sunshield, much like a trim tab helps stabilize a boat or plane!"
    txtSolarArray = "The solar panels effectively ensure the production of electrical energy for the telescope, this way all the systems are always running. The role of the solar panels is to power the scientific instruments and enable the communication systems."
    txtBusStar = "The data from the star tracker helps to point the telescope towards the target so that it appears in the field of view of the intended analysis instrument. The spacecraft bus contains six subsystems: Electrical Power Subsystem, Altitude Control Subsystem, Communication Subsystem, Command and Data Handing Subsystem, Propulsion Subsystem, and the Thermal Control Subsystem."
    txtSunshield = "The sun shield is a set of 5 layers that work together to reduce the temperatures by 570 degrees Fahrenheit. The reason for this structure  is to radiate the heat between the layers that are made of Kapton, aluminum and silicons; this combination provides tolerance to extreme temperature variations."
    
    # Each num corresponds to an object on the screen and it also has a unique text message
    if num == 1:
        drawMessage(txtMirror1)

    elif num == 2:
        drawMessage(txtMirror2)

    elif num == 3:
        drawMessage(txtISIM)

    elif num == 4:
        drawMessage(txtAntenna)

    elif num == 5:
        drawMessage(txtMomentum)
    
    elif num == 6:
        drawMessage(txtSolarArray)

    elif num == 7:
        drawMessage(txtBusStar)

    elif num == 8:
        drawMessage(txtSunshield)

def scene3():
    txtStart = "Hello there Commander, in order to assemble this you need to place in order each element, don't forget to click in check to confirm your progress!"

    # Call functions in order to be performed
    screen = screen_turtle() # Creates and initializes the app window
    registerShapes() # Saves que .gif into shapes

    drawMessage(txtStart)
    third_scene() # Calls the third_scene to create the top Menu
    createObjects()

    # Calls to the function that drag and drop the items
    mirror1.ondrag(mirror1_fxn)
    mirror2.ondrag(mirror2_fxn)
    isim.ondrag(isim_fxn)
    antenna.ondrag(antenna_fxn)
    momentum_flap.ondrag(momentum_flap_fxn)
    solar_array.ondrag(solar_array_fxn)
    spacecraft_bus_star.ondrag(spacecraft_bus_star_fxn)
    sunshield.ondrag(sunshield_fxn)
    screen.mainloop()

# Create our turtle Objects (outside and before scene3) that we will use
jwst_figure = turtle.Turtle()
mirror1 = turtle.Turtle()
mirror2 = turtle.Turtle()
isim = turtle.Turtle()
antenna = turtle.Turtle()
momentum_flap = turtle.Turtle()
solar_array = turtle.Turtle()
spacecraft_bus_star = turtle.Turtle()
sunshield = turtle.Turtle()

def scene2():

    listaimagenes = ["F1_5_9intro.gif","F2_4intro.gif","F3intro.gif","F2_4intro.gif","F1_5_9intro.gif","F6_8intro.gif","F7intro.gif","F6_8intro.gif",
                "F1_5_9intro.gif","F11intro.gif","F12intro.gif","F13intro.gif","F14intro.gif","F15intro.gif","F16intro.gif","F17intro.gif","F18intro.gif",
                "F19intro.gif","F20intro.gif","F21intro.gif","F22intro.gif","F23intro.gif","F24intro.gif","F25intro.gif","F26intro.gif","F27intro.gif",
                "F28intro.gif","F29intro.gif","F30intro.gif","F31intro.gif","F32intro.gif","F33intro.gif","F34intro.gif","F35intro.gif","F36intro.gif",
                "F37intro.gif","F38intro.gif","F39intro.gif","F40intro.gif","F41intro.gif","F42intro.gif","F43intro.gif","F44intro.gif"]

    # creates an array with the images that we will use througout the code

    pantalla2 = turtle.Screen() # create a window with its characteristics
    pantalla2.clearscreen()
    pantalla2.setup(WIDTH, HEIGHT)
    pantalla2.bgcolor("black")
    pantalla2.title("COSMIC EYE") 

    for i in listaimagenes: # shows the images from the array in order, using a loop
        pantalla2.bgpic(i)
        pantalla2.update()
        time.sleep(0.25)

    fantasma = turtle.Turtle()
    fantasma.hideturtle()
    fantasma.penup()
    fantasma.setpos(-300, -250)
    fantasma.pendown()
    fantasma.pencolor("black")
    fantasma.pensize(80) 
    fantasma.forward(600) # creates the text rectangle that will be displayed in the window

    score_pen = turtle.Turtle()
    score_pen2 = turtle.Turtle()
    score_pen.speed(0)
    score_pen2.speed(0)
    score_pen.color("white")
    score_pen2.color("white")
    score_pen.penup()
    score_pen2.penup()
    score_pen.setposition(-270, -250)
    score_pen2.setposition(-270, -270)
    scorestring = "HELP!! A micrometeorite just hit us and all the pieces"
    scorestring2 = "are flying away, please help me get them back."
    score_pen.write(scorestring, False, align="left", font=("PixelMix", 11, "normal"))
    score_pen2.write(scorestring2, False, align="left", font=("PixelMix", 11, "normal"))
    score_pen.hideturtle()
    score_pen2.hideturtle()

    turtle.onkey(scene3, 'a') # adds an atribute so that when 'a' is pressed, we move to the next scene of the game
    time.sleep(2)

def main():
    # creates menu backgound and size
    menu = turtle.Screen()
    menu.setup(WIDTH, HEIGHT)
    menu.bgcolor("black")
    menu.title("Cosmic Eyes")
    menu.bgpic("MENU.gif")
    menu.update()

    # writes title and text
    titulo = turtle.Turtle()
    titulo.hideturtle()
    titulo.penup()
    titulo.setpos(-145, -200)
    titulo.pendown()
    titulo.pencolor("white")
    texto1 = "COSMIC EYES"
    texto2 = "*Press 'A' to start"
    titulo.penup()

    
    for letter1 in texto1:
        titulo.write(letter1, align="center", font=("Pixelmix", 30, "bold"))
        titulo.fd(30)

    titulo.setpos(-90, -240)
    for letter2 in texto2:
        titulo.write(letter2, align="center", font=("Pixelmix", 12, "bold"))
        titulo.fd(10)

    # press 'a' to start the game
    menu.listen()
    menu.onkey(scene2,'a')
    menu.mainloop()

main()