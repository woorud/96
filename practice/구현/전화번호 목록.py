def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        cur = phone_book[i]
        for j in range(i+1, len(phone_book)):
            tmp = phone_book[j]
            if tmp.startswith(cur):
                return False
    return True
