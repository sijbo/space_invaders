# Space Invaders – Dual Edition Arcade

A retro-inspired, fast-paced arcade shooter project featuring two distinct versions: a hyper-responsive **HTML5/JavaScript Mobile Edition** and a classic **Python/Pygame Desktop Edition**. Take control of a futuristic defense ship, dodge incoming enemy plasma, and eliminate waves of escalating alien invaders!

---

## 🎮 Repository Overview

This repository bridges two development ecosystems, providing the same classic gameplay tailored for different devices:

### 1. HTML5 Mobile Edition (`index.html`)
* **Platform:** Mobile Browsers (Safari, Chrome) & Desktop Browsers
* **Optimizations:** Uses a lightweight HTML5 Canvas API running at 60 FPS. Features smooth Linear Interpolation (Lerp) touch-dragging so the ship perfectly tracks your finger on touchscreens. Includes a retro CRT scanline overlay and particle physics explosions.

### 2. Python Desktop Edition (`main.py`)
* **Platform:** PC / Mac Terminal
* **Optimizations:** Built on the robust **Pygame** framework. Features unique custom vector-drawn art assets for three distinct alien tiers (*Crabs*, *Octopuses*, and *Squids*) and a randomized starfield backdrop.

---

## 🕹️ Controls & Gameplay

Both games feature dynamic wave scaling—clearing a stage automatically resets the grid with an increased speed modifier for endless progression.

### HTML5 Mobile Controls
* **Touch/Drag:** Move your finger anywhere on the screen to slide the ship.
* **Tap:** Tap or lift your finger to fire a laser pulse.

### Desktop Controls (Python & HTML5 Keyboard)
| Action           | Control Configuration                       |
| :--------------- | :------------------------------------------ |
| **Move Left**    | `Left Arrow Key` / `A`                      |
| **Move Right**   | `Right Arrow Key` / `D`                     |
| **Fire Laser**   | `Spacebar` (Limited active screen capacity) |
| **Restart Game** | `Spacebar` or `R` (On Game Over screen)     |

---

## 🛠️ Installation & Setup

### How to play the Mobile/Web Version
No installation required! 
1. Open the `index.html` file directly in any desktop browser, or send it to your mobile phone and open it via **Safari** or **Chrome**.
2. Alternatively, you can copy the code and paste it into a web sandbox like [CodePen](https://codepen.io/) to play instantly.

### How to play the Desktop Python Version
Make sure you have **Python 3.x** installed on your system.

1. Install the Pygame framework using your terminal:
   ```bash
   pip install pygame