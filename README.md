# 🏁 WEC Race Simulator – Endurance Racing in Your Terminal

A **race-focused, terminal-based World Endurance Championship (WEC) simulator** written in Python.  
This project recreates the chaos, strategy, and unpredictability of endurance racing — weather swings, safety cars, retirements, and multi-class battles — lap by lap.

Built for motorsport fans who care more about **race flow and realism** than flashy graphics.

---

## 🏎️ What This Simulator Is About

This is not just a random lap counter.

It simulates:
- Long-form **endurance racing**
- Multiple racing classes on the same track
- Race control decisions that change outcomes
- Attrition — not everyone finishes

Every run tells a *different race story*.

---

## 🔥 Core Racing Features

### 🏁 Multi‑Class Endurance Racing
Cars from different classes race **together**:
- **Hypercar**
- **LMP2**
- **GTE Pro**
- **GTE Am**
- **LMGT3 (Le Mans 2025)**

Each class has realistic lap-time ranges and performance gaps.

---

### 🌦️ Dynamic Weather System
Weather can change mid‑race:
- Clear
- Cloudy
- Light Rain
- Heavy Rain

Rain directly increases lap times and can shake up the leaderboard.

---

### 🚨 Race Control & Neutralisations
Race Control intervenes dynamically:
- **Safety Car (SC)** – field bunches up
- **Full Course Yellow (FCY)** – slow zones
- Automatic green‑flag restarts

Just like real endurance racing, timing is everything.

---

### 🔧 Mechanical Failures & Accidents
- Reliability-based mechanical DNFs
- Random on-track accidents
- Some cars may be marked as **immune** (never retire)

Endurance racing is about survival — not just speed.

---

### 🛠️ Pit Stops
Cars may pit randomly for:
- Fuel
- Tires

Pit timing can make or break a race.

---

### 📊 Live Race Information
- **Class leaders every lap**
- **Full leaderboard** every 10 laps
- Time gaps and laps-down calculations
- ANSI color-coded output per class

---

### 💾 Full Race Logging
Every event is logged:
- Lap times
- Weather changes
- Safety cars
- Retirements
- Final classification

Saved automatically as:
```
WEC_Race_YYYYMMDD_HHMMSS.txt
```

---

## 🖥️ Requirements

- Python **3.8+**
- No external libraries required

Uses only:
- `random`
- `time`
- `datetime`

---

## 📁 Project Structure

```
📦 wec-race-simulator
 ┣ 📜 WEC race simulator.py
 ┣ 📜 lemans2025_entries.py
 ┗ 📄 README.md
```

`lemans2025_entries.py` defines the grid and must include:
- Car name
- Class
- Driver
- Reliability value
- Optional `immune` flag

---

## ▶️ How to Run the Race

1. Download or clone the repository
2. Open a terminal in the project folder
3. Run:

```bash
python "WEC race simulator.py"
```

4. Choose race length:
```
Choose race length (6H or 24H):
```

- **6H** → 180 laps
- **24H** → 720 laps

Then sit back and watch the race unfold 🏁

---

## 🧠 Simulation Philosophy

This simulator prioritizes:
- Race narrative over perfection
- Unpredictability over determinism
- Endurance realism over arcade logic

No two races are ever the same.

---

## 🚀 Future Race Enhancements (Planned / Possible)

- Driver stints & fatigue
- Tire degradation models
- Fuel strategy
- Virtual Energy / hybrid deployment
- Championship mode
- Live timing UI or web dashboard

---

## 📜 License

Open-source and free to use.
Fork it. Break it. Improve it. Race it.

---

**Endurance racing isn’t about winning every lap —  
it’s about still running at the end.** 🏁
