people_waiting = int(input())
current_state = input().split(" ")
current_state = [int(i) for i in current_state]
counter = 0
for wagon in range(len(current_state)):
    if current_state[wagon] < 4:
        diff = 4 - current_state[wagon]
        if diff > people_waiting:
            diff = people_waiting
        current_state[wagon] += diff
        people_waiting -= diff
for wag in range(len(current_state)):
    if current_state[wag] == 4:
        counter += 1
current_state = [str(i) for i in current_state]
current_state_str = " ".join(current_state)
if counter == len(current_state) and people_waiting == 0:
    print(current_state_str)
elif people_waiting == 0 and counter < len(current_state):
    print(f"The lift has empty spots!\n{current_state_str}")
elif people_waiting > 0 and counter == len(current_state):
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{current_state_str}")
