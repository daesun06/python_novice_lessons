FILE_PATH = '/Users/daesun_m/sonarsweep/input.txt'

input_list = []

# TODO : read about with construct and open function in python - summarize in few sentences.

with open(FILE_PATH) as file:
    lines = file.readlines()
    input_list = [int(line.strip()) for line in lines]


def sonar_sweep(input):
    answer = 0
    prev = input[0]
    
    for index in range(1, len(input)):
        cur = input[index]
        if cur > prev:
            answer += 1 
        prev = cur 
        
    return answer

print(sonar_sweep(input_list))