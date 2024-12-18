import heapq
from typing import Generic, TypeVar
from collections.abc import Callable, Hashable

T = TypeVar("T", int, float)
H = TypeVar("H", bound=Hashable)

class Dijkstra(Generic[T, H]):
    """
    Generic class for Dijkstra algorithm
    Returns:
        T: Type of the cost
        H: Type of the node
    """
    def __init__(self,
                 neighbour_func: Callable[[H], list[H]],
                 cost_func: Callable[[H, H], T],
                 min_cost: T):
        self.cost_func = cost_func
        self.neighbour_func = neighbour_func
        self.previous: dict[H, H | None] = {}
        self.costs: dict[H, T] = {}
        self.min_cost = min_cost
    def find_path(self, start: H, end: H):
        queue = []
        queue.append([0,start])
        self.previous = {}
        self.costs = {}
        self.costs[start] = self.min_cost
        self.previous[start] = None
        while queue:
            _, current = heapq.heappop(queue)
            if current == end:
                break
            for neighbour in self.neighbour_func(current):
                new_cost = self.costs[current] + self.cost_func(current, neighbour)
                if neighbour not in self.costs or new_cost < self.costs[neighbour]:
                    self.costs[neighbour] = new_cost
                    heapq.heappush(queue, [new_cost, neighbour])
                    self.previous[neighbour] = current
    def get_cost(self, end: H) -> T:
        if end not in self.costs:
            return self.min_cost
        return self.costs[end]
    def get_path(self, end: H) -> list[H]:
        path = []
        current = end
        while current:
            path.append(current)
            current = self.previous[current]
        return path[::-1]