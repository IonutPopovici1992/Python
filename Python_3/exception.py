while True:
    try:
        number = int(input("What's your favorite number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number.")
    except ZeroDivisionError:
        print("Don't pick zero.")
    except:
        break
    finally:
        print("Loop complete.\n")
