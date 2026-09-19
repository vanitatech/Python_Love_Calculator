def calculate_love_score(name1 = "Angela Yu", name2 ="Jack Bauer"):
    word =["T","R", "U", "E"]
    name_length = f"{name1} {name2}".lower()


    for letter in word:
        times = name_length.count(letter.lower())
        print(f"{letter} occurs {times} times")


calculate_love_score(name1 = "Angela Yu", name2 ="Jack Bauer")