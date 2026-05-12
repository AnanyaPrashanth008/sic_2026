import quick_sort as qs
import sys

numbers = []


numbers = [int(value) for value in sys.argv[1:]]

print('Numbers before Sorting:\n', numbers)
qs.quick_sort(numbers, 0, len(numbers) - 1)
print('Numbers after Sorting:\n', numbers)
