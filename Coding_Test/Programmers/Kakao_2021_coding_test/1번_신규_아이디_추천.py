# https://programmers.co.kr/learn/courses/30/lessons/72410
import re

def solution(new_id):
    st = new_id
    st = st.lower() # 소문자로
    st = re.sub('[^a-z0-9\-_.]', '', st) # 특수문자 제거
    st = re.sub('\.+', '.', st) # .. 2개이상은 .으로 대체
    st = re.sub('^[.]|[.]$', '', st) # 맨처음. or 맨끝.을 제거
    st = 'a' if st == '' else st[:15]
    st = re.sub('^[.]|[.]$', '', st) # 맨처음. or 맨끝.을 제거
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    
'''
no	 new_id	                         result
예1	"...!@BaT#*..y.abcdefghijklm"	 "bat.y.abcdefghi"
예2	"z-+.^."	                     "z--"
예3	"=.="	                         "aaa"
예4	"123_.def"	                     "123_.def"
예5	"abcdefghijklmn.p"	             "abcdefghijklmn"
'''
