import random
def main():
    highest_diff = float("-inf")
    low_index = 0
    test = [round(random.uniform(1,3), 2) for i in range(10)]
    high_index = len(test)-1

    for i in range(1, len(test)):
        diff = test[high_index] - test[i]
        if diff > highest_diff:
            #new lowest number, update low
            if high_index > i:
                low_index = i
                highest_diff = diff
        elif diff > 0:
            #new highest number, update high
            if low_index < i:
                high_index = i
                highest_diff = test[i] - test[low_index]
        else:
            continue
    print(f"Buy on {low_index+1}, Sell on {high_index+1}")
    a = test[high_index] - test[low_index]
    b = bubble(test)
    print(a, b)

def bubble(test):
    lowest_diff = float("inf")

    for i in range(len(test)):
        for j in range(i, len(test)):
            diff = test[i] - test[j]
            if diff < lowest_diff:
                if i < j:
                    lowest_diff = diff
    return lowest_diff

if __name__ == "__main__":
    main()
