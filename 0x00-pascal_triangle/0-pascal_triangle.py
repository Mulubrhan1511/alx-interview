#!/usr/bin/python3
"""
pascal trinagle
"""


def pascal_triangle(n):
    my_list = []
    new_list = []
    for i in range(n):
        
        if i >= 2:
            for j in range(len(new_list)):
               print(i)
        else:
            
            if i> 0:
                new_list = []
                for j in range(i+1):
                    new_list.append(1)
            else:
                new_list = []
                new_list.append(1)
            if new_list:
                my_list.append(new_list)
        
    return my_list
print(pascal_triangle(5))