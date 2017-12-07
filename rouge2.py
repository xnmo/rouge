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
    
    curses.curs_set(0)
    win.clear()
    win.refresh()
    win.move(10,10)
    win.addch(ord('@'))
    win.getch()
except:
    pass
finally:
    curses.endwin()
#curses.endwin()
#print pcname
#print races[int(racechoice)]
