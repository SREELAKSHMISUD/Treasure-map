# To write a program that will mark a spot on a map with an X.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter : ") # Where do you want to put the treasure?
letter=position[0].lower()
abc="a","b","c"
letter_index=abc.index(letter) # Accesses the first character of input
number_index=int(position[1])-1 # Accesses the second character of input
map[number_index][letter_index]="X"
print(f"{line1}\n{line2}\n{line3}")