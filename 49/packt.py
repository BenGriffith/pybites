from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")

    # Book title
    book_title = soup.find_all("div", class_="dotd-title")[0].get_text().strip()

    # Book description
    book_description = soup.find("div", class_="dotd-main-book-summary").select("div")[2].get_text().strip()

    # Link
    book_link = [a["href"] for a in soup.find("div", class_="dotd-main-book-image").select("a[href]")][0]

    # Image
    book_image = [img["data-original"] for img in soup.find("div", class_="dotd-main-book-image").select("img[data-original]")][0]

    # NamedTuple
    book_nt = Book(book_title, book_description, book_image, book_link)
    return book_nt


# if __name__ == "__main__":
#     get_book()