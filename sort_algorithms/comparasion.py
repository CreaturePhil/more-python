from timeit import Timer
import random
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows
init()

alist = random.sample(xrange(100), 10)
lists = {}
for i in range(1, 10):
  lists[i] = alist[:]

t1 = Timer("bubbleSort(lists[1])", "from bubblesort import bubbleSort\nfrom __main__ import lists")
t2 = Timer("shortBubbleSort(lists[2])", "from bubblesort import shortBubbleSort\nfrom __main__ import lists")
t3 = Timer("selectionSort(lists[3])", "from selectionsort import selectionSort\nfrom __main__ import lists")
t4 = Timer("insertionSort(lists[4])", "from insertionsort import insertionSort\nfrom __main__ import lists")
t5 = Timer("mergeSort(lists[5])", "from mergesort import mergeSort\nfrom __main__ import lists")
t6 = Timer("quickSort(lists[6])", "from quicksort import quickSort, quickSortHelper, partition\nfrom __main__ import lists")

print colored(alist, "red")
print "---" * 10
print colored("Bubble Sort:", "blue", "on_white"), colored(t1.timeit(1000), "green", "on_red"), colored("ms", "cyan")
print colored("Short Bubble Sort:", "blue", "on_white"), colored(t2.timeit(1000), "green", "on_red"), colored("ms", "cyan")
print colored("Selection Sort:", "blue", "on_white"), colored(t3.timeit(1000), "green", "on_red"), colored("ms", "cyan")
print colored("Insertion Sort:", "blue", "on_white"), colored(t4.timeit(1000), "green", "on_red"), colored("ms", "cyan")
print colored("Merge Sort:", "blue", "on_white"), colored(t5.timeit(1000), "green", "on_red"), colored("ms", "cyan")
print colored("Quick Sort:", "blue", "on_white"), colored(t6.timeit(1000), "green", "on_red"), colored("ms", "cyan")
