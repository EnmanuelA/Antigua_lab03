#Enmanuel Antigua
        #Lab03_Part2

                                #3.1
#dna strings
dna1= "CAGCTCAAGCCTAGTACTAGCAGTT"
dna2= "AGGCTCAAGCATAGCTCCATGCGTTCAAG"
#measure the length of both strings
len1 = len(dna1)
len2 = len(dna2)
count = 0

for i in range (0, min(len1, len2)) :
      if dna1[i] == dna2[i]: #whenever dna1 and dna2 match 
          count +=1 #add a 1 
print("The number of matches is", count)


