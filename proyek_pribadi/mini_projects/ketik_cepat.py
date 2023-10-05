import curses as crs
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Selamat Datang di Gim Ketik Cepat!")
    stdscr.addstr("\nTekan tombol apapun untuk mulai!")
    stdscr.refresh()
    stdscr.getkey()
    
def wpm_test(stdscr):
    target_text = "Hello, world! This is some test text for this program!"
    current_text = []
    
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    
    while True:
        key = stdscr.getkey()
        current_text.append(key)
        
        for char in current_text:
            stdscr.addstr(char, )
    
def main(stdscr):
    crs.init_pair(1, crs.COLOR_GREEN, crs.COLOR_BLACK)
    crs.init_pair(2, crs.COLOR_RED, crs.COLOR_BLACK)
    crs.init_pair(3, crs.COLOR_WHITE, crs.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
