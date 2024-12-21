import os

def make_dirs():
    day = 11
    for i in range(6, 26):
        dir_name = f"day0{i}" if i < 10 else f"day{i}"
    
        os.makedirs(dir_name, exist_ok=True)
        
        with open(f"{dir_name}/aoc{day}-{day+1}.txt", "w") as f:
            pass
        with open(f"{dir_name}/aoc{day}.py", "w") as f:
            pass
        with open(f"{dir_name}/aoc{day+1}.py", "w") as f:
            pass
        day += 2

if __name__ == "__main__":
    make_dirs()

            
