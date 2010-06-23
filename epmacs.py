
import curses, sys, traceback

# global variables
class gb:
    scrn = None # will point to window object
    row = None # current row position
    col = None # current column position

class Buffer:
    def __init__(self):
        self.name = ""
        self.data = ""
        self.window = gb.scrn
        self.row = 0
        self.col = 0
        self.win_row = 0
        self.win_col = 0

        """Point is the current location where editing operations are taking place. It is defined in terms of a private data type, since different implementations will use different representations. As it turns out, there is never a need for any code outside of the sub-editor to ever be aware of the representation of this data type.

Cur_line is optional. If implemented, it provides a high-speed way to track the current line number.

Num_chars is optional. If implemented, it provides a high-speed way to track the total number of characters in the buffer (its length).

Num_lines is optional. If implemented, it provides a high-speed way to track the total number of lines in the buffer.

Mark_list is the list of marks defined for this buffer. The mark structure is defined later.

Contents indicates the actual buffer contents. As with the location data type, its specifics will vary with the implementation.

File_name is the name of the file associated with the buffer, or the empty string if there is no associated file.

File_time is the last time at which the contents of the file and buffer were identical (i.e., the time of the last read or write). On multi-process systems, this value can be used to determine whether the contents of the file have been changed by another process, and thus whether the copy being edited is in synchronization with the actual file.

Is_modified indicates whether the buffer has been modified since it was last written out or read in.

Mode_list is the list of modes in effect for the buffer. The mode structure is defined next.

	struct mark {
		struct mark *next_mark;
		mark_name name;
		location where_it_is;
		FLAG is_fixed;
		};
This structure is a linked list and is repeated for every mark. The chain is not circular. It probably is a good idea to keep the list sorted in the order that the marks appear in the buffer.

Next_mark is a pointer to the next mark in the chain. A NULL pointer indicates the end of the chain.

Name is the name of the mark. This name is returned by the mark creation routine and provides a way for the user to refer to specific marks. If your implementation permits, you can just return a pointer to the mark structure instead of making up names.

Where_it_is is the mark's location.

Is_fixed indicates whether the mark is a fixed mark.

	struct mode {
		struct mode *next_mode;
		char *mode_name;
		status (*add_proc)();
		};
This structure is a linked list and is repeated for every mode that is in effect for the current buffer. The chain is not circular. While modes should be defined in such a way that it does not matter what order they are invoked in, it is probably not possible to meet this requirement in actual practice. Thus, this list must be kept sorted in invocation order. Modes are discussed in more detail in Chapter 8.

Next_mode is a pointer to the next mode in the chain. A NULL pointer indicates the end of the chain.

Mode_name, if non-NULL, is the name added to the list of names of modes in effect. This list is ordinarily displayed somewhere on the screen. Note that there should be a mechanism for defining modes that do not have displayed names.

Add_proc is a pointer to a procedure to execute whenever the command set for this buffer needs to be created or re-created. The procedure should make all required modifications to the global command tables and return a success/fail status."""

    def write(self, char):
        self.window.addch(self.row, self.col, char)
        self.col = self.col + 1
    
class Epmacs:
    def __init__(self, stdscr):
        self.scrn = stdscr
        self.rows, self.cols = self.scrn.getmaxyx()

        

    
def main(stdscr):
    ed = Epmacs(stdscr)

    #current_buffer = Buffer()
    
    # set up a foreground/background color pair (can do many)
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
    ed.scrn.clear()

    ed.scrn.addstr("hi ")

    ed.scrn.addstr(str(ed.rows))
    ed.scrn.addstr(" x ")
    ed.scrn.addstr(str(ed.cols))

    ed.scrn.addstr(ed.rows-1, 0, "-" * (ed.cols-1), curses.A_REVERSE)
    
    # implement the actions done so far (just the clear())
    ed.scrn.refresh()
    # now play the "game"
    
    while True:
        c = ed.scrn.getch() # read character from keyboard

        #current_buffer.write(chr(c))
        if c == ord('q'): break

        
if __name__ == '__main__':
    curses.wrapper(main)

