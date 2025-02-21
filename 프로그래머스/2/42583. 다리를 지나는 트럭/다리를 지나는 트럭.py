from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0 

    while truck_weights or current_weight > 0:
        time += 1
        exited_truck = bridge.popleft()
        current_weight -= exited_truck

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                bridge.append(0)

    return time
