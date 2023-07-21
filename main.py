from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_transactions(driver: webdriver.Chrome) -> int:
    rows_of_transactions_table = driver.find_elements(By.CLASS_NAME, 'MuiTableRow-root')
    return len(rows_of_transactions_table)


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options)
    last_page = int(input("Введите номер последней страницы: "))
    user_address = input("Введите адрес кошелька: ")
    amount_of_transactions = 0
    for number_of_page in range(1, last_page + 1):
        driver.get(f"https://explorer.aptoslabs.com/account/{user_address}?network=mainnet&page={number_of_page}")
        sleep(0.5)
        amount = get_transactions(driver)
        amount_of_transactions += amount
        # print(f"[INFO] обработал страницу {number_of_page}")

    print(amount_of_transactions)


if __name__ == "__main__":
    main()

