import random

def vacuum_cleaner():
    rooms = {'A': random.choice(['Clean', 'Dirty']),
             'B': random.choice(['Clean', 'Dirty'])}
    
    current_loc = random.choice(['A', 'B'])
    
    print("Initial States:", rooms)
    print("Vacuum cleaner starting at Room", current_loc)
    print("----Cleaning Process----")

    while True:
        print(f"\nVacuum is in Room {current_loc} | Status: {rooms[current_loc]}")

        if rooms[current_loc] == 'Dirty':
            print(f"Action: Suck the dirt in room {current_loc}")
            rooms[current_loc] = 'Clean'
        else:
            if current_loc == 'A':
                print("Action: Move right to room B")
                current_loc = 'B'
            else:
                print("Action: Move left to room A")
                current_loc = 'A'

        if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
            print("Both the rooms are clean!")
            print("Final Status:", rooms)
            break

vacuum_cleaner()
