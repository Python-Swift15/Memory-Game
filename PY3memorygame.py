import random
import time
import os
import sys

# ===== SETTINGS =====
DIFFICULTIES = {
    "1": ("Easy",   1.0),
    "2": ("Medium", 0.8),
    "3": ("Hard",   0.6),
    "4": ("Pro",    0.45),
    "5": ("God",    0.3),
}

COLORS = {
    "1": "\033[91m",  # bright red
    "2": "\033[92m",  # bright green
    "3": "\033[93m",  # bright yellow
    "4": "\033[94m",  # bright blue
    "reset": "\033[0m"
}

# ===== PLATFORM INPUT =====
def get_key():
    try:
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return key
    except:
        import msvcrt
        return msvcrt.getch().decode()

def clear():
    os.system("clear")  # 'cls' for Windows

def beep(freq):
    # simple variation using system bell
    print("\a", end="", flush=True)
    time.sleep(freq)

def loading_bar():
    clear()
    print("Loading Memory Game...\n")
    for i in range(0, 101, 5):
        bar = "█" * (i // 5) + " " * (20 - i // 5)
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(0.05)
    print("\n")

def intro():
    loading_bar()
    print("\n🧠 MEMORY GAME\n")
    print("Repeat the sequence using keys 1-4")
    input("\nPress Enter to start...")

def choose_difficulty():
    clear()
    print("Select Difficulty:\n")
    for key, (name, _) in DIFFICULTIES.items():
        print(f"{key}. {name}")
    return DIFFICULTIES.get(input("\n> ").strip(), DIFFICULTIES["1"])

def show_sequence(sequence, speed):
    for num in sequence:
        clear()
        print("\n\n")
        print(f"   {COLORS[num]}{num}{COLORS['reset']}   ")
        beep(0.05 * int(num))  # different tone feel
        time.sleep(speed)
        clear()
        time.sleep(0.2)

def streak(level):
    if level % 5 == 0:
        print("\n🔥 ON FIRE!")
    elif level % 3 == 0:
        print("\n⚡ SPEEDING UP!")

def fake_save():
    print("\nSaving progress...")
    time.sleep(1)
    print("Saved!")
    time.sleep(1)

def get_player_input(length):
    print("\nRepeat sequence:")
    user = ""
    while len(user) < length:
        key = get_key()
        if key in ["1", "2", "3", "4"]:
            print(COLORS[key] + key + COLORS["reset"], end=" ", flush=True)
            beep(0.05 * int(key))
            user += key
    print()
    return user

def play():
    intro()
    name, speed = choose_difficulty()

    sequence = []
    level = 1

    while True:
        sequence.append(str(random.randint(1, 4)))

        clear()
        print(f"{name} | Level {level}")
        time.sleep(1)

        show_sequence(sequence, speed)

        user = get_player_input(len(sequence))

        if user != "".join(sequence):
            print("\n❌ Wrong!")
            print("Correct:", "".join(sequence))
            print(f"Final Level: {level}")
            fake_save()
            break

        print("\n✅ Correct!")
        streak(level)

        level += 1
        speed = max(0.15, speed - 0.02)
        time.sleep(1.2)

# RUN
play()