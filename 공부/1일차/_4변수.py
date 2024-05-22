
name = "기환이"
animal = "강아지"
age = 17
hobby = "술"
student = age >= 8

print("우리집 "+animal+" 이름은 "+ name +"야")
hobby = "와인"
print(name +"의 나이는 " + str(age) + "살이며, "+ hobby +"을 아주 좋아해") #정수형을 문자형으로 형변환
print(name+"는 학생일까? " + str(student)) #불리안도 마찬가지이다.
print(name,"는 ",age,"살 이다.") # ,를 쓸때는 형 변환을 안해도 됨 하지만 뛰어쓰기가 된다.