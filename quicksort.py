def swap(the_list, a, b):
    # Swaps the two values in the_list at indices a and b.
    temp = the_list[a]
    the_list[a] = the_list[b]
    the_list[b] = temp

def partition(the_list, p, r, compare_func):
    # Partition function.
    pivot = the_list[r]
    i = p-1
    j = p
    for k  in xrange(p, r):
        if(j >= r):
            break
        if(compare_func(the_list[k], pivot)):
            i += 1
            swap(the_list, i, j)
        j += 1
    swap(the_list, i+1, r)
    return i+1

def quicksort(the_list, p, r, compare_func):
    if(p >= r): # base case
        return
    q = partition(the_list, p, r, compare_func)
    quicksort(the_list, p, q-1, compare_func)
    quicksort(the_list, q+1, r, compare_func)

def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
