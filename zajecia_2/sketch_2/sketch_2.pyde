#() krótka - do wartości tylko odczytywanych
#[] lista - pozostałe
#{} zbiór - kiedy nie chcemy duplikatów
#{} słownik - kiedy musimy rozmawiać  z zewnętrznymi programami



def setup():
    size(1280, 720)
    frameRate(10)
    global slownik
    global natezenie
    natezenie = 0
    slownik = {"czerwony":(255, 0, 0), "niebieski":(0, 0, 255), "szary":(120)}
def draw():
    # or you can write first (stroke(*slownik["niebieski"]) (and delete what in the 3 line)) and then you`ll have a blue line
    global natezenie
    kolory = ((255, 0, 0), (0, 0, 255), (0, 255, 0))
    stroke(natezenie, 0, 0, 100)
    natezenie = natezenie + 1
    if(natezenie == 255):
        natezenie=0
    line(mouseX, mouseY, width/3, height/3)


    #line(mouseX, mouseY, width/3, height/3) (fend off "kolory i stroke") or what above
    #global slownik (fend off "kolory i stroke") +
    #stroke(*slownik["niebieski"]) (fend off "kolory i stroke") +


    fill(*slownik["czerwony"])
    rect(60, 20, 600, 300)
    fill(slownik["szary"])
    stroke(*slownik["czerwony"])
    rect(600, 400, 100, 100)
    
    listaWliscie = [[10,20,30], [40,50,60], [70,80,90]]
    #print(listaWliscie[0][0])
    for podLista in listaWliscie:
        print(podLista)
        for element in podLista:
            print(element)
            
def mousePressed():
    exit()


    #myList = [[234, 189, 578, 189, 0], [234, 80, 956, 456, 189], [234, 189, 189, 90, 80], [234, 0, 189, 90, 134]]
    #for i in range(300):
    #    for index in myList:
    #        for index2 in index:
    #            stroke(20)
    #            print(myList[i][index2])
    #            point(i, 300)
    
