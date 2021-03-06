def solution(phone_book):
    phone_book.sort()
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True


solution(["119", "97674223", "1195524421"])
# 전화번호부에 적힌 전화번호중 한 번호가 다른 번호의 접두어인 경우
# 가 있는지 확인

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 위의 경우에 구조대의 번호는 영석이 번호의 접두사

# 전화번호부 배열 phone_book
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
# 그렇지 않으면 true를 리턴
