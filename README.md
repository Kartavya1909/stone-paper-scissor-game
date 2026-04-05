# ✂️ Rock Paper Scissors — Hand Gesture Game

A real-time Rock Paper Scissors game using your webcam. No keyboard or mouse needed — just show your hand gesture and play against the computer!

Built with Python, OpenCV, and MediaPipe.

---

## 📸 Demo

| Gesture | Hand Sign |
|---------|-----------|
| ✊ Rock | All fingers curled into a fist |
| 🖐️ Paper | All four fingers fully extended |
| ✌️ Scissors | Index and middle fingers extended |

---

## 🚀 Features

- Real-time hand gesture detection via webcam
- Accurate finger-state detection using MediaPipe landmarks
- Computer randomly picks its move every round
- 2-second cooldown between rounds (no freezing!)
- Live result display on the webcam feed

---

## 🛠️ Tech Stack

- **Python 3**
- **OpenCV** — webcam capture and display
- **MediaPipe** — hand landmark detection

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kartavya1909/stone-paper-scissor-game.git
   cd stone-paper-scissor-game
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python mediapipe
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

---

## 🎮 How to Play

1. Run the script — your webcam will open
2. Show one of the three hand gestures to the camera:
   - ✊ **Rock** — make a fist (all fingers curled)
   - 🖐️ **Paper** — open hand (all fingers extended)
   - ✌️ **Scissors** — extend only index and middle fingers
3. The computer picks its move randomly
4. The result is displayed on screen for 2 seconds
5. Press **`Q`** to quit

---

## 📁 Project Structure

```
stone-paper-scissor-game/
│
├── main.py       # Main game script
└── README.md     # Project documentation
```

---

## 🧠 How Gesture Detection Works

MediaPipe detects 21 hand landmarks in real time. To determine if a finger is extended, the Y-coordinate of the fingertip is compared to its MCP (knuckle base) joint — if the tip is higher on screen than the base, the finger is considered "up".

- **0 fingers up** → Rock
- **4 fingers up** → Paper
- **Index + Middle up only** → Scissors
- **Anything else** → Ignored (no round triggered)

---

## 📌 Requirements

- Python 3.7+
- A working webcam
- Good lighting for best gesture detection accuracy

---

## 👤 Author

**Kartavya** — [GitHub](https://github.com/Kartavya1909)
