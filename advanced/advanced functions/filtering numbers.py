b = [int(el) for el in input().split()]
positives = [el for el in b if el >= 0]
negatives = [abs(el) for el in b if el < 0]


print(f"-{sum(negatives)}")
print(sum(positives))


if sum(negatives) > sum(positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")