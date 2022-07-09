"""Написати калькулятор температури.
    Користувач вводить число та тип температури (C, F, K - Цельсій, Фарренгейт, Кельвін відповідно)
    Програма має вивести температуру у трьох шкалах температур – Цельсій, Фарренгейт, Кельвін."""


def celsius_calc(temp):
    fahrenheit = 1.8 * temp + 32
    kelvin = 273.15 + temp
    return fahrenheit, kelvin


def fahrenheit_calc(temp):
    celsius = (temp - 32) * 5 / 9
    kelvin = celsius + 273.15
    return kelvin, celsius


def kelvin_calc(temp):
    celsius = temp - 273.15
    fahrenheit = celsius * 1.8 + 32
    return celsius, fahrenheit


def main():
    temp_type = str(input("Choose type of temperature (C, F, K): "))
    temp = float(input("Enter temperature: "))
    if temp_type == "C":
        print(temp, "C is :", round(celsius_calc(temp)[0], 1), "F", "and", round(celsius_calc(temp)[1], 1), "K")
    if temp_type == "F":
        print(temp, "F is:", round(fahrenheit_calc(temp)[0], 1), "C", "and", round(fahrenheit_calc(temp)[1], 1), "K")
    if temp_type == "K":
        print(temp, "K is :", round(kelvin_calc(temp)[0], 1), "C", "and", round(kelvin_calc(temp)[1], 1), "F")


if __name__ == '__main__':
    main()
