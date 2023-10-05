import os

border = "=============================="

print(f"""  

WELCOME to eKOS!
(Alpha Test Version 0.1)

{border}""")

print("""
MENU

[1] Information
[2] Payment
[3] EXIT

""")


user_input = input("YOUR CHOICE: ")
if user_input == "1":
    os.system('cls')
    print("""
    
    [INFORMATION]
    
    """)
    os.system('pause')
    os.system('exit')

elif user_input == "2":
    os.system('cls')
    print("""
    
    [PAYMENT]
    
    """)
    os.system('pause')
    os.system('exit')
    
else:
    os.system('exit')
    