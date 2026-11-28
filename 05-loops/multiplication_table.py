# Outer loop: rows 1–10
# Inner loop: columns 1–10
for row in range(1, 11):
    for col in range(1, 11):
        print(row * col, end="\t")
    print()