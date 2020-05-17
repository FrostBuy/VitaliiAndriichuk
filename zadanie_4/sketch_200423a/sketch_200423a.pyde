import random
add_library("pdf")

def setup():
    global img
    global img2
    global img3
    size(450, 600)
    beginRecord(PDF, "just a girl.pdf")
    img = loadImage("https://pixel-plus.pl/wp-content/uploads/2020/03/zdjecie-do-dowodu.jpg")
    img2 = loadShape("https://image.flaticon.com/icons/svg/43/43501.svg")
    img3 = loadShape("https://upload.wikimedia.org/wikipedia/commons/9/9d/Sunglasses_%28example%29.svg")
    textSize(50)
    
def draw():
    global img
    global img2
    global img3
    if (25 < mouseY < 50):
        if (420 < mouseX < 440):
            fill(0, 0, 255)
            text("2", 410, 50)
            shape(img3, 80, 200, height/2, width/3)
            endRecord()
        if (385 < mouseX < 400):
            fill(0, 0, 255)
            text("1", 380, 50)
            shape(img2, 80, 275, height/2, width/2)
            endRecord()
    else: # żeby się nie nadpisywał musi jeden dotyczyć obu warunków
        fill(150, 255, 150, 100)
        image(img, 0, 0, 450, 600)
        text("1", 380, 50)
        text("2", 410, 50)

    
# plus do aktywności za estetyczny minimalistyczny UI
#1,25pkt za niedociągniętą logikę i brak prawidłowego eksportu
