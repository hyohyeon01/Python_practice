subway = [10, 20, 30]
print(subway)

subway = ["김효현", "박주원", "김경민"]
print(subway)
print(subway.index("김효현")) #몇 번째 있는지 찾기

subway.append("김주영")
print(subway)

subway.insert(1, "지기환") #사이에 넣기
print(subway)

subway.pop() #마지막 사람 꺼내기
print(subway)

subway.insert(3,"김효현")
print(subway.count("김효현"))

#정렬하기
num = [5,2,4,3,1]
num.sort()
print(num)
#뒤집기
num.reverse()
print(num)
#모두 지우기
num.clear
print(num)



mix_list = ["김효현", True, 20]
print(mix_list)

#두 리스트 합치기
num.extend(mix_list)
print(num)