def nearestValidPoint(x, y, points):
    def calculateDistance(point):
        distance = abs(x - point[0]) + abs(y - point[1])
        return distance
    
    min_distance = float("inf")
    index = 0
    for idx, point in enumerate(points):
        if x == point[0] or y == point[1]:
            distance = calculateDistance(point)
            if distance < min_distance:
                min_distance = distance
                index = idx
    return index if min_distance != float("inf") else -1


# Using a minheap
import heapq
def nearestValidPoint(self, x, y, points):
    def calculateDistance(point):
        distance = abs(x - point[0]) + abs(y - point[1])
        return distance
    
    heap = []
    for index, point in enumerate(points):
        if point[0] == x or point[1] == y:
            heappush(heap, (calculateDistance(point), index))
    return -1 if not heap else heapq.heappop(heap)[1]

                