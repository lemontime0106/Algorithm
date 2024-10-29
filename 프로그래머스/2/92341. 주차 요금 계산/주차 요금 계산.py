from math import ceil

def solution(fees, records):
    answer = []
    basic_time, basic_fee, per_min, plus_fee = fees
    
    car = {}
    parking_time = {}
    
    for record in records:
        time, number, io = record.split()
        h, m = map(int, time.split(":"))
        time = h * 60 + m  
        
        if io == "IN":
            car[number] = time 
        elif io == "OUT":
            if number in parking_time:
                parking_time[number] += (time - car[number])
            else:
                parking_time[number] = time - car[number]
            del car[number] 

    for number, time in car.items():
        if number in parking_time:
            parking_time[number] += 1439 - time
        else:
            parking_time[number] = 1439 - time
    
    for number, time in sorted(parking_time.items(), key=lambda x: x[0]):
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            additional_fee = ceil((time - basic_time) / per_min) * plus_fee
            answer.append(basic_fee + additional_fee)
    
    return answer
