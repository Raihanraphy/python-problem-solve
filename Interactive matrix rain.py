import os, random, time

chars, speed = "01", 0.05
width = 80

try:
    while True:
        print("\033[92m" + ''.join(random.choice(chars) for _ in range(width)) + "\033[0m")
        time.sleep(speed)
        if random.random() < 0.05:  # Occasionally prompt
            cmd = input("\033[93mCommand [c=chars, s=speed, q=quit]: \033[0m")
            if cmd == "c": chars = input("New chars: ") or chars
            elif cmd == "s": speed = float(input("New speed (sec): ") or speed)
            elif cmd == "q": break
except KeyboardInterrupt:
    pass

os.system('cls' if os.name == 'nt' else 'clear')
print("💻 Matrix Simulation Ended")
