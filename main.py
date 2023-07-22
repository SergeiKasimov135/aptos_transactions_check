from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_transactions(driver: webdriver.Chrome, url: str) -> int:
    driver.get(url)
    sleep(2.2)
    rows_of_transactions_table = driver.find_elements(By.CLASS_NAME, 'MuiTableRow-root')
    sleep(1.2)
    return len(rows_of_transactions_table) - 1


def main() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options)
    last_page = int(input("Введите номер последней страницы: "))
    user_address = input("Введите адрес кошелька: ")
    amount_of_transactions = 0

    if last_page > 1:
        amount = get_transactions(driver, f"https://explorer.aptoslabs.com/account/{user_address}?network=mainnet&page=1") * last_page - 1
        amount_on_last_page = get_transactions(driver, f"https://explorer.aptoslabs.com/account/{user_address}?network=mainnet&page={last_page}")
        amount_of_transactions += amount + amount_on_last_page
    else:
        amount_of_transactions += get_transactions(driver, f"https://explorer.aptoslabs.com/account/{user_address}?network=mainnet&page={last_page}")

    print(f"Количество транзакций: {amount_of_transactions}")


if __name__ == "__main__":
    main()
