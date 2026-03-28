import numpy as np

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        H = np.array(heightMap)
        R, C = H.shape
        if R < 3 or C < 3: return 0
        
        # 1. Initialize Potential Field (W)
        # Boundary is fixed, interior is 'Infinite' capacity
        W = np.full((R, C), np.max(H))
        W[0, :], W[-1, :], W[:, 0], W[:, -1] = H[0, :], H[-1, :], H[:, 0], H[:, -1]
        
        # 2. Vectorized Field Relaxation
        # We propagate the 'Lowest Boundary' inward
        # This is a fixed-point iteration (Relief Mapping)
        while True:
            W_old = W.copy()
            
            # For every internal cell, the water level is the 
            # Max of its floor and the Min of its neighbors
            # We use slicing to shift the entire field at once
            W[1:-1, 1:-1] = np.maximum(H[1:-1, 1:-1], 
                            np.minimum(np.minimum(W[0:-2, 1:-1], W[2:, 1:-1]),
                                       np.minimum(W[1:-1, 0:-2], W[1:-1, 2:])))
            
            # Break when the potential field stabilizes
            if np.array_equal(W, W_old):
                break
                
        # 3. The Volume Integration
        # Volume = Total Potential - Total Topography
        return int(np.sum(W - H))        
