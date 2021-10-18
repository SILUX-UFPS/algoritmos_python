from typing import Union
#required python >= 3.9

"""
print the data inside the list
names parameter must be a list of string

"""
def show_info(names:list[str]):
    for name in names:
        print(name)

""""
multiply each number in the list by the multipler a return a list with result
nums parameter must be a list of integers
"""
def multiply_numbers(nums:list[int], multiplier:int)->list[int]:
    results:list[int] = []
    for num in nums:
        results.append(num*multiplier)
    return results

"""
this function applies the divide operation but the parameter could be of multiple types, 
using Union typing for example, the dividend could be int or float
"""
def divide(dividend:Union[int,float], divisor:Union[int,float])->Union[str,int,float]:
    if divisor==0:
        return "Error, divisor cannot be 0"
    return dividend/divisor

show_info(names=["Jhon","George","Daniel"])

print(multiply_numbers(nums=[2,4,6,8],multiplier=3))

print(divide(4.5,4))