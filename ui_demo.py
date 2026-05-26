people = [(1, 'Alice', 0, 'New York', 30),
          (2, 'Bob', 1, 'Los Angeles', 25),
          (3, 'Charlie', 1, 'Chicago', 35),
          (4, 'Diana', 0, 'Houston', 28),
          (5, 'Eve', 0, 'Phoenix', 22)]

print('%-3s %-12s %-8s %-15s %-3s' %('ID','NAME','GENDER', 'LOCATION', 'AGE'))
print('-'*40)
gender = ''
for person in people:
    if person[2] == 0:
        gender = 'f'
    else:
        gender = 'm'
    print('%-3d %-12s  %-8s%-15s %-3d' %(person[0],person[1], gender, person[3], person[4]))
print('-'*40)