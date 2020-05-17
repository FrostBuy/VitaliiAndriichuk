def setup():
    size(400, 400)


def draw():
    clear()
    if (50 < mouseX < 75) and (50 < mouseY < 75):
        fill(0, 0, 255)
    else:
        fill(0, 255, 0, 0)
    textSize(50)
    text("V", 50, 70)
    
    if (85 < mouseX < 110) and (50 < mouseY < 75):
        fill(0, 0, 255)
    else:
        fill(0, 255, 0, 0)
    textSize(50)
    text("A", 90, 70)
    


    if keyPressed:   #for "V"
        if key == "V" or key =="v":
            fill(40, 117, 22, 200)
            text("V", 50, 70)        
    else:
        fill(120,0,0)
        text("V", 50, 70)
    if key == CODED:
        if keyCode == RIGHT:
            fill(200, 70, 22, 80)
            text("V", 50, 70)
    if key == CODED:
        if keyCode == LEFT:
            fill(210, 120, 22, 80)
            text("V", 50, 70)

 
            
    if keyPressed:   #for "A"
        if key == "A" or key =="a":
            fill(40, 117, 22, 200)
            text("A", 90, 70)        
    else:
        fill(120,0,0)
        text("A", 90, 70)
    if key == CODED:
        if keyCode == RIGHT:
            fill(200, 70, 22, 80)
            text("A", 90, 70)
    if key == CODED:
        if keyCode == LEFT:
            fill(210, 120, 22, 80)
            text("A", 90, 70)
