import heapq
from typing import Callable, Generic, Hashable, TypeVar

T = TypeVar("T", int, float)
H = TypeVar("H", bound=Hashable)
class Dijkstra(Generic[T, H]):
    
    def __init__(self,
                 neighbour_func: Callable[[H], list[H]],
                 cost_func: Callable[[H, H], T]):
        self.cost_func = cost_func
        self.neighbour_func = neighbour_func
        self.previous: dict[H, H] = {}
        self.costs: dict[H, T] = {}
    def find_path(self, start: H, end: H):
        queue = []
        queue.append([0,start])
        self.previous = {}
        self.costs = {}
        self.costs[start] = 0
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
        return self.costs[end]
    def get_path(self, end: H) -> list[H]:
        path = []
        current = end
        while current:
            path.append(current)
            current = self.previous[current]
        return path[::-1]