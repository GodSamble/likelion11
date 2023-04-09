a_list=['A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O']

A_cnt=0
B_cnt=0
O_cnt=0
AB_cnt=0

for i in a_list:
    if i == 'A':
        A_cnt+=1
    elif i == 'B':
        B_cnt+=1
    elif i =='O':
        O_cnt+=1
    else:
        AB_cnt+=1

print(A_cnt,B_cnt,O_cnt,AB_cnt)
print("hello")
# 깃 연습중