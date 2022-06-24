import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    max_calories = df.Calories.max()
    df_items_calories = df.filter(["Item", "Calories"])
    df_max_calories = df[df_items_calories.Calories == max_calories]
    return df_max_calories.Item.item()


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calculate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    df = df[df.Calories != 0]
    
    if excl_drinks:
        df = df[df.Category != "Coffee & Tea"]
        df = df[df.Category != "Beverages"]

    df["protein_calories_ratio"] = df.Protein / df.Calories
    df = df.sort_values("protein_calories_ratio", ascending=False)
    return df.Item.to_list()[:5]   


if __name__ == "__main__":
    #get_food_most_calories()
    get_bodybuilder_friendly_foods(df, True)