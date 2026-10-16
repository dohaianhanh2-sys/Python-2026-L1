import curses

def draw_curses_ui(stdscr, students, courses):
    curses.curs_set(0)
    stdscr.clear()

    max_y, max_x = stdscr.getmaxyx()

    def safe_addstr(y, x, text, attr=curses.A_NORMAL):
        if y < max_y - 1 and x < max_x:
            stdscr.addstr(y, x, text[:max_x - x - 1], attr)

    line = 1
    safe_addstr(line, 2, "=== COURSE LIST ===", curses.A_BOLD)
    line += 1
    for c in courses.values():
        safe_addstr(line, 4, f"- {c.id}: {c.name} ({c.credits} credits)")
        line += 1

    line += 1
    safe_addstr(line, 2, "=== STUDENT RANKING BY GPA (DESCENDING) ===", curses.A_BOLD)
    line += 1
    header = f"{'Student ID':<12} | {'Name':<20} | {'Date of Birth':<15} | {'GPA':<6}"
    safe_addstr(line, 4, header, curses.A_UNDERLINE)
    line += 1

    for s in students:
        row = f"{s.id:<12} | {s.name:<20} | {s.dob:<15} | {s.gpa:<6.2f}"
        safe_addstr(line, 4, row)
        line += 1

    safe_addstr(line + 1, 2, "Press any key to exit...", curses.A_DIM)
    stdscr.refresh()
    stdscr.getch()

def display_results(students, courses):
    curses.wrapper(lambda stdscr: draw_curses_ui(stdscr, students, courses))