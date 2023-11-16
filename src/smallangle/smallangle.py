import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def smallangle():
    pass


@smallangle.command()
@click.argument("number")
def sin(number):
    number = int(number)
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@smallangle.command()
@click.argument("number")
def tan(number):
    number = int(number)
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    sin(10)
