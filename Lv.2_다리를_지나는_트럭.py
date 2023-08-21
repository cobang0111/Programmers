def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = []
    on_bridge_w = 0
    
    while truck_weights:
        # Case : Empty Bridge
        if on_bridge_w == 0:
            cur = truck_weights.pop(0)
            on_bridge.append([cur,0])
            on_bridge_w += cur
        # Case : Bridge can accept more truck
        elif on_bridge_w + truck_weights[0] <= weight:
            cur = truck_weights.pop(0)
            on_bridge.append([cur,0])
            on_bridge_w += cur
        # Truck location count
        for i in range(len(on_bridge)):
            on_bridge[i][1] += 1
        # Case : First truck get out from bridge
        if on_bridge[0][1] >= bridge_length:
            on_bridge_w -= on_bridge[0][0]
            on_bridge.pop(0)
        # Time count
        answer += 1
    
    # Add the Time that Last Truck get out from bridge 
    answer += bridge_length - on_bridge[-1][1] + 1
    return answer
