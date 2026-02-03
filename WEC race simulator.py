import random
import time
from datetime import datetime
from lemans2025_entries import cars


# Colors (simulated in terminal output)
CLASS_COLORS = {
    "Hypercar": "\033[91m",
    "LMP2": "\033[94m",
    "GTE Pro": "\033[92m",
    "GTE Am": "\033[93m",
    "LMGT3": "\033[92m",  # Added for Le Mans 2025 GT3
}

END_COLOR = "\033[0m"

# Weather and Race Control Flags
weather_conditions = ["Clear", "Cloudy", "Light Rain", "Heavy Rain"]
current_weather = random.choice(weather_conditions)
race_control = None
safety_car_laps = 0

# Lap time ranges (by class)
lap_time_ranges = {
    "Hypercar": (205, 215),
    "LMP2": (215, 225),
    "LMGT3": (250, 265), # Added for Le Mans GT3 cars
    "GTE Pro": (240, 250),
    "GTE Am": (250, 265),
}


# Store logs and retirements
race_log = []
retired_cars = []

def change_weather():
    global current_weather
    if random.random() < 0.08:
        current_weather = random.choice(weather_conditions)
        msg = f"⚠️ Weather change: {current_weather}"
        print(msg)
        race_log.append(msg)

def race_control_update():
    global race_control, safety_car_laps
    if race_control == "SC":
        safety_car_laps -= 1
        if safety_car_laps == 0:
            msg = "✅ Safety Car Ending: Green flag!"
            race_control = None
            print(msg)
            race_log.append(msg)
    elif random.random() < 0.02:  # 2% SC chance
        race_control = "SC"
        safety_car_laps = random.randint(3, 6)
        msg = "🚨 Safety Car Deployed! Field bunched up."
        print(msg)
        race_log.append(msg)
    elif random.random() < 0.05:  # 5% FCY chance
        race_control = "FCY"
        msg = "🚔 Full Course Yellow: Slow zones in effect!"
        print(msg)
        race_log.append(msg)
    elif race_control == "FCY" and random.random() < 0.2:
        msg = "✅ Full Course Yellow Ending: Green flag!"
        race_control = None
        print(msg)
        race_log.append(msg)

def pit_stop(car):
    msg = f"Lap {lap}: {car} pits for fuel and tires."
    print(msg)
    race_log.append(msg)

def accident(car):
    if cars[car].get("immune"):  # Immune cars never retire
        return False
    if random.random() < 0.00005:  # 0.005% chance per lap
        msg = f"Lap {lap}: {car} has an accident at Tertre Rouge!"
        print(msg)
        race_log.append(msg)
        if random.random() < 0.25:
            retire_msg = f"💥 {car} retires due to damage."
            print(retire_msg)
            race_log.append(retire_msg)
            retired_cars.append(car)
            del cars[car]
            return True
    return False

def mechanical_failure(car):
    if cars[car].get("immune"):  # Immune cars never retire
        return
    if random.random() > (cars[car]['reliability'] + 0.00005):  # Reliability margin
        msg = f"Lap {lap}: {car} suffers mechanical failure!"
        print(msg)
        race_log.append(msg)
        retired_cars.append(car)
        del cars[car]

def random_lap_time(car):
    cls = cars[car]['class']
    base_time = random.randint(*lap_time_ranges[cls])
    if "Rain" in current_weather:
        base_time += random.randint(5, 15)
    if race_control == "FCY":
        base_time += 20
    elif race_control == "SC":
        base_time += 40
    return base_time

def print_class_leaders():
    print("\n🏆 Class Leaders:")
    race_log.append("\n🏆 Class Leaders:")
    classes = ["Hypercar", "LMP2", "GTE Pro", "GTE Am"]
    for cls in classes:
        class_cars = {k: v for k, v in cars.items() if v['class'] == cls}
        if class_cars:
            leader = min(class_cars, key=lambda c: class_cars[c]["total_time"])
            t = class_cars[leader]["total_time"]
            color = CLASS_COLORS[cls]
            line = f"{color}  {cls}: {leader} ({cars[leader]['driver']}) - {t//60}m{t%60}s{END_COLOR}"
            print(line)
            race_log.append(line)
    print()

def print_full_leaderboard():
    print("\n📋 Full Leaderboard (gaps & laps down):")
    race_log.append("\n📋 Full Leaderboard (gaps & laps down):")
    leaderboard = sorted(cars.items(), key=lambda x: x[1]["total_time"])
    if not leaderboard:
        msg = "⚠️ All cars have retired from the race!"
        print(msg)
        race_log.append(msg)
        return
    leader_time = leaderboard[0][1]["total_time"]
    leader_laps = leaderboard[0][1]["laps"]
    
    for i, (car, data) in enumerate(leaderboard, start=1):
        diff_time = data["total_time"] - leader_time
        laps_diff = leader_laps - data["laps"]
        gap = "Leader" if diff_time == 0 else f"+{diff_time//60}m{diff_time%60}s" if laps_diff == 0 else f"-{laps_diff} Lap(s)"
        color = CLASS_COLORS[data['class']]
        line = f"{color}{i}. {car} ({data['class']}) - {data['driver']} - Lap {data['laps']} - {gap}{END_COLOR}"
        print(line)
        race_log.append(line)
    print()

def race_simulator(total_laps):
    global lap
    lap = 1
    for car in cars:
        cars[car]["total_time"] = 0
        cars[car]["laps"] = 0

    while lap <= total_laps and cars:
        change_weather()
        race_control_update()
        for car in list(cars.keys()):
            lap_time = random_lap_time(car)
            cars[car]["total_time"] += lap_time
            cars[car]["laps"] += 1
            update = f"Lap {lap}: {car} ({cars[car]['driver']}) - {lap_time//60}m{lap_time%60}s"
            print(update)
            race_log.append(update)

            if random.random() < 0.05: pit_stop(car)
            if accident(car): continue
            mechanical_failure(car)

        print_class_leaders()
        if lap % 10 == 0: print_full_leaderboard()
        lap += 1
        time.sleep(0.2)

    print("\n🏁 Race Finished!\n")
    print_full_leaderboard()
    save_results()

def save_results():
    filename = f"WEC_Race_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("🏁 WEC Race Results\n\n")
        for line in race_log:
            f.write(line + "\n")
        if retired_cars:
            f.write("\n💥 Retired Cars:\n")
            for car in retired_cars:
                f.write(f"- {car}\n")
    print(f"📁 Race results saved to '{filename}'.")

# Start Race
race_length = input("Choose race length (6H or 24H): ").strip().lower()
total_laps = 180 if race_length == "6h" else 720
print(f"\n🚦 Starting a {race_length.upper()} WEC race...\n")
race_simulator(total_laps)
