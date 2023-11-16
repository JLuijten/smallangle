import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def smallangle():
    pass


@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="amount of steps",
    show_default=True,
)
def sin(number):
    """get a Dataframe with values from 0 to 2 pi and the sin of the values.

    Args:
        number (int): amount of steps between 0 and 2 pi.
    """

    number = int(number)
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="amount of steps",
    show_default=True,
)
def tan(number):
    """get a Dataframe with values from 0 to 2 pi and the tan of the values.

    Args:
        number (int): amount of steps between 0 and 2 pi.
    """

    number = int(number)
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    sin(10)
