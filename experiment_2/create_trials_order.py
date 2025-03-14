import sys
import itertools 

import numpy as np
from itertools import chain


def main():
    list_a = list(chain.from_iterable(itertools.combinations('ABCDE', 2)))
    #a = [list_a[::2],list_a[1::2]]
    
    list_b = []
    for x in range(0,len(list_a)-1,2):
        list_b.append(list_a[x] + list_a[x+1])

    list_a_perm = list(chain.from_iterable(itertools.combinations('BACDE', 2)))

    list_b_perm = []
    for x in range(0,len(list_a_perm)-1,2):
        list_b_perm.append(list_a_perm[x] + list_a_perm[x+1])
    
    list_b = np.tile(list_b,3)
    list_b_perm = np.tile(list_b_perm,3)
    final = np.concatenate((list_b, list_b_perm), axis = 0 )
    np.random.shuffle(final)
    print(final)
    #from itertools import combinations 
    #
    #combinations('ABCDE', 2)



if __name__ == '__main__':
    main() 
    sys.exit(0)
