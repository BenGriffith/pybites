import pandas as pd

XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = pd.read_csv(XYZ)
    print(df.shape[0])
    df = df.astype({"12/31/20": int, "12/31/19": int})
    df["dollar_flux"] = abs(df["12/31/20"] - df["12/31/19"])
    df["percentage_flux"] = abs(df["dollar_flux"] / df["12/31/19"])

    flux = [*zip(df["dollar_flux"], df["percentage_flux"])]

    return flux


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []

    for flux in xyz:
        if flux[0] >= THRESHOLDS[0] and flux[1] >= THRESHOLDS[1]:
            flagged_lines.append()

    return flagged_lines


if __name__ == "__main__":
    print(calculate_flux(XYZ))