"""
973. K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique 
(except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""

# Using a mainheap
# Time complexity: O(klogn)
# Space complexity: O(n)
import heapq
class Solution(object):
    def kClosest(self, points, k):
        def calculateDistance(point):
            distance = (0 - point[0])**2 + (0 - point[1])**2
            return distance
        result = []
        distAndPoint = [(calculateDistance(points[i]), points[i]) for i in range(len(points))]
        heapq.heapify(distAndPoint)
        # Pop k times
        while k > 0:
            _, point = heapq.heappop(distAndPoint)
            result.append(point)
            k -= 1
        return result
            
