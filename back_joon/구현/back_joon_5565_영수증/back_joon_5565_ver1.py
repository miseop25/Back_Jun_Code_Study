import sys
input = sys.stdin.readline

if __name__ == "__main__":
    total = int(input())
    for _ in range(9) :
        total -= int(input())
    print(total)