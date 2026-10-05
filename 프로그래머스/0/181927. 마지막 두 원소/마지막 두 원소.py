def solution(num_list):
    answer = []
    a = len(num_list)
    if(num_list[a-1]>num_list[a-2]) :
        num_list.append(num_list[a-1]-num_list[a-2])
        answer = num_list
    else : 
        num_list.append(num_list[a-1]*2)
        answer = num_list
    return answer