items=[]
while True:
    item = input("Add item (type 'done' to finish):")
    if item.lower() == "done":
        break
    items.append(item)
print("Items in Cart: ",items)