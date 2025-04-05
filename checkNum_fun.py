def get_valid_number():
    num = input("Enter number: ")
    
    while not num.isdigit():  
        num = input("Please enter a valid number: ")
    
    return int(num)  


number = get_valid_number()
print("Thats right its number:", number)
