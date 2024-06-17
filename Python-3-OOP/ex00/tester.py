from S1E9 import Character, Stark


def main():
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)

        # Test that Abstract Class can not be instantiated
        hodor = Character("hodor")
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
