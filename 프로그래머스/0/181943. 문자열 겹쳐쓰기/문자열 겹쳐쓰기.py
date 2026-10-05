def solution(my_string, overwrite_string, s):
    a = my_string[0:s]
    b = len(overwrite_string)
    c = my_string[s+b:]
    answer = a+overwrite_string+c
    return answer