import numpy as np

array = np.array([    #column 0, with elements 0 to 2
                    [['A','B','C'],['D','E','F'],['G','H','I']],  #layer 0
                    [['J','K','L'],['M','N','O'],['P','Q','R']],
                    [['S','T','U'],['V','W','X'],['Y','Z',' ']]
])
 # Multidimensional indexing

print(f"{array[1,1,0]+array[0,0,0]+array[2,1,2]}")
word =array[1,1,0]+array[0,0,0]+array[2,1,2]
print(word)
