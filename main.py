from collections import deque
import heapq

def shortest_shortest_path(graph, source):
  dist = {v: (float('inf'), float('inf')) for v in graph}
  dist[source] = (0, 0) 

  pq = [(0, 0, source)] 

  while pq:
      curr_dist, curr_edges, curr_node = heapq.heappop(pq)

      if (curr_dist, curr_edges) > dist[curr_node]:
          continue

      for neighbor, weight in graph[curr_node]:
          new_dist = curr_dist + weight
          new_edges = curr_edges + 1
          
          if (new_dist, new_edges) < dist[neighbor]:
              dist[neighbor] = (new_dist, new_edges)
              heapq.heappush(pq, (new_dist, new_edges, neighbor))
  return dist
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent = {source: None}
    queue = deque([source])

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if neighbor not in parent:
                parent[neighbor] = current_vertex
                queue.append(neighbor)

    return parent


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = ''
    current = destination
    while current is not None:
        path += str(current)
        current = parents[current]
    return path[:0:-1]
    pass

