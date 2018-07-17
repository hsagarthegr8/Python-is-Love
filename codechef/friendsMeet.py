def solution(n,arr):
    if n==1:
        return -1
    if arr[0] != 1:
       return -1
    for i in range(1,n):
        if isprime(arr[i]):
            return arr[i]
    return -1
       

def isprime(num):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        arr.sort()
        print(solution(n,arr))