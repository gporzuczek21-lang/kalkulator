import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def method(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Nie można dzielić przez zero!"
    else:
        return x / y

if __name__=="__main__":
    wybor = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    num1 = float(input("Podaj składnik 1: "))
    num2 = float(input("Podaj składnik 2: "))     
    if wybor == '1':
        logging.info(f"dodaje {num1} i {num2}")
        print(add(num1, num2))

    elif wybor == '2':
        logging.info(f"odejmuje {num2} od {num1}") 
        print(sub(num1, num2))

    elif wybor == '3':
        logging.info(f"mnoze {num1} i {num2}")
        print(method(num1, num2))

    elif wybor == '4': 
        logging.info(f"dziele {num1} przez {num2}")
        print(div(num1, num2))
    
    else:
        print("Nieprawidłowy wybór")

    