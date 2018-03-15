'''
Variant2: Contraint, each movement must involve aux_tower

PATTERN:

for i = 1 to total number of moves:
    if i==Odd
	    legal movement of top disk between source pole and auxiliary pole
    if i== Even:
	    legal movement of top disk between destination pole and auxiliary pole
'''

dict = {0:'S', 1:'D', 2:'A'}
def tower_of_hanoi(num_rings, src_tower, dest_tower, aux_tower):
    if num_rings==0:
        return
    move=0
    while(len(towers[dest_tower])<num_rings):
        move += 1
        if move%2==1:
            legal_move_ring(src_tower, aux_tower)
        else:
            legal_move_ring(dest_tower, aux_tower)

    print("Total minimum number of required moves = ",move)

def legal_move_ring(tower_1, tower_2):
    #both towers cannot be empty at same time
    if not towers[tower_2]: #if tower_2 is empty
        from_tower = tower_1
        to_tower = tower_2
    elif not towers[tower_1]: #if tower_1 is empty
        from_tower = tower_2
        to_tower = tower_1
    else:
        (from_tower, to_tower) = (tower_1, tower_2) \
            if towers[tower_1][-1] < towers[tower_2][-1] else (tower_2, tower_1)

    ring = towers[from_tower].pop()
    towers[to_tower].append(ring)
    print("Moved ", ring, " from ", dict[from_tower], " to", dict[to_tower])


#initialize towers and rings
num_towers = 3
num_rings =2
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


