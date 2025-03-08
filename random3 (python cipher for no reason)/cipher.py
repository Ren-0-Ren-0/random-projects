text=input("Enter the text: ")
shift=int(input("Enter the shift: "))
store1,store2=[],[]
bef_out1,bef_out2=[],[]
output1,output2="",""
def cipher(text, shift):
    for char in text.upper().split(""):
        print(char, ord(char), end=" ")
        store1.append(ord(char))
        
    for i in store1:
        bef_out1.append((i+2*shift)%26)
    
    for j in bef_out1:
        output1+=chr(j)


def decipher(text, shift):
    for char in text.upper().split(""):
        print(char, ord(char), end=" ")
        store2.append(ord(char))
        
    for i in store2:
        bef_out2.append((i-2*shift)%26)
    
    for j in bef_out2:
        output2+=chr(j)
        
        
y_n1=input("Do you want to encrypt the text? (Y/N): ")
if y_n1.upper()=="Y":
    cipher(text, shift)
    print("The encrypted text is: ", output1)
    
    y_n2=input("Do you want to decrypt the text? (Y/N): ")
    if y_n2.upper()=="Y":
        decipher(output1, shift)
        print("The decrypted text is: ", output2)
    else:
        print("Thank you!")
else:
    print("Thank you!")