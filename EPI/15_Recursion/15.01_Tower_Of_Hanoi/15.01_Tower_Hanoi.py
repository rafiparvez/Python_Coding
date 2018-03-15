'''
Time Complexity:
O
'''
dict = {0:'S', 1:'D', 2:'A'}
def tower_of_hanoi(num_rings, from_tower, to_tower, using_tower):
    if num_rings == 0:
        return
    tower_of_hanoi(num_rings - 1,from_tower , using_tower, to_tower)
    ring = towers[from_tower].pop()
    towers[to_tower].append(ring)
    print("Moved ", ring, " from ", dict[from_tower], " to", dict[to_tower])
    tower_of_hanoi(num_rings - 1, using_tower, to_tower, from_tower)



#initialize towers and rings
num_towers = 3
num_rings =4
init_tower = [ring for ring in range(num_rings,0,-1)]
other_towers = [[] for tower in range(num_towers-1)]
towers = [init_tower] + other_towers
print("Before movement:")
print(towers)

print("\nSteps in movement:")
print("S: Source, A:Auxiliary, D:Destination")
tower_of_hanoi(num_rings, 0,1,2)

print("\nAfter movement:")
print(towers)

