#program that counts length of string and vowels in it
#written by Mahmud Shuaib
#26-Sept-2021 
def NameIt():
    count = 0 # variable to store the no of vowels in name
    name = input("Please enter your name: ")
    name = name.lower()
    get_length = len(name)
    print(f'Hello there {name}')
    print(f'There are {get_length} characters in your name')
    for v in name:
        if v == 'a':
            count+= 1 #if a vowel is detected, add 1 to count
            print('a detected')
        elif v == 'e':
            count+= 1
            print('e detected')
        elif v == 'i':
            count+= 1            
            print('i detected')
        elif v == 'o':
            count+= 1            
            print ('o detected')
        elif v == 'u':
            count+= 1            
            print ('u detected')
    else:
        print(f'total no of vowels detected in your name: "{name}" are : {count}')
#calling the function
NameIt()


