for i in range(1, 51):
    if i % 2 == 0:
        print(f"O número {i} é par!")
print("FIM!\n\n")

# ou, com menos trabalho

for i in range(2, 51, 2):
    print(f"O número {i} é par!")
print("FIM!")