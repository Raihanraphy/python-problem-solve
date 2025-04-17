if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    roomSet = set(rooms)
    roomSum = sum(rooms)
    roomSetSum = sum(roomSet) * k
    captiansRoom = (roomSetSum - roomSum) // (k - 1)
    print(captiansRoom)