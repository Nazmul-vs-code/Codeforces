n = int(input())

crime_list = list(map(int,input().split()))

total_officer = 0
untreated_crime = 0

for i in crime_list:
    if i >0:
        total_officer+=i
    if i == -1:
        if total_officer > 0:
            total_officer -=1
        else:
            untreated_crime+=1        

print(untreated_crime)