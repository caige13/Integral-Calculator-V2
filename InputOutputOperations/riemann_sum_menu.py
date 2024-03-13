class RiemannMenu:
    def __init__(self):
        self.options = ''

    def display_menu(self):
        print("\n1. Single Integral Calculator")
        print("2. Double Integral Calculator")
        print("3. Triple Integral Calculator")
        self.options = input("Which option? ")
        return self.options