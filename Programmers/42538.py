# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    total = 0
    bridge = []
    
    while truck_weights or bridge:

        time += 1

        bridge = [[b[0],b[1]+1] for b in bridge if b[1]+1<bridge_length]

        if truck_weights:
            if sum([b[0] for b in bridge]) + truck_weights[0] <= weight:
                bridge.append([truck_weights.pop(0), 0])  

    return time