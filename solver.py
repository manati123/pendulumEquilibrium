from utils import *
# -*- coding: utf-8 -*-
# """
# In this file your task is to write the solver function!

# """
# def solver(theta: float,omega: float):
#     """
#     Parameters
#     ----------
#     t : TYPE: float
#         DESCRIPTION: the angle theta
#     w : TYPE: float
#         DESCRIPTION: the angular speed omega

#     Returns
#     -------
#     F : TYPE: float
#         DESCRIPTION: the force that must be applied to the cart
#     or
    
#     None :if we have a division by zero

#     """    
#     return None




def fuzzify(x, left, middle, right):
    #calculate the values based on theta and the values in the corresponding dictionaries
    if left is not None and left <= x < middle:
        return (x - left) / (middle - left)
    elif right is not None and middle <= x < right:
        return (right - x) / (right - middle)
    elif left is None and x <= middle:
        return 1
    elif right is None and x >= middle:
        return 1
    else:
        return 0

def compute_values(value, ranges):
    to_return = dict()
    for key in ranges:#the keys in the theta_ranges and omega_ranges imported from utils.py
        to_return[key] = fuzzify(value, ranges[key][0],ranges[key][1],ranges[key][2])#keep the values computed in the fuzzyfy() function and add them to the corresponding keys
    return to_return
def solver(theta, omega):#give the theta and omega values and the corresponding dictionaries to the value calculator
    theta_values = compute_values(theta, theta_ranges)
    omega_values = compute_values(omega, omega_ranges)
    f_values = dict()
    for theta_key in fuzzy_table:
        for omega_key, f_value in fuzzy_table[theta_key].items():#take the corresponding values from the fuzzy table(keys and values)
            value = min(theta_values[theta_key], omega_values[omega_key])
            if f_value not in f_values:
                f_values[f_value] = value#add new value to the f_values
            else:
                f_values[f_value] = max(value, f_values[f_value])#if the value is already there keep only the max value
    s = sum(f_values.values())
    if s == 0:
        return None
    return sum(f_values[fSet] * bValues[fSet] for fSet in f_values.keys()) / s#that very confusing equation from the pdf
