def triangle():
    base = int(input('enter the base: '))
    height = int(input('enter the height: '))
    print('area of triangle :' ,(0.5*base*height))


def square():
    side = int(input('enter the side: '))
    print('area of sqaure :' ,(side*4))



def circle():
    radious = int(input('enter the radious: '))
    print('area of circle :' , (3.14*radious*radious))


while True:
    choice = int(input('enter your choice'))
    areaof = {
        1: triangle,
        2: square,
        3: circle,
        4: exit
    }
    output = areaof[choice]()



