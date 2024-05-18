import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!\nPress any key to begin!\nPress ESC to exit the game!")
    stdscr.refresh()
    
    #we are waiting for the user to press any keyy and then the next lines of codes will be executed
    stdscr.getkey() 


def display_text(stdscr, target, current, wpm=0):
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f"WPM: {wpm}")


        for i, char in enumerate(current):
            correct_char = target[i]
            color = curses.color_pair(1)

            if char != correct_char:
                color = curses.color_pair(2)

            stdscr.addstr(0, i, char, color)

def load_text():
    with open("text.txt", "r") as fobj:
        lines = fobj.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    # to register the users key presses
    while True:

        # max() incoluded so to not get a zero division error
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len (current_text) / (time_elapsed / 60)) / 5)
         
        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try: 
            key = stdscr.getkey()
        except:
            continue

        # ASCII character representation
        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len (current_text) > 0: #Checking if the stack is UNDERFLOW
                current_text.pop()
        
        # this is done so that the user doesn't type more, else it will show index error for the above codes
        elif len(current_text) < len(target_text):
            current_text.append(key)



#standard output screen
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "You completed the text! Press any key to Continue or ESC to exit...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break
         
wrapper(main)

    