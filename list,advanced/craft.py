collected_items = input().split(", ")
command = input()

while not command == "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        if item not in collected_items:
            collected_items.append(item)
    elif action == "Drop":
        if item in collected_items:
            collected_items.remove(item)
    elif action == "Combine Items":
        for i in range(len(collected_items)):
            if collected_items[i] in item:
                item_one, item_two = item.split(":")
                collected_items.insert(i+1, item_two)
                break
    elif action == "Renew":
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)
    command = input()
collected_items_str = ", ".join(collected_items)
print(collected_items_str)
