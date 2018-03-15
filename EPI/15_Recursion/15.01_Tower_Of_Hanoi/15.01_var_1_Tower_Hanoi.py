'''
var1: TERATIVE Tower of hanoi:
It can derived from observing pattern of movements in recursive algo.
Pattern:
When num_rings = Odd(3),
Steps in movement:
S: Source, A:Auxiliary, D:Destination
Moved  1  from  S  to D
Moved  2  from  S  to A
Moved  1  from  D  to A
Moved  3  from  S  to D
Moved  1  from  A  to S
Moved  2  from  A  to D
...
When num_rings = Even(4),
Steps in movement:
S: Source, A:Auxiliary, D:Destination
Moved  1  from  S  to A
Moved  2  from  S  to D
Moved  1  from  A  to D
Moved  3  from  S  to A
Moved  1  from  D  to S
Moved  2  from  D  to A
...

PATTERNS:
When num_rings = Even, Destination(D) can be replaced with Auxiliary(A) tower.
1. Calculate the total number of moves required i.e. "pow(2, n)
   - 1" here n is number of disks.
2. If number of disks (i.e. n) is even then interchange destination
   pole and auxiliary pole.
3. for i = 1 to total number of moves:
     if i%3 == 1:
	legal movement of top disk between source pole and
        destination pole
     if i%3 == 2:
	legal movement top disk between source pole and
        auxiliary pole
     if i%3 == 0:
        legal movement top disk between auxiliary pole
        and destination pole

https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
'''

dict = {0:'S', 1:'D', 2:'A'}
def tower_of_hanoi(num_rings, src_tower, dest_tower, aux_tower):
    if num_rings==0:
        return

    if num_rings%2==0:
        aux_tower, dest_tower = dest_tower,aux_tower

    num_moves = (1<<num_rings) - 1  # 2^n -1
    for move in range(1,num_moves+1):
        if (move%3==1):
            legal_move_ring(src_tower, dest_tower)
        elif (move%3==2):
            legal_move_ring(src_tower, aux_tower)
        else:
            legal_move_ring(aux_tower, dest_tower)

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


