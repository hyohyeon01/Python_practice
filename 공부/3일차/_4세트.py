#집합, 순서가 없고, 중복이 안됨
my = {1,2,3,3,3}
print(my)

java = {"박주원", "김경민"}
python = set(["김효현", "김경민"])

#교집합 자바와 파이썬 모두 할 수 있는 사람

print(java & python)

#합집합
print(java | python)

#차집합
print(java - python)

python.add("박주원")
print(python)

java.remove("김경민")
print(java)