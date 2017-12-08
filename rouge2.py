import curses
import random

races = ['Human',
        'Flying Eyeball',
        'Robot',
        'Dino-person']
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
    win.addstr(6,2, 'Choose thine race: ')
    racechoice = win.getstr()
    
    pcy = random.randint(1,10)
    pcx = random.randint(1,10)

    curses.curs_set(0)
    while True:
        # clears screen and draws character
        win.clear()
        win.refresh()
        liney = 0
        while liney != 21:
            win.addstr(liney, 41 , '#')
            win.addstr(liney, 0, '#')
            liney += 1
        linex = 0
        while linex != 41:
                win.addstr(20, linex, '#')
                win.addstr(0, linex, '#')
                linex += 1
        win.addstr(0, 43, 'NAME: ' + str(pcname))
        win.addstr(1, 43, 'RACE: ' + str(races[int(racechoice)]))
        win.addstr(3, 43, 'Move with:')
        win.addstr(5, 43, 'y k u')
        win.addstr(6, 43, ' \|/')
        win.addstr(7, 43, 'h-+-l')
        win.addstr(8, 43, ' /|\\')
        win.addstr(9, 43, 'b j n')


        win.move(pcy,pcx)
        win.addch(ord('@'))
        
        # deals with movement 
        movement = win.getch()
        if movement == 104:
            if pcx > 1:
                pcx -= 1
        elif movement == 106:
            if pcy < 19:
                pcy += 1
        elif movement == 107:
            if pcy > 1:
                pcy -= 1
        elif movement == 108:
            if pcx < 40:
                pcx += 1
        elif movement == 121:
            if pcy > 1 and pcx > 1:
                pcx -= 1
                pcy -= 1
        elif movement == 117:
            if pcy > 1 and pcx < 40:
                pcx += 1
                pcy -= 1
        elif movement == 98:
            if pcy < 19 and pcx > 1:
                pcx -= 1
                pcy += 1
        elif movement == 110:
            if pcy < 19 and pcx < 40:
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
