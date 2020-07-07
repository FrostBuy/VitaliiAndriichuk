def setup():
    global img
    global img2
    size(800, 600)
    img = loadImage("P_1.png")
    img2 = loadImage("P_2.png")
    noFill()
    textSize(25)

def draw():
    global img
    global img2
    clear()
    if mousePressed:
        image(img, 250, 150, 300, 300)
        text("A secret pony :)", 280, 100)
        stroke(0, 255, 0)
    else:
        try:
            image(img2, 250, 150, 300, 300)
            stroke(0, 0, 255)
        except:
            text("The file is missing", 280, 300)
            stroke(255, 0, 0)
    rect(250, 150, 300, 300)
    
#1,5pkt +
        
