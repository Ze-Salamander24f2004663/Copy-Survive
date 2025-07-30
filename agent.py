import os
import random
import time
import pyperclip
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk

# Characters to use (uppercase and lowercase only)
CHARACTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

# 10 Wikipedia pages only
URLS = [
    "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Computer_vision",
    "https://en.wikipedia.org/wiki/Neural_network",
    "https://en.wikipedia.org/wiki/Natural_language_processing",
    "https://en.wikipedia.org/wiki/Robotics",
    "https://en.wikipedia.org/wiki/Deep_learning",
    "https://en.wikipedia.org/wiki/Computer_science",
    "https://en.wikipedia.org/wiki/Turing_test"
]

# Game constants
TOTAL_ROUNDS = 10
LETTERS_FOLDER = "letters"  # Folder with A.png to z.png
RED_ZONES = 0


def show_letter_overlay(letter):
    """
    Display the target letter image in a floating window at the top center of the screen.
    """
    win = tk.Tk()
    win.title("Target Letter")
    win.attributes("-topmost", True)
    win.overrideredirect(True)  # No borders

    img_path = os.path.join(LETTERS_FOLDER, f"{letter}.png")
    if not os.path.exists(img_path):
        print(f"❗ Image for '{letter}' not found at {img_path}")
        win.destroy()
        return

    # Load and resize the image
    img = Image.open(img_path).resize((150, 150))
    tk_img = ImageTk.PhotoImage(img)

    # Position window at top center
    screen_width = win.winfo_screenwidth()
    x = int((screen_width - 180) / 2)
    win.geometry(f"180x180+{x}+20")

    label = tk.Label(win, image=tk_img)
    label.pack()

    win.after(15000, win.destroy)  # Close after 15 seconds
    win.mainloop()


def run_game():
    global RED_ZONES
    round = 0
    results = []

    print("🎮 COPY & SURVIVE: The Game Begins!")
    print("Instructions:")
    print("- A random Wikipedia page opens.")
    print("- A letter appears at the top (non-copyable PNG).")
    print("- You must find and copy that letter from the webpage (case-insensitive).")
    print("- If correct: ✅; if wrong: 🟥")
    print("- Survive 10 rounds to win!\n")

    # Countdown before game starts
    print("⏳ Get ready!")
    for i in range(10, 0, -1):
        print(f"⏳ Game starts in: {i} seconds...", end="\r", flush=True)
        time.sleep(1)
    print("🚀 GO!                                       \n")

    while round < TOTAL_ROUNDS and RED_ZONES < TOTAL_ROUNDS:
        round += 1
        target = random.choice(CHARACTERS)
        site = random.choice(URLS)

        print(f"\n📢 Round {round}/{TOTAL_ROUNDS}")
        print(f"🔒 Letter to copy (shown in image): {target}")
        print(f"🌐 Opening site: {site}")
        webbrowser.open(site)

        show_letter_overlay(target)

        clipboard = pyperclip.paste().strip()

        if clipboard.lower() == target.lower():
            print("✅ Correct!")
            results.append(True)
        else:
            RED_ZONES += 1
            print(f"❌ Incorrect! You copied '{clipboard}' instead of '{target}'")
            results.append(False)

        # Progress bar
        progress = ""
        for i in range(round):
            progress += "✅" if results[i] else "🟥"
        progress += "⬛" * (TOTAL_ROUNDS - round)
        print(progress)

        time.sleep(1)

    # Final message
    if RED_ZONES >= TOTAL_ROUNDS:
        print("\n🟥 GAME OVER: Too many incorrect attempts!")
    else:
        print("\n🎉 YOU WIN! You survived Copy & Survive🎉🎉!")


if __name__ == "__main__":
    run_game()
