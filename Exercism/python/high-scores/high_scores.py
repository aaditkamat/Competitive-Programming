import heapq

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


# Create a max heap based on the scores and pop the top element the required number of times 
# (either 3 or the size of heap, which one ever is lesser)
def personal_top_three(scores):
    max_heap = [-score for score in scores]
    heapq.heapify(max_heap)
    return [-1 * heapq.heappop(max_heap) for i in range(min(len(max_heap), 3))]
