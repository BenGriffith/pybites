from decimal import Decimal

def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    splits = []

    item_total = Decimal(item_total.lstrip("$"))
    tax_rate = Decimal(tax_rate.rstrip("%")) / 100
    tip = Decimal(tip.rstrip("%")) / 100

    total_with_tax = round(item_total + (item_total * tax_rate), 2)
    total_with_tip = total_with_tax + round(total_with_tax * tip, 2)

    grand_total = total_with_tip
    
    while people != 0:
        split = round(grand_total/people, 2)
        splits.append(split)
        grand_total = grand_total - split
        people -= 1

    return (f"${total_with_tip:.2f}", splits)