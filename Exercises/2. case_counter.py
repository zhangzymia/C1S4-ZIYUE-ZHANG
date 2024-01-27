def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        # Check if the character is alphabetic and uppercase
        if char.isalpha() and char.isupper():
            uppercase_count += 1
        # Check if the character is alphabetic and lowercase
        elif char.isalpha() and char.islower():
            lowercase_count += 1
    
    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)

case_counter("Hello World!")
case_counter("PYTHON")
case_counter("python")
case_counter("1234!@#$")
