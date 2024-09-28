def is_balanced(s):
    # Стек для зберігання відкритих дужок
    stack = []

    bracket_map = {')': '(', ']': '[', '}': '{'}
    open_brackets = bracket_map.values()

    for char in s:
        if char in open_brackets:
            # Якщо це відкрита дужка, додаємо до стеку
            stack.append(char)
        elif char in bracket_map:
            # Якщо це закрита дужка, перевіряємо відповідність
            if not stack or stack.pop() != bracket_map[char]:
                return "Несиметрично"
    
    # Якщо після перебору стек порожній, значить усі дужки симетричні
    return "Симетрично" if not stack else "Несиметрично"




input_string_1 = "( ){[ 1 ]( 1 + 3 )( ){ }}"
print(f"{input_string_1}: {is_balanced(input_string_1)}")
input_string_2 = "( 23 ( 2 - 3);"
print(f"{input_string_2}: {is_balanced(input_string_2)}")
input_string_3 = "( 11 }"
print(f"{input_string_3}: {is_balanced(input_string_3)}")
