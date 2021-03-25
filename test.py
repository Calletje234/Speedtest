items = {'a1':"", 'a2':"", 'a3':"", 
         'b1':"", 'b2':"", 'b3':"", 
         'c1':"", 'c2':"", 'c3':""}

def display_field(items):
    a1 = items['a1']
    a2 = items['a2']
    a3 = items['a3']
    b1 = items['b1']
    b2 = items['b2']
    b3 = items['b3']
    c1 = items['c1']
    c2 = items['c2']
    c3 = items['c3']   
    print(f"       |        |        ")
    print(f"   {a1}    |    {b1}    |    {c1}")
    print(f"       |        |        ")
    print(f"-------|--------|--------")
    print(f"       |        |        ")
    print(f"   {a2}    |  {b2}      |    {c2}")
    print(f"       |        |        ")
    print(f"-------|--------|--------")
    print(f"       |        |        ")
    print(f"   {a3}    |    {b3}    |    {c3}")
    print(f"       |        |        ")

def row1_win():
    a1 = item['a1']
    b1 = item['b1']
    c1 = item['c1']
    if a1, b1, c1 == "o":
        print("'o' is the winner!")
        return True
    elif a1, b1, c1 == "x":
        print("'x' is the winner!")
        return True

def row2_win():
    a2 = item['a2']
    b2 = item['b2']
    c2 = item['c2']
    if a2, b2, c2 == "o":
        print("'o' is the winner!")
        return True
    elif a2, b2, c2 == "x":
        print("'x' is the winner!")
        return True

def row3_win():
    a3 = item['a3']
    b3 = item['b3']
    c3 = item['c3']
    if a3, b3, c3 == "o":
        print("'o' is the winner!")
        return True
    elif a3, b3, c3 == "x":
        print("'x' is the winner!")
        return True

def colum1_win():
    a1 = item['a1']
    a2 = item['a2']
    a3 = item['a3']
    if a1, a2, a3 == "o":
        print("'o' is the winner!")
        return True
    elif a1, a2, a3 == "x":
        print("'x' is the winner!")
        return True

def colum2_win():
def colum3_win():
def diagonal1_win():
def diagonal2_win():

win = False
turn = "o_input"
while win == False:
    display_field(items)
    fillin = input("Please Enter a number between 1-9: ")
    if turn == "o_input":
        if fillin == "1" and items['a1'] == "":
            item["a1"] = 'o'
            turn = "x_input"
        elif fillin == "2" and items['b1'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "3" and items['c1'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "4" and items['a2'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "5" and items['b2'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "6" and items['c2'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "7" and items['a3'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "8" and items['b3'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        elif fillin == "9" and items['c3'] == "":
            item["b1"] = 'o'
            turn = "x_input"
        else:
            print("Sorry this isn't a valid input")
   if turn == "x_input":
        if fillin == "1" and items['a1'] == "":
            item["a1"] = 'x'
            turn = "o_input"
        elif fillin == "2" and items['b1'] == "":
            item["b1"] = 'x'
            turn = "o_input"
        elif fillin == "3" and items['c1'] == "":
            item["c1"] = 'x'
            turn = "o_input"
        elif fillin == "4" and items['a2'] == "":
            item["a2"] = 'x'
            turn = "o_input"
        elif fillin == "5" and items['b2'] == "":
            item["b2"] = 'x'
            turn = "o_input"
        elif fillin == "6" and items['c2'] == "":
            item["c2"] = 'x'
            turn = "o_input"
        elif fillin == "7" and items['a3'] == "":
            item["a3"] = 'x'
            turn = "o_input"
        elif fillin == "8" and items['b3'] == "":
            item["b3"] = 'x'
            turn = "o_input"
        elif fillin == "9" and items['c3'] == "":
            item["c3"] = 'x'
            turn = "o_input"
        else:
            print("Sorry this isn't a valid input")
        