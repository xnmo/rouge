# Attempt at a simple map

# curses is a weird way to manipulate a terminal
import curses
import dungeon
import pc

def main():
	# this does a whole bunch of low level shit, just do it and don't worry about it
	curses.initscr()
	try:
		# this turns off the drawing of keys to the screen, unless otherwise specified
	#	curses.noecho()

		# this creates a window ie screen division 
		# of a certain size
		# in this case 0 lines, 0 columns
		# note, it is possible to give 2 more args	
		win = curses.newwin(0, 0)
		
		chargen = pc.CharacterCreation()
		chargen.askForName(win, 0, 0)
		name = win.getstr()#.decode(encoding='utf-8')
		chargen.askForRace(win, 0, 1)
		race = win.getstr()
		
		win.clear()
		win.refresh()
		
		d = dungeon.Dungeon()
		pcinfo = pc.PlayerCharacter(name, race)
		
		win.addstr(2, 0, 'IS THIS THINE TRUE SELF?')	
		# d.drawTo(win, 0, 0)
		pcinfo.drawTo(win, 5, 4)
		win.addstr(13, 9, 'Y or N')
		win.refresh()
		
		# waits for a keypress
		win.getch()
		win.clear()
		win.refresh()
		d.drawTo(win, 0, 0)
		win.getch()
		
	except:
		curses.endwin()
	finally:
		pass
	# return terminal to normal
	curses.endwin()

main()	
