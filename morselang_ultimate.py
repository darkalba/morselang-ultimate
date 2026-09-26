# MorseLang Ultimate v5.1 - CU COD MORSE REAL!
# Culori, Animații, Grafice, Mini-Games, Cod Morse
# Creat de Darkalba @c 2026

import math
import random
import datetime
import subprocess
import os
import json
import time

# ============= COD MORSE REAL =============
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Invers pentru decodare
MORSE_TO_TEXT = {v: k for k, v in MORSE_CODE.items()}

def text_to_morse(text):
    """Convertește text în cod Morse"""
    result = []
    for char in text.upper():
        if char in MORSE_CODE:
            result.append(MORSE_CODE[char])
        else:
            result.append('?')  # Caracter necunoscut
    return ' '.join(result)

def morse_to_text(morse):
    """Convertește cod Morse în text"""
    result = []
    for code in morse.split():
        if code in MORSE_TO_TEXT:
            result.append(MORSE_TO_TEXT[code])
        elif code == '/':
            result.append(' ')
        else:
            result.append('?')  # Cod necunoscut
    return ''.join(result)

def morse_visual(morse, color=None):
    """Afișează cod Morse vizual cu culori"""
    visual = ""
    for char in morse:
        if char == '.':
            visual += colorize("●", Colors.GREEN if color is None else color) + " "
        elif char == '-':
            visual += colorize("━", Colors.YELLOW if color is None else color) + " "
        elif char == ' ':
            visual += "  "
        elif char == '/':
            visual += "   "
        else:
            visual += char + " "
    return visual

# ============= CULORI ANSI =============
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    
    # Background
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_BLUE = "\033[44m"
    BG_YELLOW = "\033[43m"
    BG_BLACK = "\033[40m"

def colorize(text, color):
    return f"{color}{text}{Colors.RESET}"

# ============= FUNCȚII DE FORMATARE VIZUALĂ =============

def draw_box(text, width=60, color=None):
    if not text.strip():
        text = "(empty)"
    box_top = "╔" + "═" * width + "╗"
    box_bottom = "╚" + "═" * width + "╝"
    
    if color:
        box_top = colorize(box_top, color)
        box_bottom = colorize(box_bottom, color)
    
    print(box_top)
    for line in text.split('\n'):
        if line.strip():
            padded = line.ljust(width)
            if color:
                print(colorize("║ " + padded + " ║", color))
            else:
                print("║ " + padded + " ║")
    print(box_bottom)

def draw_diagonal_up(text, start_space=0):
    if not text.strip():
        text = "(empty)"
    lines = [l for l in text.split('\n') if l.strip()]
    for i, line in enumerate(reversed(lines)):
        spaces = start_space + i
        print(" " * spaces + line)

def draw_diagonal_down(text, start_space=0):
    if not text.strip():
        text = "(empty)"
    lines = [l for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        spaces = start_space + i
        print(" " * spaces + line)

def draw_centered(text, width=60, color=None):
    if not text.strip():
        text = "(empty)"
    for line in text.split('\n'):
        if line.strip():
            padded = line.center(width)
            if color:
                print(colorize(padded, color))
            else:
                print(padded)

def draw_wide(text, spacing=3):
    if not text.strip():
        text = "(empty)"
    for line in text.split('\n'):
        if line.strip():
            spaced = (' ' * spacing).join(line)
            print(spaced)

def draw_double_spaced(text):
    if not text.strip():
        text = "(empty)"
    lines = [l for l in text.split('\n') if l.strip()]
    for line in lines:
        print(line)
        print()

def draw_framed(text, width=60, color=None):
    if not text.strip():
        text = "(empty)"
    top = "+" + "-" * width + "+"
    bottom = "+" + "-" * width + "+"
    
    if color:
        top = colorize(top, color)
        bottom = colorize(bottom, color)
    
    print(top)
    for line in text.split('\n'):
        if line.strip():
            padded = line.ljust(width)
            if color:
                print(colorize("| " + padded + " |", color))
            else:
                print("| " + padded + " |")
    print(bottom)

def draw_arrow_box(text, width=60, color=None):
    if not text.strip():
        text = "(empty)"
    top = "◄" + "─" * width + "►"
    bottom = "◄" + "─" * width + "►"
    
    if color:
        top = colorize(top, color)
        bottom = colorize(bottom, color)
    
    print(top)
    for line in text.split('\n'):
        if line.strip():
            padded = line.ljust(width)
            if color:
                print(colorize("│ " + padded + " │", color))
            else:
                print("│ " + padded + " │")
    print(bottom)

def draw_star_box(text, width=60, color=None):
    if not text.strip():
        text = "(empty)"
    top = "★" + "★" * width + "★"
    bottom = "★" + "★" * width + "★"
    
    if color:
        top = colorize(top, color)
        bottom = colorize(bottom, color)
    
    print(top)
    for line in text.split('\n'):
        if line.strip():
            padded = line.ljust(width)
            if color:
                print(colorize("★ " + padded + " ★", color))
            else:
                print("★ " + padded + " ★")
    print(bottom)

def draw_bar_chart(data, width=40, color=Colors.GREEN):
    """Desenează un bar chart ASCII"""
    if not data:
        print("No data!")
        return
    
    max_val = max(data.values()) if isinstance(data, dict) else max(data)
    
    print("\n" + "=" * (width + 10))
    print(colorize("  BAR CHART  ", Colors.BOLD))
    print("=" * (width + 10))
    
    if isinstance(data, dict):
        for label, value in data.items():
            bar_len = int((value / max_val) * width) if max_val > 0 else 0
            bar = "█" * bar_len
            print(f"{label:10} {colorize(bar, color)} {value}")
    else:
        for i, value in enumerate(data):
            bar_len = int((value / max_val) * width) if max_val > 0 else 0
            bar = "█" * bar_len
            print(f"Item {i:2} {colorize(bar, color)} {value}")
    
    print("=" * (width + 10) + "\n")

# ============= ANIMAȚII =============

def animate_typing(text, delay=0.05, color=None):
    """Animație de tastare"""
    for char in text:
        if color:
            print(colorize(char, color), end='', flush=True)
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print()

def animate_scroll(text, delay=0.1):
    """Animație de scroll"""
    lines = text.split('\n')
    for line in lines:
        print(line)
        time.sleep(delay)

def animate_bounce(text, times=3):
    """Animație de bounce (stânga-dreapta)"""
    for _ in range(times):
        for i in range(10):
            print(" " * i + text)
            time.sleep(0.05)
        for i in range(9, -1, -1):
            print(" " * i + text)
            time.sleep(0.05)

def animate_grow(text, max_size=5):
    """Animație de creștere"""
    for i in range(1, max_size + 1):
        print(text * i)
        time.sleep(0.1)

def animate_morse(text, delay=0.1):
    """Animație Morse - afișează puncte și liniuțe"""
    morse = text_to_morse(text)
    for char in morse:
        if char == '.':
            print(colorize("●", Colors.GREEN), end='', flush=True)
        elif char == '-':
            print(colorize("━", Colors.YELLOW), end='', flush=True)
        elif char == ' ':
            print(" ", end='', flush=True)
        elif char == '/':
            print("   ", end='', flush=True)
        time.sleep(delay)
    print()

# ============= MINI-GAMES =============

def game_guess_number():
    """Mini-game: Ghicește numărul"""
    print("\n" + "=" * 50)
    print(colorize("  GHICEȘTE NUMĂRUL  ", Colors.BOLD + Colors.YELLOW))
    print("=" * 50)
    
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"Am ales un număr între 1 și 100. Ai {max_attempts} încercări!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nÎncercarea {attempts + 1}: "))
            attempts += 1
            
            if guess == secret:
                print(colorize(f"\n🎉 FELICITĂRI! Ai ghicit în {attempts} încercări!", Colors.GREEN))
                return True
            elif guess < secret:
                print(colorize("Prea MIC!", Colors.RED))
            else:
                print(colorize("Prea MARE!", Colors.RED))
        except:
            print(colorize("Intră un număr valid!", Colors.RED))
    
    print(colorize(f"\n😞 Ai pierdut! Numărul era {secret}.", Colors.RED))
    return False

def game_tic_tac_toe():
    """Mini-game: X și 0 (Tic-Tac-Toe)"""
    print("\n" + "=" * 50)
    print(colorize("  X ȘI 0 (Tic-Tac-Toe)  ", Colors.BOLD + Colors.CYAN))
    print("=" * 50)
    
    board = [' ' for _ in range(9)]
    
    def print_board():
        print()
        for i in range(3):
            row = board[i*3:i*3+3]
            print(f"  {row[0]} | {row[1]} | {row[2]}  ")
            if i < 2:
                print("  " + "-" * 11)
        print()
    
    def check_win(player):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # cols
            [0,4,8], [2,4,6]            # diagonals
        ]
        return any(all(board[i] == player for i in win) for win in wins)
    
    current_player = 'X'
    
    for turn in range(9):
        print_board()
        try:
            pos = int(input(f"Player {current_player}, alege poziția (0-8): "))
            if board[pos] != ' ':
                print(colorize("Poziție ocupată!", Colors.RED))
                continue
            board[pos] = current_player
            
            if check_win(current_player):
                print_board()
                print(colorize(f"🎉 Player {current_player} CÂȘTIGĂ!", Colors.GREEN))
                return
        except:
            print(colorize("Intră o poziție validă (0-8)!", Colors.RED))
            continue
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board()
    print(colorize("🤝 EGalitate!", Colors.YELLOW))

# ============= EXECUȚIE COD =============

output_buffer = ""

def add_output(text):
    global output_buffer
    output_buffer += text + "\n"

def clear_output():
    global output_buffer
    output_buffer = ""

def get_output():
    global output_buffer
    return output_buffer

def parse_line(line):
    if not line.strip() or line.strip().startswith('#'):
        return None
    words = line.strip().split()
    return words

def execute(program, variables={}, functions={}, arrays={}, libs={}, visual_mode='normal'):
    global output_buffer
    lines = program.strip().split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        tokens = parse_line(line)
        
        if not tokens:
            i += 1
            continue
        
        cmd = tokens[0].upper()
        
        # ========== IMPORT LIBRARIES ==========
        if cmd == 'IMPORT':
            if len(tokens) >= 2:
                lib_name = tokens[1].upper()
                libs[lib_name] = True
                add_output(f"  => Imported {lib_name}")
        
        # ========== BASIC COMMANDS ==========
        elif cmd == 'PRINT':
            if len(tokens) >= 2:
                arg = tokens[1]
                if arg in variables:
                    add_output(f"  => {variables[arg]}")
                else:
                    add_output(f"  => {arg}")
        
        elif cmd == 'SET':
            if len(tokens) >= 3:
                var_name = tokens[1]
                value = tokens[2]
                variables[var_name] = value
                add_output(f"  => {var_name} = {value}")
        
        # ========== MATH OPERATIONS ==========
        elif cmd == 'ADD':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val1 = variables.get(tokens[2], 0)
                val2 = variables.get(tokens[3], 0)
                try:
                    variables[result_var] = int(val1) + int(val2)
                except:
                    variables[result_var] = str(val1) + str(val2)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'SUB':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val1 = int(variables.get(tokens[2], 0))
                val2 = int(variables.get(tokens[3], 0))
                variables[result_var] = val1 - val2
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MUL':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val1 = int(variables.get(tokens[2], 0))
                val2 = int(variables.get(tokens[3], 0))
                variables[result_var] = val1 * val2
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DIV':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val1 = int(variables.get(tokens[2], 1))
                val2 = int(variables.get(tokens[3], 1))
                variables[result_var] = val1 // val2
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        # ========== MATH LIBRARY ==========
        elif cmd == 'MATH.SQRT' or (cmd == 'SQRT' and libs.get('MATH')):
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = variables.get(tokens[2], 0)
                try:
                    variables[result_var] = int(math.sqrt(int(val)))
                except:
                    variables[result_var] = 0
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.SIN' or (cmd == 'SIN' and libs.get('MATH')):
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 0))
                variables[result_var] = round(math.sin(val), 6)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.COS' or (cmd == 'COS' and libs.get('MATH')):
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 0))
                variables[result_var] = round(math.cos(val), 6)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.TAN' or (cmd == 'TAN' and libs.get('MATH')):
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 0))
                variables[result_var] = round(math.tan(val), 6)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.LOG' or (cmd == 'LOG' and libs.get('MATH')):
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 1))
                variables[result_var] = round(math.log10(val), 6)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.LN' or (cmd == 'LN' and libs.get('MATH')):
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 1))
                variables[result_var] = round(math.log(val), 6)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.POW':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val1 = float(variables.get(tokens[2], 0))
                val2 = float(variables.get(tokens[3], 0))
                variables[result_var] = round(math.pow(val1, val2), 6)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.PI':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(math.pi)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.E':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(math.e)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.ABS':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = int(variables.get(tokens[2], 0))
                variables[result_var] = abs(val)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.CEIL':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 0))
                variables[result_var] = math.ceil(val)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.FLOOR':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 0))
                variables[result_var] = math.floor(val)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'MATH.ROUND':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = float(variables.get(tokens[2], 0))
                variables[result_var] = round(val, 2)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        # ========== RANDOM LIBRARY ==========
        elif cmd == 'RANDOM.INT':
            if len(tokens) >= 3:
                result_var = tokens[1]
                max_val = int(variables.get(tokens[2], 100))
                variables[result_var] = random.randint(0, max_val)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'RANDOM.FLOAT':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(round(random.random(), 6))
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'RANDOM.CHOICE':
            if len(tokens) >= 3:
                result_var = tokens[1]
                arr_name = tokens[2]
                if arr_name in arrays and arrays[arr_name]:
                    variables[result_var] = random.choice(arrays[arr_name])
                    add_output(f"  => {result_var} = {variables[result_var]}")
                else:
                    add_output("  => Array empty or not found!")
        
        elif cmd == 'RANDOM.SHUFFLE':
            if len(tokens) >= 2:
                arr_name = tokens[1]
                if arr_name in arrays:
                    random.shuffle(arrays[arr_name])
                    add_output(f"  => Shuffled {arr_name}")
                else:
                    add_output("  => Array not found!")
        
        # ========== DATETIME LIBRARY ==========
        elif cmd == 'DATETIME.NOW':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.DATE':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = datetime.datetime.now().strftime("%Y-%m-%d")
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.TIME':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = datetime.datetime.now().strftime("%H:%M:%S")
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.YEAR':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(datetime.datetime.now().year)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.MONTH':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(datetime.datetime.now().month)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.DAY':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(datetime.datetime.now().day)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.HOUR':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(datetime.datetime.now().hour)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.MINUTE':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(datetime.datetime.now().minute)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'DATETIME.SECOND':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = str(datetime.datetime.now().second)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        # ========== STRING LIBRARY ==========
        elif cmd == 'STRING.UPPER':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = variables.get(tokens[2], '')
                variables[result_var] = str(val).upper()
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.LOWER':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = variables.get(tokens[2], '')
                variables[result_var] = str(val).lower()
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.CAPITALIZE':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = variables.get(tokens[2], '')
                variables[result_var] = str(val).capitalize()
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.REVERSE':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = variables.get(tokens[2], '')
                variables[result_var] = str(val)[::-1]
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.LEN':
            if len(tokens) >= 3:
                result_var = tokens[1]
                val = variables.get(tokens[2], '')
                variables[result_var] = str(len(str(val)))
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.REPLACE':
            if len(tokens) >= 5:
                result_var = tokens[1]
                val = str(variables.get(tokens[2], ''))
                old = variables.get(tokens[3], '')
                new = variables.get(tokens[4], '')
                variables[result_var] = val.replace(old, new)
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.SPLIT':
            if len(tokens) >= 4:
                arr_name = tokens[1]
                val = str(variables.get(tokens[2], ''))
                delim = variables.get(tokens[3], ' ')
                arrays[arr_name] = val.split(delim)
                add_output(f"  => {arr_name} = {arrays[arr_name]}")
        
        elif cmd == 'STRING.JOIN':
            if len(tokens) >= 4:
                result_var = tokens[1]
                arr_name = tokens[2]
                delim = variables.get(tokens[3], ' ')
                if arr_name in arrays:
                    variables[result_var] = delim.join(arrays[arr_name])
                    add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.FIND':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val = str(variables.get(tokens[2], ''))
                sub = variables.get(tokens[3], '')
                variables[result_var] = str(val.find(sub))
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.STARTSWITH':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val = str(variables.get(tokens[2], ''))
                prefix = variables.get(tokens[3], '')
                variables[result_var] = '1' if val.startswith(prefix) else '0'
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'STRING.ENDSWITH':
            if len(tokens) >= 4:
                result_var = tokens[1]
                val = str(variables.get(tokens[2], ''))
                suffix = variables.get(tokens[3], '')
                variables[result_var] = '1' if val.endswith(suffix) else '0'
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        # ========== SYSTEM LIBRARY ==========
        elif cmd == 'SYSTEM.EXEC':
            if len(tokens) >= 2:
                command = ' '.join(tokens[1:])
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    add_output(result.stdout)
                    if result.stderr:
                        add_output(result.stderr)
                except Exception as e:
                    add_output(f"  => EXEC error: {e}")
        
        elif cmd == 'SYSTEM.CWD':
            if len(tokens) >= 2:
                result_var = tokens[1]
                variables[result_var] = os.getcwd()
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        elif cmd == 'SYSTEM.LS':
            add_output("  => Files in current directory:")
            for f in os.listdir('.'):
                add_output(f"     {f}")
        
        elif cmd == 'SYSTEM.CD':
            if len(tokens) >= 2:
                path = variables.get(tokens[1], tokens[1])
                try:
                    os.chdir(path)
                    add_output(f"  => Changed to {os.getcwd()}")
                except Exception as e:
                    add_output(f"  => CD error: {e}")
        
        elif cmd == 'SYSTEM.MKDIR':
            if len(tokens) >= 2:
                dir_name = variables.get(tokens[1], tokens[1])
                try:
                    os.makedirs(dir_name, exist_ok=True)
                    add_output(f"  => Created directory {dir_name}")
                except Exception as e:
                    add_output(f"  => MKDIR error: {e}")
        
        elif cmd == 'SYSTEM.RM':
            if len(tokens) >= 2:
                file_name = variables.get(tokens[1], tokens[1])
                try:
                    os.remove(file_name)
                    add_output(f"  => Deleted {file_name}")
                except Exception as e:
                    add_output(f"  => RM error: {e}")
        
        elif cmd == 'SYSTEM.ENV':
            if len(tokens) >= 2:
                env_var = tokens[1]
                variables[env_var] = os.environ.get(env_var, 'NOT_FOUND')
                add_output(f"  => {env_var} = {variables[env_var]}")
        
        # ========== FILE LIBRARY ==========
        elif cmd == 'FILE.READ':
            if len(tokens) >= 3:
                result_var = tokens[1]
                file_name = variables.get(tokens[2], tokens[2])
                try:
                    with open(file_name, 'r', encoding='utf-8') as f:
                        content = f.read()
                        variables[result_var] = content
                        add_output(f"  => {result_var} = (loaded from {file_name})")
                        add_output(f"  => Content: {content}")
                except Exception as e:
                    add_output(f"  => FILE.READ error: {e}")
        
        elif cmd == 'FILE.WRITE':
            if len(tokens) >= 3:
                file_name = variables.get(tokens[1], tokens[1])
                content = variables.get(tokens[2], '') if len(tokens) > 2 else ''
                try:
                    with open(file_name, 'w', encoding='utf-8') as f:
                        f.write(content)
                    add_output(f"  => Wrote to {file_name}")
                except Exception as e:
                    add_output(f"  => FILE.WRITE error: {e}")
        
        elif cmd == 'FILE.APPEND':
            if len(tokens) >= 3:
                file_name = variables.get(tokens[1], tokens[1])
                content = variables.get(tokens[2], '') if len(tokens) > 2 else ''
                try:
                    with open(file_name, 'a', encoding='utf-8') as f:
                        f.write(content)
                    add_output(f"  => Appended to {file_name}")
                except Exception as e:
                    add_output(f"  => FILE.APPEND error: {e}")
        
        elif cmd == 'FILE.EXISTS':
            if len(tokens) >= 3:
                result_var = tokens[1]
                file_name = variables.get(tokens[2], tokens[2])
                variables[result_var] = '1' if os.path.exists(file_name) else '0'
                add_output(f"  => {result_var} = {variables[result_var]}")
        
        # ========== JSON LIBRARY ==========
        elif cmd == 'JSON.PARSE':
            if len(tokens) >= 3:
                result_var = tokens[1]
                json_str = variables.get(tokens[2], tokens[2])
                try:
                    variables[result_var] = json_str
                    add_output(f"  => {result_var} = {variables[result_var]}")
                except Exception as e:
                    add_output(f"  => JSON.PARSE error: {e}")
        
        elif cmd == 'JSON.STRINGIFY':
            if len(tokens) >= 3:
                result_var = tokens[1]
                obj_name = tokens[2]
                try:
                    variables[result_var] = variables.get(obj_name, '')
                    add_output(f"  => {result_var} = {variables[result_var]}")
                except Exception as e:
                    add_output(f"  => JSON.STRINGIFY error: {e}")
        
        # ========== CONTROL FLOW ==========
        elif cmd == 'IF':
            if len(tokens) >= 5:
                var1 = variables.get(tokens[1], tokens[1])
                op = tokens[2]
                var2 = variables.get(tokens[3], tokens[3])
                result_var = tokens[4]
                
                try:
                    v1 = int(var1)
                    v2 = int(var2)
                    condition = False
                    if op == '>': condition = v1 > v2
                    elif op == '<': condition = v1 < v2
                    elif op == '==': condition = v1 == v2
                    
                    if condition and result_var in variables:
                        add_output(f"  => {variables[result_var]}")
                except:
                    add_output("IF error!")
        
        elif cmd == 'FOR':
            if len(tokens) >= 5 and tokens[2].upper() == 'IN' and tokens[3].upper() == 'RANGE':
                var_name = tokens[1]
                max_val = variables.get(tokens[4], 0)
                try:
                    for j in range(int(max_val)):
                        variables[var_name] = j
                        add_output(f"  => {var_name} = {j}")
                except:
                    add_output("FOR error!")
        
        # ========== ARRAYS ==========
        elif cmd == 'ARRAY':
            if len(tokens) >= 2:
                arr_name = tokens[1]
                values = tokens[2:] if len(tokens) > 2 else []
                arrays[arr_name] = values
                add_output(f"  => {arr_name} = {arrays[arr_name]}")
        
        elif cmd == 'PUSH':
            if len(tokens) >= 3:
                arr_name = tokens[1]
                value = tokens[2]
                if arr_name not in arrays:
                    arrays[arr_name] = []
                arrays[arr_name].append(value)
                add_output(f"  => Pushed {value} to {arr_name}")
        
        elif cmd == 'POP':
            if len(tokens) >= 3:
                result_var = tokens[1]
                arr_name = tokens[2]
                if arr_name in arrays and arrays[arr_name]:
                    variables[result_var] = arrays[arr_name].pop()
                    add_output(f"  => {result_var} = {variables[result_var]}")
                else:
                    add_output("  => Array empty!")
        
        elif cmd == 'GET':
            if len(tokens) >= 4:
                result_var = tokens[1]
                arr_name = tokens[2]
                index = int(variables.get(tokens[3], 0))
                if arr_name in arrays and 0 <= index < len(arrays[arr_name]):
                    variables[result_var] = arrays[arr_name][index]
                    add_output(f"  => {result_var} = {variables[result_var]}")
                else:
                    add_output("  => Out of bounds!")
        
        # ========== MORSE CODE COMMANDS ==========
        elif cmd == 'MORSE.ENCODE':
            if len(tokens) >= 2:
                text = variables.get(tokens[1], tokens[1]) if len(tokens) > 1 else get_output()
                morse = text_to_morse(text)
                add_output(f"  => Text: {text}")
                add_output(f"  => Morse: {morse}")
        
        elif cmd == 'MORSE.DECODE':
            if len(tokens) >= 2:
                morse = variables.get(tokens[1], tokens[1]) if len(tokens) > 1 else get_output()
                text = morse_to_text(morse)
                add_output(f"  => Morse: {morse}")
                add_output(f"  => Text: {text}")
        
        elif cmd == 'MORSE.VISUAL':
            if len(tokens) >= 2:
                text = variables.get(tokens[1], '') if len(tokens) > 1 else get_output()
                morse = text_to_morse(text)
                visual = morse_visual(morse)
                print(visual)
                clear_output()
        
        elif cmd == 'MORSE.ANIM':
            if len(tokens) >= 2:
                text = variables.get(tokens[1], '') if len(tokens) > 1 else get_output()
                animate_morse(text)
                clear_output()
        
        # ========== VISUAL MODE COMMANDS ==========
        elif cmd == 'VISUAL.BOX':
            color = variables.get(tokens[1].lower(), None) if len(tokens) > 1 else None
            draw_box(get_output(), color=color)
            clear_output()
        
        elif cmd == 'VISUAL.DIAG_UP':
            draw_diagonal_up(get_output())
            clear_output()
        
        elif cmd == 'VISUAL.DIAG_DOWN':
            draw_diagonal_down(get_output())
            clear_output()
        
        elif cmd == 'VISUAL.CENTER':
            color = variables.get(tokens[1].lower(), None) if len(tokens) > 1 else None
            draw_centered(get_output(), color=color)
            clear_output()
        
        elif cmd == 'VISUAL.WIDE':
            draw_wide(get_output())
            clear_output()
        
        elif cmd == 'VISUAL.DOUBLE':
            draw_double_spaced(get_output())
            clear_output()
        
        elif cmd == 'VISUAL.FRAME':
            color = variables.get(tokens[1].lower(), None) if len(tokens) > 1 else None
            draw_framed(get_output(), color=color)
            clear_output()
        
        elif cmd == 'VISUAL.ARROW':
            color = variables.get(tokens[1].lower(), None) if len(tokens) > 1 else None
            draw_arrow_box(get_output(), color=color)
            clear_output()
        
        elif cmd == 'VISUAL.STAR':
            color = variables.get(tokens[1].lower(), None) if len(tokens) > 1 else None
            draw_star_box(get_output(), color=color)
            clear_output()
        
        # ========== COLOR COMMANDS ==========
        elif cmd == 'COLOR.RED':
            add_output(colorize(get_output(), Colors.RED))
        
        elif cmd == 'COLOR.GREEN':
            add_output(colorize(get_output(), Colors.GREEN))
        
        elif cmd == 'COLOR.YELLOW':
            add_output(colorize(get_output(), Colors.YELLOW))
        
        elif cmd == 'COLOR.BLUE':
            add_output(colorize(get_output(), Colors.BLUE))
        
        elif cmd == 'COLOR.MAGENTA':
            add_output(colorize(get_output(), Colors.MAGENTA))
        
        elif cmd == 'COLOR.CYAN':
            add_output(colorize(get_output(), Colors.CYAN))
        
        # ========== ANIMATION COMMANDS ==========
        elif cmd == 'ANIM.TYPE':
            text = variables.get(tokens[1], '') if len(tokens) > 1 else get_output()
            animate_typing(text)
            clear_output()
        
        elif cmd == 'ANIM.SCROLL':
            text = variables.get(tokens[1], '') if len(tokens) > 1 else get_output()
            animate_scroll(text)
            clear_output()
        
        elif cmd == 'ANIM.BOUNCE':
            text = variables.get(tokens[1], '') if len(tokens) > 1 else get_output()
            animate_bounce(text)
            clear_output()
        
        elif cmd == 'ANIM.GROW':
            text = variables.get(tokens[1], '') if len(tokens) > 1 else get_output()
            animate_grow(text)
            clear_output()
        
        # ========== GRAPH COMMANDS ==========
        elif cmd == 'GRAPH.BAR':
            # Exemplu: GRAPH.BAR A 10 B 20 C 15
            data = {}
            j = 1
            while j < len(tokens):
                if j + 1 < len(tokens):
                    label = tokens[j]
                    try:
                        value = int(variables.get(tokens[j+1], tokens[j+1]))
                        data[label] = value
                    except:
                        pass
                    j += 2
                else:
                    break
            if data:
                draw_bar_chart(data)
        
        # ========== GAME COMMANDS ==========
        elif cmd == 'GAME.GUESS':
            game_guess_number()
        
        elif cmd == 'GAME.TICTAC':
            game_tic_tac_toe()
        
        # ========== SYSTEM COMMANDS ==========
        elif cmd == 'HELP':
            print("=" * 60)
            print(colorize("  MorseLang Ultimate v5.1 - CU COD MORSE REAL!  ", Colors.BOLD + Colors.CYAN))
            print("  Creat de Darkalba @c 2026")
            print("=" * 60)
            print()
            print(colorize("MORSE CODE:", Colors.YELLOW))
            print("  MORSE.ENCODE text    - Text → Morse")
            print("  MORSE.DECODE morse   - Morse → Text")
            print("  MORSE.VISUAL text    - Afișează Morse vizual (● și ━)")
            print("  MORSE.ANIM text      - Animație Morse")
            print()
            print(colorize("VISUAL MODES:", Colors.YELLOW))
            print("  VISUAL.BOX, VISUAL.DIAG_UP, VISUAL.DIAG_DOWN")
            print("  VISUAL.CENTER, VISUAL.WIDE, VISUAL.DOUBLE")
            print("  VISUAL.FRAME, VISUAL.ARROW, VISUAL.STAR")
            print()
            print(colorize("COLORS:", Colors.YELLOW))
            print("  COLOR.RED, COLOR.GREEN, COLOR.YELLOW")
            print("  COLOR.BLUE, COLOR.MAGENTA, COLOR.CYAN")
            print()
            print(colorize("ANIMATIONS:", Colors.YELLOW))
            print("  ANIM.TYPE, ANIM.SCROLL, ANIM.BOUNCE, ANIM.GROW")
            print()
            print(colorize("GRAPHS:", Colors.YELLOW))
            print("  GRAPH.BAR label1 val1 label2 val2 ...")
            print()
            print(colorize("GAMES:", Colors.YELLOW))
            print("  GAME.GUESS - Ghicește numărul")
            print("  GAME.TICTAC - X și 0")
            print()
            print(colorize("LIBRARIES:", Colors.YELLOW))
            print("  MATH, RANDOM, DATETIME, STRING, SYSTEM, FILE, JSON")
            print()
            print(colorize("BASIC:", Colors.YELLOW))
            print("  SET, PRINT, ADD, SUB, MUL, DIV, IF, FOR")
            print("  ARRAY, PUSH, POP, GET, HELP, VARS, CLEAR, EXIT")
            print("=" * 60)
        
        elif cmd == 'VERSION':
            print(colorize("MorseLang Ultimate v5.1 - CU COD MORSE REAL!", Colors.BOLD + Colors.GREEN))
            print("Creat de Darkalba @c 2026")
        
        elif cmd == 'CLEAR':
            variables.clear()
            arrays.clear()
            libs.clear()
            clear_output()
            print("All cleared!")
        
        elif cmd == 'VARS':
            if variables:
                print("Variabile:")
                for k, v in variables.items():
                    print(f"  {k} = {v}")
            else:
                print("Nicio variabila.")
        
        elif cmd == 'LIBS':
            if libs:
                print("Librării importate:")
                for k in libs.keys():
                    print(f"  - {k}")
            else:
                print("Nicio librărie importată.")
        
        i += 1
    
    return variables, functions, arrays, libs

# ============= PROGRAM INTERACTIV =============

print("=" * 60)
print(colorize("  MorseLang Ultimate v5.1 - CU COD MORSE REAL!  ", Colors.BOLD + Colors.CYAN))
print("  Creat de Darkalba @c 2026")
print("=" * 60)
print()
print("Scrie cod sau 'help' pentru ajutor, 'exit' pentru a ieși")
print(colorize("NOU: Cod Morse Real (Text ↔ Morse)!", Colors.GREEN))
print()

variables = {}
functions = {}
arrays = {}
libs = {}

while True:
    try:
        user_input = input("MorseLang> ").strip()
        
        if user_input.lower() == 'exit':
            print(colorize("\nLa revedere!", Colors.CYAN))
            break
        
        elif user_input.lower() == 'help':
            execute("HELP", variables, functions, arrays, libs)
            print()
            continue
        
        elif user_input.lower() == 'vars':
            if variables:
                print("Variabile:")
                for k, v in variables.items():
                    print(f"  {k} = {v}")
            else:
                print("Nicio variabila.")
            print()
            continue
        
        elif user_input.lower() == 'libs':
            if libs:
                print("Librării importate:")
                for k in libs.keys():
                    print(f"  - {k}")
            else:
                print("Nicio librărie importată.")
            print()
            continue
        
        elif user_input.lower() == 'clear':
            variables.clear()
            arrays.clear()
            libs.clear()
            clear_output()
            print("All cleared!")
            print()
            continue
        
        # Execută codul introdus
        variables, functions, arrays, libs = execute(user_input, variables, functions, arrays, libs)
        
    except KeyboardInterrupt:
        print(colorize("\n\nLa revedere!", Colors.CYAN))
        break
    except Exception as e:
        print(f"Eroare: {e}")
        print()
