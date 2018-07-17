def solution(n, arr):
    for i in range(n):
        for j in range(i,n):
            if gcd(arr[i],arr[j])==1:
                return "YES"
        
    return "NO"
                


def gcd(a, b):
    if a==0:
        return b
    return gcd(b%a, a)
    
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(solution(n,arr))