def count_vowel(word=str):
    temp_list = list(word)
    count = 0
    vowels = "аеёиоуыэюя"
    for step in range(0, len(temp_list)):
        if temp_list[step] in vowels:
            count += 1
    return count

def rhythm(text=str):
    temp_list = text.split(" ")
    result_list = []
    count_in_all_words = 0
    for step in range(0, len(temp_list)):
        result_list.append(count_vowel(temp_list[step]))
    for step in range(0, len(result_list)):
        count_in_all_words = count_in_all_words +result_list[step]
    if count_in_all_words == 0:
        return False
    else:
        return all(check == result_list[0] for check in result_list)
    

text = input("Введите строку: ")
result = rhythm(text)

if result == True:
    print("Парам пам-пам")
else:
    print("Пам парам")