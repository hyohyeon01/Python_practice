python = "I Want go Home"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #0번째 있는 값이 대문자면 True
print(len(python)) #문자열의 길이
print(python.replace("Home", "School")) #원하는 문자열로 바꾸기

index = python.index("o") #g가 있는 위치
print(index)

index = python.index("o", index + 1) #위에 있는 index에서 o의 위치를 찾은 다음 부터 또 o가 있는지 찾기
print(index)

print(python.find("Home"))#없으면 -1 나옴 하지만 index에서 없으면 에러남

print(python.count("o")) # 몇 번 나오는 지