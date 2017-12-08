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
    
    # starts the pc in a random position
    pcy = random.randint(1,10)
    pcx = random.randint(1,10)
    # hides the cursor
    curses.curs_set(0)
    # draws the playfield and UI
    while True:
        win.clear()
        win.refresh()
        liney = 0
        while liney != 21:
            win.addch(liney, 41 , 35)
            win.addch(liney, 0, 35)
            liney += 1
        linex = 0
        while linex != 41:
                win.addch(20, linex, 35)
                win.addch(0, linex, 35)
                linex += 1
        win.addstr(0, 43, 'NAME: ' + str(pcname))
        win.addstr(1, 43, 'RACE: ' + str(races[int(racechoice)]))
        win.addstr(3, 43, 'Move with:')
        win.addstr(5, 43, 'y k u')
        win.addstr(6, 43, ' \|/')
        win.addstr(7, 43, 'h-+-l')
        win.addstr(8, 43, ' /|\\')
        win.addstr(9, 43, 'b j n')
        win.addstr(12, 43, 'position x, y: ' + (str(pcx)+','+ str(pcy)))

        # moves cursor to the pc's position, then draws them
        win.move(pcy,pcx)
        win.addch(ord('@'))

        # moves the cursor away from the player character
        # if the cursor is in the checked area it will not
        # see an empty space there
        win.move(0,0
                ) 
        # deals with movement, checks for an empty space 
        movement = win.getch()
        if movement == 104:
            if win.inch(pcy,pcx-1) == 32:
                pcx -= 1
        elif movement == 106:
            if win.inch(pcy+1,pcx) == 32:
                pcy += 1
        elif movement == 107:
            if win.inch(pcy-1,pcx) == 32:
                pcy -= 1
        elif movement == 108:
            if win.inch(pcy,pcx+1) == 32:    
                pcx += 1
        elif movement == 121:
            if win.inch(pcy-1,pcx-1) == 32:
                pcx -= 1
                pcy -= 1
        elif movement == 117:
            if win.inch(pcy-1,pcx+1) == 32:
                pcx += 1
                pcy -= 1
        elif movement == 98:
            if win.inch(pcy+1,pcx-1) == 32:
                pcx -= 1
                pcy += 1
        elif movement == 110:
            if win.inch(pcy+1,pcx+1) == 32:
                pcx += 1
                pcy += 1

except:
    pass
finally:
    curses.endwin()
#y 121 | u 117 | b 98 | n 110
# h 104 || j 106 || k 107 || l 108
