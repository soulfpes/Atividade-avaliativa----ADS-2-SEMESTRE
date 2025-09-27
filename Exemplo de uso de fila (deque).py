# Example of queue usage (deque)
# It helps to understand the idea of ​​"first in, first out" (FIFO).
from collections import deque

fila = deque()
fila.append("A")
fila.append("B")
fila.append("C")

print("Fila inicial:", list(fila))

print("Saiu:", fila.popleft())  # A
print("Fila agora:", list(fila))

print("Saiu:", fila.popleft())  # B
print("Fila agora:", list(fila))
