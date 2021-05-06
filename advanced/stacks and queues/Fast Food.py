from collections import deque

food_quantity = int(input())

orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    order = orders.popleft()
    if food_quantity >= order:
        food_quantity -= order

    else:
        orders.appendleft(order)
        break

if orders:
    orders = deque(map(str, orders))
    print(f'Orders left: {" ".join(orders)}')
else:
    print(f"Orders complete")