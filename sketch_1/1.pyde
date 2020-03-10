def setup():
    size(1280, 720)

value = 0

def draw():
    background(255, 40, 0)
    fill(value)
    if mousePressed:
        circle(200,120,200)
    else: rect(200, 300, 150, 100)
    line(0, 0, 1280, 720)
    line(760, 1280, 0, 0)
    line(0, 0, 1280, 240)
    rect(width/3, height/3, width/3*2, height/3*2)

def mouseClicked():
    global value
    if value == 0:
        value = 255
    else:
        value = 0
