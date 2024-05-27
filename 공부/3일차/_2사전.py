cab = {1:"김효현", 2:"지기환"} #키는 (??) value는 (name)
print(cab[1]) #키를 입력하면 된다

print(cab.get(1))

print(cab.get(5, "사용 가능"))
#cab[5]일 때 키가 없으면 강제 종료 되지만 .get(5)를하면 강제 종료 되지 않고 다음 문장이 실행 된다


print(1 in cab) #True
print(5 in cab) #Flase

cab = {"A-1":"김효현", "B-1":"박주원"}
print(cab["A-1"])

#키 추가 또는 키 바꾸기
cab["C-1"] = "지기환"
cab["B-1"] = "김경민"
print(cab)

del cab["C-1"]
print(cab)

print(cab.keys()) #키만 출력
print(cab.values()) #values만 출력
print(cab.items()) #둘 다 출력

cab.clear()
print(cab)