import math

def solution(fees, records):
    answer = []
    
    parking = []
    car_fee = {}
    
    # Record using stack and hash
    for string in records:
        temp = string.split()
        time = int(temp[0][:2])*60 + int(temp[0][3:])
        if temp[2] == "IN":
            parking.append((temp[1],time))
            if temp[1] not in car_fee:
                car_fee[temp[1]] = 0
        else:
            for car in parking:
                if car[0] == temp[1]:
                    time_gap = time - car[1]
                    car_fee[temp[1]] += time_gap
                    parking.remove(car)
                    break
    
    # Remain car at 23:59 (1439)
    for car in parking:
        time_gap = 1439 - car[1]
        car_fee[car[0]] += time_gap
    
    # Fee calculation
    temp_L = []
    for key in car_fee:
        if car_fee[key] <= fees[0] :
            temp_L.append([key, fees[1]])
        else:
            fee = fees[1] + math.ceil((car_fee[key] - fees[0])/fees[2])*fees[3]
            temp_L.append([key, fee])
    
    # Result
    temp_L.sort()
    for car_num, fee in temp_L:
        answer.append(fee)
    
    return answer
