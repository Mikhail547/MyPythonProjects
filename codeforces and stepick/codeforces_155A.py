from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    n = int(input())
    # список прямых подчинённых сотрудника i
    graph = [[] for _ in range(n+1)]
    queue = deque() # очередь
    level = [0] * (n+1) # массив расстояний, длина ветви на i сотруднике
    for worker in range(1, n+1):
        manager = int(input()) # начальник нынешнего сотрудника, если его нет, то -1
        if manager == -1:
            queue.append(worker) # добавляем в начало очереди тех, у кого нет начальника
            level[worker] = 1 # стартовая длина ветви
        else: # иначе добавляем сотрудника в список его подчинённых
            graph[manager].append(worker)
    max_level = 0
    while queue:
        current = queue.popleft()
        max_level = max(max_level, level[current])
        for worker in graph[current]:
            level[worker] = level[current] + 1
            queue.append(worker)

    print(max_level)

bfs()