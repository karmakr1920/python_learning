# string_analyzer.py

def analyze_string(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    word_count = len(text.split())
    char_count = len(text)
    cleaned = ''

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        if char.isalnum():
            cleaned += char

    if cleaned:
        unique_chars = set(cleaned)
        most_common = max(unique_chars, key=cleaned.count)
    else:
        most_common = None

    is_palindrome = cleaned == cleaned[::-1]

    print("\n📊 String Analysis Result")
    print("-" * 30)
    print(f"Total Characters     : {char_count}")
    print(f"Total Words          : {word_count}")
    print(f"Vowel Count          : {vowel_count}")
    print(f"Consonant Count      : {consonant_count}")
    print(f"Most Frequent Char   : {most_common}")
    print(f"Is Palindrome?       : {'Yes' if is_palindrome else 'No'}")

if __name__ == "__main__":
    user_input = input("Enter a string to analyze: ")
    analyze_string(user_input)
