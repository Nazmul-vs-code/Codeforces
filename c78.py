n = int(input())

# For Division 1: 1900≤rating
# For Division 2: 1600≤rating≤1899
# For Division 3: 1400≤rating≤1599
# For Division 4: rating≤1399



for i in range(n):
    rating = int(input())
    if 1900 <= rating:
        print("Division 1")
    elif 1600 <= rating and rating <=1899:
        print("Division 2")
    elif 1400<= rating and rating<=1599:
        print("Division 3")
    elif rating <= 1399 :
        print("Division 4")    