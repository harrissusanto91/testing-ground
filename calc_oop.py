class Calculator:  
    def __init__(self):  
        self.history = []  

    def add(self, a, b):  
        result = a + b  
        self.history.append(f"{a} + {b} = {result}")  
        return result  

    def subtract(self, a, b):  
        result = a - b  
        self.history.append(f"{a} - {b} = {result}")  
        return result  
    
    def multiply(self, a, b):  
        result = a * b  
        self.history.append(f"{a} * {b} = {result}")  
        return result  

    def divide(self, a, b):  
        if b == 0:  
            return "Error: Division by zero."  
        result = a / b  
        self.history.append(f"{a} / {b} = {result}")  
        return result  

    def show_history(self):  
        if not self.history:  
            return "No history available."  
        return "\n".join(self.history)  

def main():  
    calc = Calculator()  
    
    while True:  
        print("\nSimple Calculator")  
        print("Select operation:")  
        print("1. Add")  
        print("2. Subtract")  
        print("3. Multiply")  
        print("4. Divide")  
        print("5. Show History")  
        print("6. Exit")  

        choice = input("Enter choice (1/2/3/4/5/6): ")  

        if choice in ['1', '2', '3', '4']:  
            try:  
                num1 = float(input("Enter first number: "))  
                num2 = float(input("Enter second number: "))  
            except ValueError:  
                print("Invalid input! Please enter numeric values.")  
                continue  

            if choice == '1':  
                print(f"Result: {calc.add(num1, num2)}")  
            elif choice == '2':  
                print(f"Result: {calc.subtract(num1, num2)}")  
            elif choice == '3':  
                print(f"Result: {calc.multiply(num1, num2)}")  
            elif choice == '4':  
                print(f"Result: {calc.divide(num1, num2)}")  

        elif choice == '5':  
            print("\nCalculation History:")  
            print(calc.show_history())  

        elif choice == '6':  
            print("Exiting the calculator. Goodbye!")  
            break  

        else:  
            print("Invalid choice! Please select a valid operation.")  

if __name__ == '__main__':  
    main()