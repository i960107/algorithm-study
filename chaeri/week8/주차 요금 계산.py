import math

def solution(fees, records):
    parking = dict()
    stack = dict()
    last_time = 23 * 60 + 59
    answer=[]
    
    for record in records:
        time, car, check = record.split() #시간, 차 번호, IN/OUT
        time_list = list(map(int, time.split(':')))
        minutes = time_list[0]*60 + time_list[1] #분으로 바꿔줌
        
        if parking.get(car):
            if check == 'IN':
                parking[car].append(minutes) #in이면 입차
            elif check == 'OUT': #출차
                if stack.get(car):
                    stack[car] += minutes-(parking[car].pop())
                else:
                    stack[car] = minutes-(parking[car].pop())
        else:
            parking[car] = [minutes]
    
    #출차 안했을 때        
    for key,value in parking.items():
        if value:
            if stack.get(key): # 기록이 남아있다면 23:59분에 출차한 것으로 간주
                stack[key] += (last_time - value[0])
            else:
                stack[key] = (last_time - value[0])
    
    #계산 (문제 제공) 
    for key,value in sorted(stack.items()):
        if value > fees[0]:
            answer.append(fees[1] + math.ceil((value-fees[0])/fees[2])*fees[3]) #올림
        else:
            answer.append(fees[1])
    
    return answer