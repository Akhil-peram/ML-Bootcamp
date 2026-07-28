def divider():
    try:
        nume = int(input("Enter numerator: "))
        denom = int(input("Denominator: "))
        result = nume / denom
        print(result)

    except ZeroDivisionError:
        print("Can't divide with Zero")
    except ValueError:
        print("Enter only integers ")

divider()
