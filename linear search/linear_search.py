# Algorithm: Linear search

data = list(range(1, 1001))

# Linear search for targeting element
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
        
    return None

target = int(input("What number you want found?" ))
print(f"Number {target}: {linear_search(data, target)}")
