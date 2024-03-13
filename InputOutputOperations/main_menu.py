class MainMenu:
    def __init__(self):
        self.options = ''

    def display_menu(self):
        print("\nIf you're new to Python Look at Library I explain some of the operators")
        print("\n1. Single Integral Calculator")
        print("2. Double Integral Calculator")
        print("3. Triple Integral Calculator")
        print("4. Anti Derivative of a Function")
        print("5. Derivative of a Function")
        print("6. Riemann/Manual Sums of Functions")
        print("7. Library of Python Symbols(Have to use these)")
        print("8. Exit")
        self.options = input("Which option? ")
        return self.options

