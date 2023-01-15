import curses
from curses.textpad import rectangle
from datetime import datetime, date
import os, vlc

copyright_ = "made by: NAVIAROK"
help_to_quit = "type 'q' to exit"
clock_dimensions = (82, 8)
separator = ["$$\ ","\__|","    ","$$\ ","\__|"]
characters = [[' $$$$$$\\\n', '$$ ___$$\\\n', '\\_/   $$ |\n', '  $$$$$ /\n', '  \\___$$\\\n', '$$\\   $$ |\n', '\\$$$$$$  |\n', ' \\______/'], ['$$\\   $$\\\n', '$$ |  $$ |\n', '$$ |  $$ |\n', '$$$$$$$$ |\n', '\\_____$$ |\n', '      $$ |\n', '      $$ |\n', '      \\__|'], [' $$$$$$\\\n', '$$  __$$\\\n', '\\__/  $$ |\n', ' $$$$$$  |\n', '$$  ____/\n', '$$ |\n', '$$$$$$$$\\\n', '\\________|'], [' $$$$$$\\\n', '$$  __$$\\\n', '$$ /  \\__|\n', '$$$$$$$\\\n', '$$  __$$\\\n', '$$ /  $$ |\n', ' $$$$$$  |\n', ' \\______/'], ['  $$\\\n', '$$$$ |\n', '\\_$$ |\n', '  $$ |\n', '  $$ |\n', '  $$ |\n', '$$$$$$\\\n', '\\______|'], ['$$$$$$$$\\\n', '\\____$$  |\n', '    $$  /\n', '   $$  /\n', '  $$  /\n', ' $$  /\n', '$$  /\n', '\\__/'], ['$$$$$$$\\\n', '$$  ____|\n', '$$ |\n', '$$$$$$$\\\n', '\\_____$$\\\n', '$$\\   $$ |\n', '\\$$$$$$  |\n', ' \\______/'], [' $$$$$$\\\n', '$$$ __$$\\\n', '$$$$\\ $$ |\n', '$$\\$$\\$$ |\n', '$$ \\$$$$ |\n', '$$ |\\$$$ |\n', '\\$$$$$$  /\n', ' \\______/'], [' $$$$$$\\\n', '$$  __$$\\\n', '$$ /  $$ |\n', '\\$$$$$$$ |\n', ' \\____$$ |\n', '$$\\   $$ |\n', '\\$$$$$$  |\n', ' \\______/'], [' $$$$$$\\\n', '$$  __$$\\\n', '$$ /  $$ |\n', ' $$$$$$  |\n', '$$  __$$<\n', '$$ /  $$ |\n', '\\$$$$$$  |\n', ' \\______/']]
temp_list = []
dictionary = {
    "0": 7,
    "1": 4,
    "2": 2,
    "3": 0,
    "4": 1,
    "5": 6,
    "6": 3,
    "7": 5,
    "8": 9,
    "9": 8
}

for i in range(10):
    characters.append(list())

def load_numbers(folder=""):
    index = 0
    for file in os.listdir(folder):
        with open(f"{folder}/{str(file)}", "r") as file:
            content = file.readlines()
            for line in content:
                characters[index].append(line)
        index += 1

def get_time():
    out    = list()
    time_now = datetime.now()
    hour   = time_now.strftime("%H")
    minute = time_now.strftime("%M")
    second = time_now.strftime("%S")
    time_now = (hour, minute, second)
    for side in time_now:
        for char in side:
            out.append(char)
    return out

def get_date():
    today = date.today()
    return today.strftime("%b-%d-%Y")

def add_str(stdscr=None, text=None, x=0, y=0, theme=None):
    for line in text:
        stdscr.addstr(y, x, line, theme)
        y += 1

def store_in(tuple_of_time, list):
    for number in tuple_of_time:
        list.append(characters[dictionary.get(number)])

def show_clock(stdscr=None, clock_list=None, x=0, y=0, width=10, height=8, separator_range=1, theme=None):

    DH = (x, y)
    UH = ((x+width+separator_range), y)
    DM = (x+(width*2)+(3*separator_range)+5, y)
    UM = (x+(width*2)+(3*separator_range)+width+separator_range+5, y)
    DS = ((x+(width*2)+(3*separator_range)+5)+(width*2)+(3*separator_range)+7, y)
    US = ((x+(width*2)+(3*separator_range)+5)+(width*2)+(3*separator_range)+5+width+separator_range+5, y)
    SEP1 = (((x+(width*2)+(2*separator_range)), y+3))
    SEP2 = (((x+((width*2)*2)+(2*separator_range))+10, y+3))

    add_str(stdscr=stdscr, text=clock_list[0], x=DH[0], y=DH[1], theme=theme)
    add_str(stdscr=stdscr, text=clock_list[1], x=UH[0], y=UH[1], theme=theme)
    add_str(stdscr=stdscr, text=clock_list[2], x=DM[0], y=DM[1], theme=theme)
    add_str(stdscr=stdscr, text=clock_list[3], x=UM[0], y=UM[1], theme=theme)
    add_str(stdscr=stdscr, text=clock_list[4], x=DS[0], y=DS[1], theme=theme)
    add_str(stdscr=stdscr, text=clock_list[5], x=US[0], y=US[1], theme=theme)
    add_str(stdscr=stdscr, text=separator, x=SEP1[0], y=SEP1[1], theme=theme)
    add_str(stdscr=stdscr, text=separator, x=SEP2[0], y=SEP2[1], theme=theme)

def main(stdscr):

    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(1)

    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    MAGENTA_ON_BLACK = curses.color_pair(1)
    CYAN_ON_BLACK = curses.color_pair(2)
    BLACK_ON_CYAN = curses.color_pair(3)

    screen_height, screen_width = stdscr.getmaxyx()
    clock_begin = (((screen_width // 2) - 41), ((screen_height // 2) - 4)  ) # x, y

    stdscr.attron(CYAN_ON_BLACK)
    rectangle(stdscr, ((screen_height // 2) - 5),((screen_width // 2) - 43), ((screen_height // 2)-4)+clock_dimensions[1], ((screen_width // 2) - 39)+clock_dimensions[0])
    stdscr.addstr((screen_height // 2) - 5,(clock_begin[0]+(clock_dimensions[0]//2))-5,get_date())
    stdscr.attroff(CYAN_ON_BLACK)

    stdscr.attron(BLACK_ON_CYAN)
    stdscr.addstr(screen_height-1, 0, copyright_)
    stdscr.addstr(screen_height-1, screen_width-len(help_to_quit)-1, help_to_quit)
    stdscr.attroff(BLACK_ON_CYAN)

    while True:

        try:
            key = stdscr.getkey()
        except:
            key = ""

        store_in(get_time(), temp_list)
        show_clock(stdscr, temp_list, x=clock_begin[0], y=clock_begin[1], theme=MAGENTA_ON_BLACK)
        temp_list.clear()
        stdscr.refresh()
        if key == "q":
            break

if __name__ == "__main__":
    soundtrack = "Parasyte.mp3"
    p = vlc.MediaPlayer(soundtrack)
    p.play()

    try:
        curses.wrapper(main)
    except:
        print("[ERROR]: dimensions are not compatible")
