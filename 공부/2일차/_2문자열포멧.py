# print("a"+"b")
# print("a","b")

print("나는 %d살 입니다."%(20))
print("나는 %s를 좋아해요"%("파이썬"))
print("Apple은 %c로 시작해요"%("A"))

print("나는 %s색과 %s색을 좋아해요."%("빨간", "파란"))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란")) #순서 바꾸기

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

age = 20
color = "파란색"
print(f"나는 {age}살이며, {color}색을 좋아해요")