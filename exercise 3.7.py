while True:

    sum_1 = input("What is 5*5? ")
    if sum_1 == "25":
        print("That is correct! ")
        sum_2 = input("what is 24/3? ")
        if sum_2 == "8":
            print("That is correct! ")
            sum_3 = input("What is 10*11? ")
            if sum_3 == "110":
                print("That is correct! ")
                break
            else:
                print("That is false, you failed the test! ")
        else:
            print("That is false, you failed the test! ")
    else:
        print("That is false, you failed the test! ")
        break