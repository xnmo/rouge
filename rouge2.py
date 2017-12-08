import curses
import random

races = ['human',
        'flying eyeball',
        'robot',
        'dino-person']
curses.initscr()
try:
    win = curses.newwin(0,0)
    win.addstr(0,2,'What is thy name? ')
    pcname = win.getstr()
    win.clear()
    win.refresh()
    y = 0
    for race in races:
        win.addstr(y,2,(str(y)+': '+str(race)))
        y += 1
    win.addstr(6,2, 'choose thine race: ')
    racechoice = win.getstr()
    
    pcy = random.randint(1,10)
    pcx = random.randint(1,10)

    curses.curs_set(0)
    while True:
        # clears screen and draws character
        win.clear()
        win.refresh()
        win.move(pcy,pcx)
        win.addch(ord('@'))
        
        # deals with movement 
        movement = win.getch()
        if movement == 104:
            pcx -= 1
        elif movement == 106:
            pcy += 1
        elif movement == 107:
            pcy -= 1
        elif movement == 108:
            pcx += 1
        elif movement == 121:
            pcx -= 1
            pcy -= 1
        elif movement == 117:
            pcx += 1
            pcy -= 1
        elif movement == 98:
            pcx -= 1
            pcy += 1
        elif movement == 110:
            pcx += 1
            pcy += 1

except:
    pass
finally:
    curses.endwin()
#print pcname
#print races[int(racechoice)]
#y 121 | u 117 | b 98 | n 110
# h 104 || j 106 || k 107 || l 108
