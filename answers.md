# CMPS 2200 Recitation 08

## Answers

**Name:** Kevin Skelly
**Name:** Zach Goodman


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**

W(E, V) = W(V) + W(E * ln(V)) = O(V+ElnV)

S(E) = O(E) 

- **2b)**

```
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
```
