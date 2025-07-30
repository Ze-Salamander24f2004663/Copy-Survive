
# 🕹️ Copy & Survive

An interactive clipboard-based survival game built with **Python + Tkinter**, designed for the **Orgo AI Agents Hackathon**.

---

## 🎮 Game Concept

- The agent opens a **random Wikipedia page**.
- A random **letter** is displayed as a **non-copyable PNG image** at the **top center** of the screen.
- You have **15 seconds** to copy that exact letter (case-insensitive) from the open webpage.
- The agent checks your clipboard:
  - ✅ If correct: you survive the round.
  - 🟥 If incorrect: one red tile appears.
- There are **10 rounds** in total — survive all to win!

---

## 📁 Folder Structure

```
Copy-Survive/
├── agent.py               # Main game logic
├── requirements.txt       # Install dependencies
├── letters/               # All letter images (A-Z, a-z)
│   ├── A.png
│   ├── B.png
│   └── ...
```

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/Ze-Salamander24f2004663/Copy-Survive.git
cd Copy-Survive
```

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python agent.py
```

---

## 📦 Requirements

- Python 3.10+
- `pyperclip`
- `Pillow`
- `tkinter` (built-in)

---

## 🧠 Built For

**Orgo AI Agents Hackathon**  
Focus: Combining agent tools with human-computer interaction in a fun way.

---

## 📜 License

MIT License – Free to use, modify, and share.

---

## 🌐 Author

**Ze Salamander**  
[GitHub](https://github.com/Ze-Salamander24f2004663)
