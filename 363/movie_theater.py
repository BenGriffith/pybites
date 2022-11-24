TICKET_DISCOUNT = 5

"""
Refactor the code below. Try go get the functions' bodies
as close to the left side as possible (only one indentation deep).
"""
available_movies = {
    "Tomorrow Never Dies": {
        "id": "tomorrow_never_dies",
        "quality": "IMAX",
        "genre": "Action",
    },
    "Robin Hood": {"id": "robin_hood", "quality": "regular", "genre": "Adventure"},
    "Pulp Fiction": {"id": "pulp_fiction", "quality": "regular", "genre": "Crime"},
}


def invoice_to_be_refactored(movie, tickets):
    amount = 0
    movie_in_available_movies = False
    for title in available_movies:
        if title == movie:
            movie_in_available_movies = True
            if tickets != 0:
                if available_movies[movie]["quality"] == "IMAX":
                    price = 12
                    if tickets >= 5:
                        discount = 10
                    else:
                        discount = 0
                else:
                    price = 10
                    if tickets >= 5:
                        discount = 10
                    else:
                        discount = 0
            else:
                raise ValueError("Cannot calculate price for 0 tickets")
    if movie_in_available_movies is False:
        raise LookupError("Movie not available")
    else:
        total_amount = amount + (tickets * price) - discount
        return total_amount


def _discount(tickets):
    if tickets >= TICKET_DISCOUNT:
        return 10
    return 0


def _price(movie):
    if available_movies[movie]["quality"] == "IMAX":
        return 12
    return 10


def invoice_refactored(movie, tickets):
    """"Refactor the above code getting rid of the arrow shape"""
    if tickets == 0:
        raise ValueError
    if movie not in available_movies:
        raise LookupError

    discount = _discount(tickets)
    price = _price(movie)
    return tickets * price - discount