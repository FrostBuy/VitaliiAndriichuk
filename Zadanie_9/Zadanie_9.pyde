def setup():
    global img
    global img2
    size(800, 600)
    img = loadImage("P_1.png")
    img2 = loadImage("P_2.png")

def draw():
    global img
    global img2
    clear()
    if mousePressed:
        image(img, 250, 150, 300, 300)
        textSize(25)
        text("A secret pony :)", 280, 100)
        fill(200, 50, 50)
        noFill()
        stroke(0, 255, 0)
        rect(250, 150, 300, 300)
    else:
        try:
            image(img2, 250, 150, 300, 300)
            noFill()
            stroke(0, 0, 255)
            rect(250, 150, 300, 300)
        except:
            textSize(25)
            text("The file is missing", 280, 300)
            fill(200, 50, 50)
            noFill()
            stroke(255, 0, 0)
            rect(250, 150, 300, 300)
        
