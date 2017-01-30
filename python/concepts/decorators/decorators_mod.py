def mod_outer(mod_inner):
    def wrapper():
        num = 10
        if num == 10:
            print("Yep, num == 10")
        else:
            print("nope...")

        mod_inner()

        print("something after mod_inner")

    return wrapper

if __name__ == "__main__":
    mod_outer()
