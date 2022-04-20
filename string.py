Value="my name is rabish kumar"

val=Value[8]
print(val)
print(Value)

txt = "my name is rabish kumar"
if "rabish" in txt :
    print("yes rabish is in value")
    print(len(txt))


    print("rabish" in txt)

    # slicing 
    b = "Hello, World!"
    print(b[2:5])   #Slicing
    print(b[:5])    #Slice From the Start
    print(b[2:])     #Slice To the End
    print(b[-5:-2])  # Negative indexing


    # Case change
    a = "Hello, World!"
    print(a.upper())
    print(a.lower())

    # Replace String
    a = "Hello, World!"
    print(a.replace("H", "J"))
    print(a.split(","))         # returns ['Hello', ' World!']


# Formater
    quantity = 3
    itemno = 567
    price = 49.95
    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(quantity, itemno, price))