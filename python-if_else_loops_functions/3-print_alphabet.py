#!/usr/bin/pthon3   
for i in range(ord('a'), ord('z')+1):                                                                        
    if i == ord('q') or i == ord('e'):
        continue
    printf("{:C}".format(i), end="")                                                                                          
