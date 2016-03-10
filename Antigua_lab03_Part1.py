#Enmanuel Antigua
        #Lab 03

                                        #2.1
dna= "ACTGAC"

#Replacing of all the letters
dna = dna.replace("A","B")

dna= dna.replace("T","A")

dna= dna.replace("B","T")

dna= dna.replace("C","G")

print(dna)

                                        #2.2
dna= "ACTGAC"
#here, im printig the dna string backwards 
dna[::-1]
print(dna)

                                        #2.3
#for this part im making sure i have the valid Characters [A,G,T,C] 
dna= "ACTGAC"

chars = set('AGCT')

if all((c in chars) for c in dna):
    print('VALID')
else:
    print('INVALID')

                                        #2.4
dna1= "ACTGAC"
dna2= "CAGTCA"

#check characters on both dna strings

if all((c in chars) for c in dna1):
    print('VALID')
else:
    print('INVALID')

if all((c in chars) for c in dna2):
    print('VALID')
else:
    print('INVALID')

#finding out if the're equal to eachother
if dna1 == dna2 :
    print ("Match")
else:
    print("Do not Match")
        
                        #reverse

#this part is where I reverse and check if they match

dna1= "ACTGAC"
dna2= "CAGTCA"

if dna1[::-1] == dna2 :
    print("Match")
else:
    print("Do not match")

                        #mirror

#this part is where I mirror and check if they match

dna1= "ACTGAC"
dna2= "CAGTCA"

def mirror(s):
    s = s[:len(s)//2]                
    return s + ''.join(reversed(s))  
    
print (mirror(dna1))

if (mirror(dna1))== dna2 :
    print ("Match")
else:
    print ("Do not match")
        
    
                        #reverse-mirror

#this part is where I actually reverse and mirror the dna strings and check if they match

dna1= "ACTGAC"
dna2= "CAGTCA"

dna1_reversed = dna1[::-1]
print (mirror(dna1_reversed))

if mirror(dna1_reversed)== dna2:
    print ("Match")
else:
    print ("Do not match")

            
