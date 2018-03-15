'''
Time Complexity:
'''
dict = {0:'S', 1:'D', 2:'A_1' , 3:'A_2'}
def tower_of_hanoi(num_rings, from_tower, dest_tower, aux_tower_1, aux_tower_2):
    if num_rings == 0:
        return
    if num_rings ==1:
        towers[dest_tower].append(towers[from_tower].pop())
        print("Moved ", towers[dest_tower][-1], " from ", dict[from_tower], " to", dict[dest_tower])
        return

    tower_of_hanoi(num_rings - 2,from_tower , aux_tower_1, aux_tower_2, dest_tower)

    #move 2nd last ring to 2nd auxiliary tower
    towers[aux_tower_2].append(towers[from_tower].pop())
    print("Moved ", towers[aux_tower_2][-1], " from ", dict[from_tower], " to", dict[aux_tower_2])

    #move last ring to 2nd dest tower
    towers[dest_tower].append(towers[from_tower].pop())
    print("Moved ", towers[dest_tower][-1], " from ", dict[from_tower], " to", dict[dest_tower])

    # move 2nd last ring to destination tower
    towers[dest_tower].append(towers[aux_tower_2].pop())
    print("Moved ", towers[dest_tower][-1], " from ", dict[aux_tower_2], " to", dict[dest_tower])


    tower_of_hanoi(num_rings - 2, aux_tower_1, dest_tower, aux_tower_2, from_tower)



#initialize towers and rings
num_towers = 4
num_rings =5
init_tower = [ring for ring in range(num_rings,0,-1)]
other_towers = [[] for tower in range(num_towers-1)]
towers = [init_tower] + other_towers
print("Before movement:")
print(towers)

print("\nSteps in movement:")
print("S: Source, A:Auxiliary, D:Destination")
tower_of_hanoi(num_rings, 0,1,2,3)

print("\nAfter movement:")
print(towers)

