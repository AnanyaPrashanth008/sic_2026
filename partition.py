def partition_array(numbers):
    numbers = []
    pivot = numbers[-1] #assign last element as reference element
    i = 0 #to access the elements in the list
    j = 0 #to find the inde of the pivot element

    for i in range(len(numbers) - 1):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1

    numbers[-1], numbers[j] = numbers[j], numbers[-1]