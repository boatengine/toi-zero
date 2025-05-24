m, d = int(input()), int(input())
print(["winter", "spring", "summer", "fall", "winter"][
    (m + (d >= 21)) // 3
])