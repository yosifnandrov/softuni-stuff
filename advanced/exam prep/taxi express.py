from collections import deque

customers = [int(el) for el in input().split(", ")]

taxi = [int(el) for el in input().split(", ")]

total_time = 0

customers = deque(customers)

while customers:
    if not taxi:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break
    current_customer = customers.popleft()
    current_taxi = taxi.pop()
    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)


if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")



