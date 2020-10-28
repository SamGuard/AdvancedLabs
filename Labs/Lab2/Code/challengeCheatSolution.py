import heapq

def main():
    line = input().split()
    M = int(line[0])
    N = int(line[1])

    pQ = []
    line = input().split()
    for i in range(M):
        pQ.append(-1 * int(line[i]))

    heapq.heapify(pQ)
    
    totalMoney = 0
    for i in range(N):
        nextVal = -1 * heapq.heappop(pQ)
        totalMoney += nextVal
        heapq.heappush(pQ, -1 * (nextVal - 1))

    print(totalMoney)

main()