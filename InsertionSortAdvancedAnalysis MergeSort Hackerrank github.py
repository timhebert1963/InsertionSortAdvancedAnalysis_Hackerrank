# Hankerrank documentation for Insertion Sort Advanced Analysis
# 
# https://www.hackerrank.com/challenges/insertion-sort/problem
#
# the requirement is to count and return the shifts/inversions it would take to sort the array
# and not necessarily end up with a sorted array. 
#  - the program does not have to return the sorted array.

import time

class Shifts():
    def __init__(self):
        self.inv = 0

def getHalves(A, l):
    mid = l // 2
    lhalf, rhalf = A[:mid], A[mid:] 
    return lhalf, rhalf

def countInversions(lhalf, lhalf_sz, rhalf, rhalf_sz, shifts):

    lhalf.sort()
    rhalf.sort()
    i, j = 0, 0

    while i < lhalf_sz:
        while j < rhalf_sz:

            if lhalf[i] > rhalf[j]:
                shifts.inv += lhalf_sz - i
                j += 1
            else:
                break

        i += 1

def mergeSort(A, shifts):
    
    A_sz = len(A)

    if A_sz > 1:
        lhalf, rhalf = getHalves(A, A_sz)
        lhalf_sz, rhalf_sz = len(lhalf), len(rhalf)
        
        mergeSort(lhalf, shifts)
        mergeSort(rhalf, shifts)

        countInversions(lhalf, lhalf_sz, rhalf, rhalf_sz, shifts)

def insertionSort(arr):
    shifts = Shifts()
    mergeSort(arr, shifts)
    return shifts.inv

def getTime():
    return int(time.time())

def convertSeconds(s):
    return s // 60, s % 60  # minutes = s // 60, seconds = s % 60

def testResults(test, inversions, expected, start_time):
    
    end_time = getTime()
    seconds = end_time - start_time
    minutes, seconds = convertSeconds(seconds)

    if expected == inversions:
        status = 'PASS'
    else:
        status = 'FAIL'

    print('\n')
    print("{} number of inversions  == {}  expected result == {}   {}\n".format(test, inversions, expected, status))
    print("{} total time to execute == {:2d} minutes {:2d} seconds".format(test, minutes, seconds))
    print('\n')

def main():
    
    #######################################################################################################
    #
    # Some tests to pass on Hackerrank for Insertion Sort Advanced Analysis inlcuded as a demo listed below.
    #
    # TC2_1_length_441_answer_46768.py and TC2_2_length_18_answer_77.py need to be imported as in the for
    # loop below.
    #
    #######################################################################################################


    test_case_list = ['TC2_1', 'TC2_2']

    for test in test_case_list:

        if test == 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            expected = 46768

        elif test == 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            expected = 77

        start_time = getTime()
        
        inversions = insertionSort(arr)

        testResults(test, inversions, expected, start_time)

if __name__ == '__main__':
    main()