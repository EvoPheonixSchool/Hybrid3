#By:Sheldon McGrath


#takes two numbers adds and returns them
def add(n1,n2):
    return n1 + n2

#takes two numbers, subtracts and returns them
def subtract(n1,n2):
    return n1 - n2

#takes two numbers, multiplies and returns them
def multiply(n1,n2):
    return n1 * n2

#takes two numbers, divides and returns them
def divide(n1,n2):
    return n1 / n2

#main block
if __name__ == '__main__':
    #loops until quit has been chosen
    end = False
    while end == False:

        #takes 2 numbers and an operator from keyboard input
        num1 = int(input('enter a number: '))
        num2 = int(input('enter a second number: '))
        op = input('select an operator(+,-,/,*): ')

        #selects function to call from operator
        if op == '+': print(add(num1,num2))
        elif op == '-': print(subtract(num1,num2))
        elif op == '/':
            if num2 == '0': print("Only chuck norris can divide by zero")
            else: print(divide(num1,num2))
        elif op == '*': print(multiply(num1*num2))
        else: print("you have used an illegal operator")

        #ask to quit program
        quit = input('would you like to quit(y/n)?')

        #close if true
        if quit == 'y': end = True


