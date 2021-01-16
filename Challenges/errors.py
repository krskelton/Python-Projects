def getInfo():
    var1 = input("please provide the first numeric value:")
    var2 = input("please probide the second numeric value:")
    return var1, var2

def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            #convert to an integer
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: You did not provide a numeric value".format(e))
        except:
            print("Oopsie, you provided invalid input, program will close now.")
        finally:
            print("Moving on...")
        print("{} + {} = {}".format(var1, var2, var3))

if __name__ == "__main__":
    compute()
