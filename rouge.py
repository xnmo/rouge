import curses
import dungeon
import pc

def main():
	curses.initscr()
	try:
		win = curses.newwin(0, 0)
	
		# get player name and race
		chargen = pc.CharacterCreation()
		chargen.askForName(win, 0, 0)
		name = win.getstr()#.decode(encoding='utf-8')
		chargen.askForRace(win, 0, 1)
		race = win.getstr()
		
		#clear the screen
		win.clear()
		win.refresh()
		
		# instantiate classes
		d = dungeon.Dungeon()
		pcinfo = pc.PlayerCharacter(name, race)
		
		# prints character info
		win.addstr(2, 0, 'IS THIS THINE TRUE SELF?')	
		pcinfo.drawTo(win, 5, 4)
		win.addstr(13, 9, 'Y or N')
		win.refresh()
		
		# waits for a keypress
		win.getch()
		
		# clear the screen
		win.clear()
		win.refresh()

		#draw dungeon map and close on keystroke
		d.drawTo(win, 0, 0)
		win.getch()
	except:
		curses.endwin()
	finally:
		pass
	# return terminal to normal
	curses.endwin()

main()	
