import re
'''
정규표현식
1. 문자클래스 []
숫자: [0-9], 알파벳: [a-zA-Z]
\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

2. Dot(.)
a.b = a + 모든문자 + b

3. 반복(*), 반복(+), 반복({m,n}, ?)
{1,} = +
{0,} = *


모듈
1. match(): 문자열의 처음부터 정규식과 매치되는지 조사한다.
2. search(): 문자열 저체를 검색하여 매치되는지 조사한다.
3. findall(): 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
4. finditer(): 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.

메타문자
|: or, ^: 문자열의 맨 처음, $: 문자열의 맨 끝 
\A: 줄과 상관없이 전체 문자열의 맨 처음, 
\Z: 줄과 상관없이 전체 문자열의 맨 끝, 
\b: 공백으로 구분되는 단어만 매치, 
\B: 공백으로 구분되지 않은 단어만 매치
'''

def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    #3
    new_id = re.sub('\.+', '.', new_id)
    #4
    new_id = re.sub('^[.]', '', new_id)
    new_id = re.sub('[.]$', '', new_id)
    #5
    new_id = new_id if new_id else 'a'
    #6
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = re.sub('[.]$', '', new_id)
    #7
    new_id = new_id + new_id[-1]*(3-len(new_id)) if len(new_id) <= 2 else new_id

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."	))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
