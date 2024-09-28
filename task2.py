from collections import deque

# Функція для перевірки паліндрому


def is_palindrome(s):
    # Програма є нечутливою до регістру та пробілів
    s = ''.join(filter(str.isalnum, s)).lower()

    char_deque = deque(s)

    # Порівняння символів з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


input_string = "A man, a plan, a canal, Panama"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
