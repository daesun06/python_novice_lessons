# Dummy calculation 

number1 = 7
number2 = 5

def calculate(input1, input2, symbol): 
    computation_string = f'{input1} {symbol} {input2}'
    result = eval(computation_string)
    return result 


calculation_1 = calculate(number1, number2, "+")
calculation_2 = calculate(number1, number2, "*")

print(calculation_1)
print(calculation_2) 