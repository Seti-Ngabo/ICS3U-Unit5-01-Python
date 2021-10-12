#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program calculates the temperature in degrees fahrenheit
#   with user input


def fahrenheit():
    # this function lets you enter in a temperature in degrees Celsius and it
    #   then prints out what that temperature is degrees Fahrenheit

    # input
    user_input_as_str = input("Enter a temperature (℃): ")
    print("")

    # process and output
    try:
        user_input_as_int = int(user_input_as_str)
        temperature = (9 / 5) * user_input_as_int + 32
        print("{0}℃ is equal to {1}℉.".format(user_input_as_int, temperature))

    except Exception:
        print("{0} is not a temperature.".format(user_input_as_str))

    print("\nDone.")


def main():
    # call function
    fahrenheit()


if __name__ == "__main__":
    main()
