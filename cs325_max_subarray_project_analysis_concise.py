from math import ceil
from time import clock, ctime
import random

def alg1(ar):
    max_subarray_sum = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            cur_subarray_sum = 0
            for k in range(i, j+1):
                cur_subarray_sum += ar[k]
                if cur_subarray_sum > max_subarray_sum:
                    max_subarray_sum = cur_subarray_sum
    return max_subarray_sum

def alg2(ar):
    max_subarray_sum = 0
    for i in range(len(ar)):
        cur_subarray_sum = ar[i]
        if cur_subarray_sum > max_subarray_sum:
            max_subarray_sum = cur_subarray_sum
        for j in range(i+1, len(ar)):
            cur_subarray_sum += ar[j]
            if cur_subarray_sum > max_subarray_sum:
                max_subarray_sum = cur_subarray_sum
        
    return max_subarray_sum

def alg3(ar):
    #if array has 1 element, return value of that element
    if len(ar) == 1: return ar[0]
    
    #split array in half
    array_a = ar[:int(ceil(len(ar)/2))]
    array_b = ar[int(len(ar))/2:]

    #get max from part a
    array_a_max = alg3(array_a)

    #get max from part b
    array_b_max = alg3(array_b)

    #find max suffix in a
    array_a_suffix_max = 0
    array_a_cur_max = 0
    for i in reversed(array_a):
        array_a_cur_max += i
        if array_a_cur_max > array_a_suffix_max:
            array_a_suffix_max = array_a_cur_max

    #find max prefix in b
    array_b_prefix_max = 0
    array_b_cur_max = 0
    for i in array_b:
        array_b_cur_max += i
        if array_b_cur_max > array_b_prefix_max:
            array_b_prefix_max = array_b_cur_max

    #combine suffix and prefix
    array_combined_max = array_a_suffix_max + array_b_prefix_max

    #return the max
    return max(array_a_max, array_b_max, array_combined_max)

    

if __name__== '__main__':

    # create random arrays
    random.seed()
    ar1  = [random.randint(-500,500) for x in xrange(100)]
    ar2  = [random.randint(-500,500) for x in xrange(200)]
    ar3  = [random.randint(-500,500) for x in xrange(300)]
    ar4  = [random.randint(-500,500) for x in xrange(400)]
    ar5  = [random.randint(-500,500) for x in xrange(500)]
    ar6  = [random.randint(-500,500) for x in xrange(600)]
    ar7  = [random.randint(-500,500) for x in xrange(700)]
    ar8  = [random.randint(-500,500) for x in xrange(800)]
    ar9  = [random.randint(-500,500) for x in xrange(900)]
    ar10 = [random.randint(-500,500) for x in xrange(1000)]
    ar11 = [random.randint(-500,500) for x in xrange(2000)]
    ar12 = [random.randint(-500,500) for x in xrange(3000)]
    ar13 = [random.randint(-500,500) for x in xrange(4000)]
    ar14 = [random.randint(-500,500) for x in xrange(5000)]
    ar15 = [random.randint(-500,500) for x in xrange(6000)]
    ar16 = [random.randint(-500,500) for x in xrange(7000)]
    ar17 = [random.randint(-500,500) for x in xrange(8000)]
    ar18 = [random.randint(-500,500) for x in xrange(9000)]
    
    ar = [ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9]
    ar2 = [ar10,ar11,ar12,ar13,ar14,ar15,ar16,ar17,ar18]
    
    #testing variables
    runs_per_group = 10
    
    #run algorithm 1            
    print "Testing Algorithm 1\n-------------------------------"
    for a in (ar):
        print "\tSize %d:\t"%len(a),
        total_runtime = 0
        for i in xrange(runs_per_group):
            t = clock()
            alg1(a)
            t = clock()-t
            total_runtime += t
        print "%d ms"%(total_runtime/runs_per_group*1000)

    #add additional test arrays
    ar.extend(ar2)
    
    #run algorithm 2
    print "\nTesting Algorithm 2\n-------------------------------"
    for a in (ar):
        print "\tSize %d:\t"%len(a),
        total_runtime = 0
        for i in xrange(runs_per_group):
            t = clock()
            alg2(a)
            t = clock()-t
            total_runtime += t
        print "%d ms"%(total_runtime/runs_per_group*1000)

        
    #run algorithm 3
    print "\nTesting Algorithm 3\n-------------------------------"
    for a in (ar):
        print "\tSize %d:\t"%len(a),
        total_runtime = 0
        for i in xrange(runs_per_group):
            t = clock()
            alg3(a)
            t = clock()-t
            total_runtime += t
        print "%d ms"%(total_runtime/runs_per_group*1000)

