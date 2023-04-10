#리스트 => append insert del pop Remove / len() /
colors= ['red','blue','green']
colors.insert(2,'yellow')
print(colors)

del colors[0]
print(colors)

color=colors.pop(0)
print(color)
# del 과 pop은 동일하나, 리턴값으로 없앤 값을 살려놓음
#remove('yellow')이런 식의 remove 함수도 있음

print("_----------------------------------_")
real_colors=['grey','white','black','yellow']
#real_colors.sort(reverse=True) 역순으로 나옴
print(real_colors)
print(real_colors[-1])


cp1 = ['one','two','three','four','five']
cp2 = cp1[:] # 중요 !!!!! 이렇게 해줘야 값복사임. [:] 를 빼고 쓸 시, 참조의 개념이 돼서 기존의 값에 지장이 가게 됨.
cp2.pop()
print(cp1)
print(cp2)

################## 이 밑으론 튜플 ##################
tup = (1, 20, 44)
print(tup)
list_tup = list(tup) # 튜플을 리스트로 변경
print(list_tup)


################## Dictionary 키와 벨류
student = {
    "student_no" : "2020205001",
    "major" : "software",
    "grade" : 3
}
print(student["student_no"])
#추가
student["gpa"] = 4.5
print(student)

#삭제
del student["grade"]
print(student)

friend = {
    "name" : "철수",
    "age" : 14,
    "height" : 180
}

print(friend.get("weight" , "해당 키-값 이 없습니다."))

print(list(friend.values()))
print(list(friend.keys()))

tech = {
    "HTML": "Advanced",
    "JavaScript": "Intermediate",
    "Python": "Expert",
    "Go": "Novice"
}
for key, value in tech.items(): #중요!!!!! items()
    print(f'{key}-{value}')

for i in tech: #이렇게 할 시 키 값만 나오게 됨.
    print(i)

for key in tech.keys():
    print(key)

for value in tech.values():
    print(value)


student_1 = {
    "student_no": "1",
    "gpa": "4.3"
}

student_2 = {
    "student_no": "2",
    "gpa": "3.8"
}

students= [student_1, student_2]

for student in students:
    print(student)