# Space Invaders Clustered

A sleek, retro-inspired arcade shooter built in Python using the **Pygame** framework. Take control of a futuristic defense ship, dodge incoming enemy plasma, and eliminate waves of escalating alien invaders!

---

## 🚀 Features

* **Dynamic Wave Scaling:** Clearing a wave automatically resets the grid with an increased speed modifier for endless progression.
* **Procedural Retro Sprites:** Features custom vector-drawn art layers for the Player Ship and three distinct types of alien configurations (*Crabs*, *Octopuses*, and *Squids*).
* **Layered Score Engine:** Destroying higher-tier alien units rewards the player with progressively scaling points.
* **Ammo Limitations:** Balance your offensive output with a maximum cap of 3 active friendly projectiles on-screen at once.
* **Atmospheric Starfield:** Includes an integrated parallax particle backdrop to simulate high-speed interstellar movement.

---

## 🎮 Controls

The game utilizes straightforward keyboard configurations designed for instant accessibility:

| Action           | Control Configuration                 |
| :--------------- | :------------------------------------ |
| **Move Left**    | `Left Arrow Key` / `A`                |
| **Move Right**   | `Right Arrow Key` / `D`               |
| **Fire Laser**   | `Spacebar` (Max 3 on screen)          |
| **Restart Game** | `Spacebar` (Only on Game Over Screen) |

---

## 🛠️ Installation & Setup

Follow these steps to configure your local environment and boot up the game application:

### Prerequisites
Make sure you have **Python 3.x** installed on your operating system. If you don't have Pygame installed yet, run the following pipeline package manager command in your terminal:

```bash
pip install pygame