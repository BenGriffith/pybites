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
    df = df.astype({"12/31/20": int, "12/31/19": int})
    df["dollar_flux"] = abs(df["12/31/20"] - df["12/31/19"])
    df["percentage_flux"] = abs(df["dollar_flux"] / df["12/31/19"])

    flux = []
    for row in df.itertuples():
        flux.append((row.Account, row._2, row._3, row.dollar_flux, row.percentage_flux))

    return flux


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []

    for flux in xyz:
        if flux[3] > THRESHOLDS[0] and flux[4] > THRESHOLDS[1]:
            flagged_lines.append(flux)

    return flagged_lines


# if __name__ == "__main__":
#     print(identify_flux(calculate_flux(XYZ)))