""" Simple Script that we'll build off of.

Functions will include:
    fahrenheit_to_celcius(fahrenheit: float) -> float
    >>> [fahrenheit_to_celcius(x) for x in [-40, 14, 32., 50, 60.8, 95.0]]
    [-40.0, -10.0, 0.0, 10.0, 16.0, 35.0]

=================================================================
    Task #1.
        `celcius_to_fahrenheit(celcius: float) -> float`

        Create a function with above call signature,
        such that it passes the below tests.
        edit the place_holder function to do this.
        remove # when function is ready

    # >>> [celcius_to_fahrenheit(x) for x in [-40.0, -10.0, 0.0, 10.0, 16.0]]
    [-40.0, 14.0, 32.0, 50.0, 60.8]

=================================================================
    Task #2a:
        `celcius_to_kelvin(celcius: float) -> float`

        Create a function with above call signature,
        such that it passes the below tests.

        edit the place_holder function to do this.
        remove # when function is ready

    # >>> celcius_to_kelvin(0)
    273.15

    Task #2b:
        `kelvin_to_celcius(celcius: float) -> float`

        This time add the new function below you celcius_to_kelvin method.

    # >>> kelvin_to_celcius(0)
    -273.15

=================================================================
    Task 3:
        Merge `feature1` into main.  Then merge `feature2` into main.

=================================================================
    Task 4:
        Last 2 functions, Add below your other edits.

        `fahrenheit_to_kelvin(fahrenheit: float) -> float`

        `kelvin_to_fahrenheit(fahrenheit: float) -> float`


    # >>> [fahrenheit_to_kelvin(x) for x in [14, 32., 50, 60.8, 95.0]]
    [263.15, 273.15, 283.15, 289.15, 308.15]

    # >>> [kelvin_to_fahrenheit(x) for x in [263.15, 273.15, 283.15, 289.15, 308.15]]
    [14.0, 32.0, 50.0, 60.8, 95.0]

"""

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celcius_to_kelvin(celcius):
    return celcius + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

if __name__ == "__main__":
    import argparse
    agp = argparse.ArgumentParser()
    agp.add_argument('value', type=float)
    val = agp.parse_args().value

    print(f"{val}°F = {fahrenheit_to_celcius(val):.2f}°C")

    # 1.  uncomment this line once you have added a c_to_f function
    # print(f"{val}°C = {celcius_to_fahrenheit(val):.2f}°F")

    #2.  uncomment these lines when c_to_k and k_to_c are done
    # print(f"{val}°C = {celcius_to_kelvin(val):.2f} K")
    # print(f"{val} K = {kelvin_to_celcius(val):.2f}°C")

    #3.  uncomment these lines when f_to_k and k_to_f are done
    # print(f"{val}°F = {fahrenheit_to_kelvin(val):.2f} K")
    # print(f"{val} K = {kelvin_to_fahrenheit(val):.2f}°F")
