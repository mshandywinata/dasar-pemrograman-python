import os
import curses as crs
from curses import wrapper
import time as tm
import random as rand

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Selamat Datang di Tes WPM!")
    stdscr.addstr("\nTekan tombol apapun untuk mulai!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"Kecepatan: {wpm} kata/menit")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = crs.color_pair(1)
        
        if char != correct_char:
            color = crs.color_pair(2)
            
        stdscr.addstr(0, i, char, color)

def load_text():
    with open("D:/Codes/Python/dasar-pemrograman-python/proyek_pribadi/mini_projects/tes_wpm/teks.txt", "r") as f:
        lines = f.readlines()
        return rand.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = tm.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(tm.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        
        elif len(current_text) < len(target_text):
            current_text.append(key)
    
def main(stdscr):
    crs.init_pair(1, crs.COLOR_GREEN, crs.COLOR_BLACK)
    crs.init_pair(2, crs.COLOR_RED, crs.COLOR_BLACK)
    crs.init_pair(3, crs.COLOR_WHITE, crs.COLOR_BLACK)
    
    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "Kamu telah berhasil menyelesaikan teksnya! Tekan tombol apapun untuk melanjutkan...")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break

wrapper(main)
