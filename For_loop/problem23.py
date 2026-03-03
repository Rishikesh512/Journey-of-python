sentence = input("Enetr any sentence :-")

total = 0

for word in sentence.split(): #.split() method use for ignoring spaces inside the string 
                            
    total += 1

print("All word in sentence is :-",total)