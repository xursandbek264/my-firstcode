num_bins=int(input("Enter the number of bins: "))
total_bottles=0
empty_botlles=0
for i in range(1, num_bins+1):
    num_bottles=int(input(f"Enter the bottle count in bin #{i}: "))
    total_bottles=total_bottles+num_bottles
    if num_bottles==0:
        empty_bins+=1

print(f"Total bottles: {total_bottles}")
print(f"Empty bins: {empty_bins}")
