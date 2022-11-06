# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# The documentation can be found in: https://realpython.com/build-a-python-url-shortener-with-fastapi/

from shortener_app.config import get_settings

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_settings().base_url)
    print(get_settings().db_url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
