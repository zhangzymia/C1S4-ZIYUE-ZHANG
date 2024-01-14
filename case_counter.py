def case_conter(text):
    uppercase_count = 0
    lowercase_count = 0
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return f"uppercase letters:{uppercase_count}, lowercase letters:{lowercase_count}"
print (case_conter("Hello World!"))
print (case_conter("PYTHON"))
print (case_conter("python"))
print (case_conter("1234!@#$"))
