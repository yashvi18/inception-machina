
try:

    p=8778
    b=56434
    #f = open("ab.txt")


    p = b/0

    f = open("ab.txt")

    for line in f:
        print(line)

except FileNotFoundError as e:
    print( e.filename)

except Exception as e:
    print(e)

except ZeroDivisionError as e:
    print(e)
#except (FileNotFoundError , ZeroDivisionError):
    #print("file not found")

#except ZeroDivisionError:
    #print("zero division error")


#i = 0/0
