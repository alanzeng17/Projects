
print "Find the next prime! Enter any key to continue, or type STOP to stop."
curr_prime = 1
flag = True
while flag:
    nextVal = raw_input()
    if nextVal != "STOP":
        fin = False
        while fin == False:           
            found = True
            curr_prime +=1 
            for i in range (2,curr_prime):
                if curr_prime % i == 0:
                    found = False
            fin = found
        print curr_prime
    else:
        flag = False
print "Find prime exiting."
            
                
                    
