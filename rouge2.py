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
    win.refresh()
    
    win.clear()
    win.refresh()
    y = 0
    for race in races:
        win.addstr(y,2,(str(y)+': '+str(race)))
        y += 1
    win.addstr(6,2, 'choose thine race: ')
    racechoice = win.getstr()

except:
    curses.endwin()
finally:
    pass
curses.endwin()
#print pcname
#print races[int(racechoice)]
