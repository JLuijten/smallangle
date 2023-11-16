import click
import numpy as np
import pandas as pd
from numpy import pi


# defining the callable function
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
    """get a Dataframe with values from 0 to 2 pi and the sin of the values, the values are from a chosen sample size.

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
    """get a Dataframe with values from 0 to 2 pi and the tan of the values, the values are from a chosen sample size.

    Args:
        number (int): amount of steps between 0 and 2 pi.
    """

    number = int(number)
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


@smallangle.command()
@click.option(
    "-a",
    "--accuracy",
    default=0.1,
    help="maximum allowed difference",
    show_default=True,
)
def approx(accuracy):
    """finds the largest angle the small-angle approximation holds up to for an accuracy

    Args:
        accuracy (float): largest allowed difference between x and sin(x)
    """

    # status is set to 0 when done
    status = 1

    check_number = 0
    while status == 1:
        if abs(check_number - np.sin(check_number)) > accuracy:
            status = 0
        else:
            check_number += 0.001

    print(
        f"For an accuracy of {accuracy}, the small-angle approximation holds up to x = {check_number:.3} ."
    )


if __name__ == "__main__":
    sin(10)
