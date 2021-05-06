from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = input().split()
bullets = [int(el) for el in bullets]

locks = deque(input().split())
locks = deque([int(el) for el in locks])
value = int(input())
barrel = gun_barrel_size
used_bullets = 0
while bullets:
    used_bullets += 1
    gun_barrel_size -= 1
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    if gun_barrel_size == 0:
        if bullets:
            print("Reloading!")
            gun_barrel_size = barrel
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${value - (used_bullets * bullet_price)}")
        exit()

print(f"Couldn't get through. Locks left: {len(locks)}")
