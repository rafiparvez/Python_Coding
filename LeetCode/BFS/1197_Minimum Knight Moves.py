from collections import defaultdict

"""
 Because of board symmetry around (0,0), Without loss of generality, we can take
 absolute values of target coordinates and assume that the target will always be
 in upper right quadrant.
 In such case we can always, assume the Knight move in possi
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # because of symmetry, we can assume the target to be in upper right
        # quadrant
        x, y = abs(x), abs(y)
        self.min_steps = 0
        visited = defaultdict(int)

        def get_next_coordinates(k_x, k_y):
            coords = []
            return coords

        def bfs(k_x, k_y):
            if (k_x, k_y) == (x, y):
                return


        bfs(0, 0)
        return self.min_steps
