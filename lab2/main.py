#!/usr/bin/env python3

import sys

def string_to_numeric(count, str):
    index=0;
    pw=pow(10, count-1)
    res=0
    while str[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        res+=pw*int(str[index])
        pw=pw/10
        index=index+1
    return res

def get_string_length(str):
    index=0
    count=0
	
    if(str[index] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        return -1, count
    while(str[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        count=count+1
        index=index+1
    if(str[index]!='k'):
        return -1, count
    num=string_to_numeric(count, str)
    return num, count

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.':
                length, count=get_string_length(format_string[idx+2:])
                length=int(length)
                if length>0:
            	    print(param[:int(length)].swapcase(), end="")
                shouldDo=False
                print(format_string[idx+3+count:],end="")
                break
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
