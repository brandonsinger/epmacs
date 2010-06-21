
import curses, sys, traceback

# global variables
class gb:
    boxrows = int(sys.argv[1]) # number of rows in the box
    boxcols = boxrows # number of columns in the box
    scrn = None # will point to window object
    row = None # current row position
    col = None # current column position

    
def draw(chr):
    # paint chr at current position, overwriting what was there; if it's
    # the last row, also change colors; if instead of color we had
    # wanted, say, reverse video, we would specify curses.A_REVERSE instead of
    # curses.color_pair(1)
    if gb.row == gb.boxrows-1:
        gb.scrn.addch(gb.row, gb.col, chr, curses.color_pair(1))
    else:
        gb.scrn.addch(gb.row, gb.col, chr)

    # implement the change
    gb.scrn.refresh()
    # move down one row
    gb.row += 1
    # if at bottom, go to top of next column
    if gb.row == gb.boxrows:
        gb.row = 0
        gb.col += 1
        # if in last column, go back to first column
        if gb.col == gb.boxcols: gb.col = 0

    
def main(stdscr):    
    gb.scrn = stdscr
    
    # set up a foreground/background color pair (can do many)
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
    # clear screen
    gb.scrn.clear()
    # set current position to upper-left corner; note that these are our
    # own records of position, not Curses
    gb.row = 0
    gb.col = 0
    # implement the actions done so far (just the clear())
    gb.scrn.refresh()
    # now play the "game"
    while True:
        # read character from keyboard
        c = gb.scrn.getch()
        # was returned as an integer (ASCII); make it a character
        c = chr(c)
        # quit?
        if c == 'q': break
        # draw the character
        draw(c)
        
if __name__ == '__main__':
    curses.wrapper(main)

