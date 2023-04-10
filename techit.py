print("안녕하세요")
hi ="안녕하세요"
print(hi)

city = "seoul"
city.upper()

print(city.upper())

occupation = "  안  녕  "
occupation.lstrip()
print(occupation.lstrip())

score = "점수:90"
print(score.removeprefix("점수:"))

city2="서울 중구"
print(city2.replace("서울","서울시"))

si_1="용인"
gu_1="기흥"
address=f"{si_1}시    {gu_1}구"
print(address)
si_2="서울"
gu_2="종로"
print(f"{si_1}시, {gu_1}구.")

a=2
b=3
print(a**b)


price = 12_312_000_000
print(price)

#소문자 = 변수
#대문자 = 상수

print(3==3.0) #True
print(3 is 3.0) #False 문자열로 간주해서, 문자열-문자열로 같은지 비교함

#text = input("숫자를 입력해주세요: ")
#print(text)

"""
여러줄
주석
"""

# 파이썬은 모든 입력 값을 string으로 인식함. 고로, int()를통해 정수 혹은 실수의 형태로 바꿔야함

value = input("입력해주세요: ")
print(value)
value = value.upper()

if value =="INFP":
    print("INFP")
else:
    print("nothing")

i=0 
text= "" #반복문과 같이 i 혹은 text 등을 정의할 때, 쓰레기 값이 개입되지 않도록 항상 초기화 해주는 것이 좋음

progress = 0
while progress<100:
    progress+=1
    print(f"{progress}% completed")


