def lonelyinteger(b):
    answer = b[0]
    for x in b[1:]:
        answer=answer^x
    return answer

if __name__ == '__main__':
    a = int(input())
    b = [int(x) for x in input().strip().split(" ")]
    print(lonelyinteger(b))
