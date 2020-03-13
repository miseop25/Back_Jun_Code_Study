import collections

def solution(bridge_length, weight, truck_weights):
    answer = 1
    time_input = collections.deque()
    on_the_bridge = collections.deque()
    truck_deq = collections.deque(truck_weights)

    on_the_bridge.append(truck_deq.popleft())
    time_input.append(answer)
    while True :
        if truck_deq or on_the_bridge :
            answer +=1
        else :
            break

        if ((answer - time_input[0]) == bridge_length):
            on_the_bridge.popleft()
            time_input.popleft()

        try : 
            if (truck_deq[0] + sum(on_the_bridge) <= weight ) :
                on_the_bridge.append(truck_deq.popleft())
                time_input.append(answer)

        except :
            pass

    return answer