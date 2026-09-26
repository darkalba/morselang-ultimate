# morselang-ultimate
A fun Python programming language with Morse Code, colors, animations and mini-games. Great for beginners!
# 🚀 MorseLang Ultimate v5.1

**A complete Python programming language with Morse Code, colors, animations, ASCII charts, and mini-games!**

> **Created by Darkalba @c 2026**

---

## 📋 Table of Contents

- [About](#about)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Basic Commands](#basic-commands)
- [Morse Code](#morse-code)
- [Libraries](#libraries)
- [Visual Formatting](#visual-formatting)
- [Colors](#colors)
- [Animations](#animations)
- [Charts](#charts)
- [Mini-Games](#mini-games)
- [Complete Examples](#complete-examples)

---

## 📖 About

**MorseLang Ultimate** is an interpreted programming language written in Python that combines:

- ✅ **Real Morse Code** (encode, decode, visual, animations)
- ✅ **7 libraries** (MATH, RANDOM, DATETIME, STRING, SYSTEM, FILE, JSON)
- ✅ **9 visual formats** (box, diagonal, centered, etc.)
- ✅ **6 ANSI colors** (red, green, blue, etc.)
- ✅ **4 animations** (typing, scroll, bounce, grow)
- ✅ **ASCII charts** (bar charts)
- ✅ **2 mini-games** (Guess the Number, Tic-Tac-Toe)

---

## 🛠️ Installation

### Requirements

- Python 3.6 or newer

### Steps

1. Download the `morselang_ultimate.py` file
2. Open terminal in the folder where it's located
3. Run:

```bash
python morselang_ultimate.py
```

---

## 🎬 Getting Started

After running, you'll see:

```
============================================================
  MorseLang Ultimate v5.1 - WITH REAL MORSE CODE!  
  Created by Darkalba @c 2026
============================================================

Type code or 'help' for help, 'exit' to quit
NEW: Real Morse Code (Text ↔ Morse)!

MorseLang>
```

Type `help` to see all commands!

---

## 📝 Basic Commands

### Variables

```
SET X 10          # Set variable X
SET TEXT hello    # Set variable TEXT
PRINT X           # Print variable X
PRINT TEXT        # Print variable TEXT
```

### Math Operations

```
ADD Z X Y         # Z = X + Y
SUB Z X Y         # Z = X - Y
MUL Z X Y         # Z = X * Y
DIV Z X Y         # Z = X / Y
```

### Control Flow

```
IF X > 5 Y        # If X > 5, print Y
FOR I IN RANGE 10 # Loop from 0 to 9
```

### Arrays

```
ARRAY NUMS 1 2 3 4 5   # Create array
PUSH NUMS 6            # Add 6 to array
POP X NUMS             # Pop last element to X
GET X NUMS 2           # Get element at index 2
```

### Utilities

```
HELP          # Show help
VARS          # Show all variables
LIBS          # Show imported libraries
CLEAR         # Clear all variables
EXIT          # Exit program
```

---

## 📻 Morse Code

### MORSE.ENCODE

Convert text to Morse Code:

```
SET TEXT HELLO
MORSE.ENCODE TEXT
```

**Output:**
```
  => Text: HELLO
  => Morse: .... . .-.. .-.. ---
```

### MORSE.DECODE

Convert Morse Code to text:

```
SET CODE .... . .-.. .-.. ---
MORSE.DECODE CODE
```

**Output:**
```
  => Morse: .... . .-.. .-.. ---
  => Text: HELLO
```

### MORSE.VISUAL

Display Morse Code visually with colors:
- ● (green) = dot
- ━ (yellow) = dash

```
SET TEXT SOS
MORSE.VISUAL TEXT
```

**Output:**
```
●●● ━━━ ━━━ ●●●
```

### MORSE.ANIM

Morse Code animation with dots and dashes:

```
SET TEXT MORSE
MORSE.ANIM TEXT
```

**Output:** (animation with delay)
```
━━ ━━━ ●━● ●●● ●
```

### Morse Code Alphabet

| Letter | Code | Letter | Code | Letter | Code |
|--------|------|--------|------|--------|------|
| A | `.-` | N | `-.` | 0 | `-----` |
| B | `-...` | O | `---` | 1 | `.----` |
| C | `-.-.` | P | `.--.` | 2 | `..---` |
| D | `-..` | Q | `--.-` | 3 | `...--` |
| E | `.` | R | `.-.` | 4 | `....-` |
| F | `..-.` | S | `...` | 5 | `.....` |
| G | `--.` | T | `-` | 6 | `-....` |
| H | `....` | U | `..-` | 7 | `--...` |
| I | `..` | V | `...-` | 8 | `---..` |
| J | `.---` | W | `.--` | 9 | `----.` |
| K | `-.-` | X | `-..-` | | |
| L | `.-..` | Y | `-.--` | | |
| M | `--` | Z | `--..` | | |

**Space:** `/`

---

## 📚 Libraries

### MATH

```
IMPORT MATH

MATH.SQRT Z X      # Square root
MATH.SIN Z X       # Sine
MATH.COS Z X       # Cosine
MATH.TAN Z X       # Tangent
MATH.LOG Z X       # Logarithm (base 10)
MATH.LN Z X        # Natural logarithm
MATH.POW Z X Y     # X to the power of Y
MATH.PI Z          # Pi (3.14159...)
MATH.E Z           # Euler (2.71828...)
MATH.ABS Z X       # Absolute value
MATH.CEIL Z X      # Round up
MATH.FLOOR Z X     # Round down
MATH.ROUND Z X     # Round to 2 decimals
```

### RANDOM

```
IMPORT RANDOM

RANDOM.INT Z 100    # Random integer between 0 and 100
RANDOM.FLOAT Z      # Random float (0-1)
RANDOM.CHOICE Z ARR # Random element from array
RANDOM.SHUFFLE ARR  # Shuffle array
```

### DATETIME

```
IMPORT DATETIME

DATETIME.NOW Z      # Current date and time
DATETIME.DATE Z     # Current date
DATETIME.TIME Z     # Current time
DATETIME.YEAR Z     # Current year
DATETIME.MONTH Z    # Current month
DATETIME.DAY Z      # Current day
DATETIME.HOUR Z     # Current hour
DATETIME.MINUTE Z   # Current minute
DATETIME.SECOND Z   # Current second
```

### STRING

```
IMPORT STRING

STRING.UPPER Z TEXT      # Convert to uppercase
STRING.LOWER Z TEXT      # Convert to lowercase
STRING.CAPITALIZE Z TEXT # Capitalize first letter
STRING.REVERSE Z TEXT    # Reverse text
STRING.LEN Z TEXT        # Text length
STRING.REPLACE Z T O N   # Replace O with N in T
STRING.SPLIT ARR T D     # Split text T by delimiter D
STRING.JOIN T ARR D      # Join array ARR with delimiter D
STRING.FIND Z T S        # Find S in T (returns index)
STRING.STARTSWITH Z T P  # Check if T starts with P (1/0)
STRING.ENDSWITH Z T S    # Check if T ends with S (1/0)
```

### SYSTEM

```
IMPORT SYSTEM

SYSTEM.EXEC "notepad"    # Execute system command
SYSTEM.CWD Z             # Current working directory
SYSTEM.LS                # List files
SYSTEM.CD "folder"       # Change directory
SYSTEM.MKDIR "folder"    # Create directory
SYSTEM.RM "file.txt"     # Delete file
SYSTEM.ENV PATH          # Environment variable
```

### FILE

```
IMPORT FILE

FILE.READ X "file.txt"     # Read file to X
FILE.WRITE "file.txt" TXT  # Write TXT to file
FILE.APPEND "file.txt" TXT # Append TXT to file
FILE.EXISTS Z "file.txt"   # Check if file exists (1/0)
```

### JSON

```
IMPORT JSON

JSON.PARSE Z '{"key": "value"}'  # Parse JSON
JSON.STRINGIFY Z OBJ             # Convert object to JSON
```

---

## 🎨 Visual Formatting

### VISUAL.BOX

Display output in a double-bordered box:

```
SET X 144
MATH.SQRT Z X
PRINT Z
SET TEXT hello
STRING.REVERSE Z TEXT
PRINT Z
VISUAL.BOX
```

**Output:**
```
╔════════════════════════════════════════════════════════════╗
║   => X = 144                                                 ║
║   => Z = 12                                                  ║
║   => 12                                                      ║
║   => TEXT = hello                                            ║
║   => Z = olleh                                               ║
║   => olleh                                                   ║
╚════════════════════════════════════════════════════════════╝
```

### VISUAL.DIAG_UP

Diagonal (bottom-to-top):

```
SET X 144
MATH.SQRT Z X
PRINT Z
VISUAL.DIAG_UP
```

### VISUAL.DIAG_DOWN

Diagonal (top-to-bottom):

```
SET X 144
MATH.SQRT Z X
PRINT Z
VISUAL.DIAG_DOWN
```

### VISUAL.CENTER

Centered text:

```
DATETIME.NOW Z
PRINT Z
VISUAL.CENTER
```

### VISUAL.WIDE

Wide spacing between characters:

```
SET TEXT HELLO
PRINT TEXT
VISUAL.WIDE
```

### VISUAL.DOUBLE

Double spacing between lines:

```
SET X 10
PRINT X
SET Y 20
PRINT Y
VISUAL.DOUBLE
```

### VISUAL.FRAME

Simple frame:

```
SET X 144
MATH.SQRT Z X
PRINT Z
VISUAL.FRAME
```

### VISUAL.ARROW

Arrow-bordered box:

```
SET X 144
MATH.SQRT Z X
PRINT Z
VISUAL.ARROW
```

### VISUAL.STAR

Star-bordered box:

```
RANDOM.INT Z 100
PRINT Z
VISUAL.STAR
```

---

## 🌈 Colors

### COLOR.RED

```
SET TEXT Danger!
PRINT TEXT
COLOR.RED
VISUAL.BOX
```

### COLOR.GREEN

```
SET TEXT Success!
PRINT TEXT
COLOR.GREEN
VISUAL.BOX
```

### COLOR.YELLOW

```
SET TEXT Warning!
PRINT TEXT
COLOR.YELLOW
VISUAL.BOX
```

### COLOR.BLUE

```
SET TEXT Info
PRINT TEXT
COLOR.BLUE
VISUAL.BOX
```

### COLOR.MAGENTA

```
SET TEXT Special
PRINT TEXT
COLOR.MAGENTA
VISUAL.BOX
```

### COLOR.CYAN

```
SET TEXT Cyan
PRINT TEXT
COLOR.CYAN
VISUAL.BOX
```

---

## 🎬 Animations

### ANIM.TYPE

Typing animation:

```
SET TEXT Hello world!
ANIM.TYPE TEXT
```

### ANIM.SCROLL

Scroll animation:

```
SET TEXT Line 1
SET TEXT Line 2
SET TEXT Line 3
ANIM.SCROLL TEXT
```

### ANIM.BOUNCE

Bouncing text (left-right):

```
SET TEXT HELLO
ANIM.BOUNCE TEXT
```

### ANIM.GROW

Growing text:

```
SET TEXT MORSE
ANIM.GROW TEXT
```

---

## 📊 Charts

### GRAPH.BAR

Bar chart:

```
GRAPH.BAR Jan 100 Feb 150 Mar 200 Apr 175
```

**Output:**
```
==================================================
  BAR CHART  
==================================================
Jan        ████████████████████ 100
Feb        ██████████████████████████████ 150
Mar        ████████████████████████████████████ 200
Apr        ███████████████████████████████ 175
==================================================
```

---

## 🎮 Mini-Games

### GAME.GUESS

Guess the Number (1-100):

```
GAME.GUESS
```

**How to play:**
1. Computer picks a random number between 1 and 100
2. You have 10 attempts to guess
3. You're told if your guess is too low or too high
4. If you guess it, you win!

### GAME.TICTAC

Tic-Tac-Toe (X and O):

```
GAME.TICTAC
```

**How to play:**
1. Board has 9 positions (0-8)
2. Player X starts
3. Choose a free position (0-8)
4. Win by getting 3 in a row (horizontal, vertical, or diagonal)
5. If board fills without winner, it's a draw

**Board positions:**
```
  0 | 1 | 2
  ----------
  3 | 4 | 5
  ----------
  6 | 7 | 8
```

---

## 💻 Complete Examples

### Example 1: Morse Code

```
SET TEXT HELLO
MORSE.ENCODE TEXT
MORSE.VISUAL TEXT
MORSE.ANIM TEXT

SET CODE .... . .-.. .-.. ---
MORSE.DECODE CODE
```

### Example 2: Math Calculator

```
IMPORT MATH

SET X 144
MATH.SQRT Z X
PRINT Z

SET Y 10
MATH.POW R Y 2
PRINT R

MATH.PI P
PRINT P

COLOR.GREEN
VISUAL.BOX
```

### Example 3: String Manipulation

```
IMPORT STRING

SET TEXT hello world
STRING.UPPER UPPER TEXT
PRINT UPPER

STRING.LOWER LOWER TEXT
PRINT LOWER

STRING.REVERSE REV TEXT
PRINT REV

STRING.LEN LEN TEXT
PRINT LEN

COLOR.BLUE
VISUAL.FRAME
```

### Example 4: Date and Time

```
IMPORT DATETIME

DATETIME.DATE D
PRINT D

DATETIME.TIME T
PRINT T

DATETIME.YEAR Y
PRINT Y

COLOR.YELLOW
VISUAL.CENTER
```

### Example 5: Complete Game

```
IMPORT RANDOM
IMPORT MATH

GAME.GUESS

RANDOM.INT Z 100
PRINT Z

MATH.SQRT R Z
PRINT R

COLOR.GREEN
VISUAL.STAR
```

### Example 6: Chart with Data

```
GRAPH.BAR Monday 50 Tuesday 75 Wednesday 60 Thursday 90 Friday 80

COLOR.GREEN
```

### Example 7: Multiple Animations

```
SET TEXT Welcome!
ANIM.TYPE TEXT

SET TEXT MORSE
ANIM.GROW TEXT

SET TEXT LANG
ANIM.BOUNCE TEXT
```

### Example 8: Morse + Colors

```
SET TEXT DARKALBA
MORSE.ENCODE TEXT
MORSE.VISUAL TEXT
MORSE.ANIM TEXT

SET TEXT X
MORSE.VISUAL TEXT
COLOR.CYAN
VISUAL.STAR
```

---

## 🏆 Quick Commands Reference

| Category | Commands |
|----------|----------|
| **Morse** | `MORSE.ENCODE`, `MORSE.DECODE`, `MORSE.VISUAL`, `MORSE.ANIM` |
| **Basic** | `SET`, `PRINT`, `ADD`, `SUB`, `MUL`, `DIV` |
| **Control** | `IF`, `FOR`, `ARRAY`, `PUSH`, `POP`, `GET` |
| **Math** | `MATH.SQRT`, `MATH.SIN`, `MATH.COS`, `MATH.PI` |
| **Random** | `RANDOM.INT`, `RANDOM.FLOAT`, `RANDOM.CHOICE` |
| **Date** | `DATETIME.NOW`, `DATETIME.DATE`, `DATETIME.TIME` |
| **String** | `STRING.UPPER`, `STRING.REVERSE`, `STRING.LEN` |
| **System** | `SYSTEM.LS`, `SYSTEM.CWD`, `SYSTEM.EXEC` |
| **File** | `FILE.READ`, `FILE.WRITE`, `FILE.APPEND` |
| **Visual** | `VISUAL.BOX`, `VISUAL.CENTER`, `VISUAL.STAR` |
| **Colors** | `COLOR.RED`, `COLOR.GREEN`, `COLOR.BLUE` |
| **Animations** | `ANIM.TYPE`, `ANIM.BOUNCE`, `ANIM.GROW` |
| **Charts** | `GRAPH.BAR` |
| **Games** | `GAME.GUESS`, `GAME.TICTAC` |
| **Utility** | `HELP`, `VARS`, `LIBS`, `CLEAR`, `EXIT` |

---

## 🎉 Credits

**Created by Darkalba @c 2026**

---

## 📝 License

Personal project - Use it as you wish!

---

## 🚀 Have Fun with MorseLang Ultimate!

Type `help` in the program to see all available commands!

---

## 📦 Files

- `morselang_ultimate.py` - Complete language v5.1
- `README.md` - This tutorial

---

## 🌐 Share It!

You can upload it to:
- **GitHub** - github.com
- **GitLab** - gitlab.com
- **SourceForge** - sourceforge.net
- **Replit** - replit.com (run it directly)

Or share it on programming forums!
