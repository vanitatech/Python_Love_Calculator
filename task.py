def calculate_love_score(name1 = "Angela Yu", name2 ="Jack Bauer"):
    
    combined_letters = f"{name1}{name2}".lower()
    # print(combined_letters)

    true_sum = 0
    for letter in "true":
        true_sum += combined_letters.count(letter)
        
    love_sum = 0
    for letter in "love":
        love_sum += combined_letters.count(letter)


    love_score = int(f"{true_sum}{love_sum}")

    print(love_score)
    
calculate_love_score("Kanye West", "Kim Kardashian")

