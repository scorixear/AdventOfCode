import heapq
from typing import Callable, Generic, TypeVar

T = TypeVar("T", int, float)

class AStar(Generic[T]):
    """Provides a generic A* algorithm implementation.

    Args:
        Generic (int | float): The cost and heuristic return type.
    """
    def __init__(self, graph: list[list], 
                 neighbour_func: Callable[[tuple[int, int]], list[tuple[int, int]]],
                 cost_func: Callable[[tuple[int, int], tuple[int,int]], T],
                 heuristic_func: Callable[[tuple[int, int]], T]):
        self.graph = graph
        self.cost_func = cost_func
        self.neighbour_func = neighbour_func
        self.heriustic_func = heuristic_func
        self.n = len(graph)
        self.m = len(graph[0])
        self.previous: dict[tuple[int, int], tuple[int, int]] = {}
        self.costs: dict[tuple[int, int], int] = {}
    
    def find_path(self, start: tuple[int, int], end: tuple[int, int]):
        queue = []
        queue.append([0,start])
        self.previous = {}
        self.previous[start] = None
        self.costs = {}
        self.costs[start] = 0
        
        while queue:
            _, current = heapq.heappop(queue)
            if current == end:
                break
            for neighbour in self.neighbour_func(current):
                new_cost = self.costs[current] + self.cost_func(current, neighbour)
                if neighbour not in self.costs or new_cost < self.costs[neighbour]:
                    self.costs[neighbour] = new_cost
                    priority = new_cost + self.heriustic_func(neighbour)
                    heapq.heappush(queue, [priority, neighbour])
                    self.previous[neighbour] = current
    def get_cost(self, end: tuple[int, int]) -> int:
        return self.costs[end]
    def get_path(self, end: tuple[int, int]) -> list[tuple[int, int]]:
        path = []
        current = end
        while current:
            path.append(current)
            current = self.previous[current]
        return path[::-1]