import requests
from bs4 import BeautifulSoup


def get_website_content(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    return False


def get_parspack_data(url= "https://parspack.com/vps"):
    html_content = get_website_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "lxml")  # or "html.parser"

        card_plans = soup.find_all(class_="card-plan__wrap")
        for cp in card_plans:
            title = cp.find(class_="card-plan__title")
            price = cp.find(class_="card-plan__price")
            print("ParsPack VPS:")
            print(title.text, price.get("data-price"))


get_parspack_data()

cmd = input("Enter any key to exit.")
