from data import *


def loading_screen() -> None:
    """Simulates a loding screen operation
    """

    loading_character = chr(9609)
    loading_logo = list(loading_character)
    download_limit = 100
    bytes_downloaded = 0

    while bytes_downloaded <= download_limit:
        clean()
        loading_logo.append(loading_character)

        for byte in loading_logo:
            string_loading_logo = list_to_string(loading_logo)

        print(f"{color_blue}{bytes_downloaded} : {color_green}{string_loading_logo}{color_blue}")
        bytes_downloaded += 1

loading_screen()


def welcome_screen() -> None:
    """Simulates a welcome screen operation
    """

    clean()
    print(f"{color_blue}Welcome to KhodeNima's Random password generator Version : {color_green}{current_version}{color_blue} .")
    sleep(0.5)


def goodbye_screen() -> None:
    """Simulates a goodbye screen operation
    """

    clean()
    print(f"{color_blue} Thanks for using KhodeNima's Random password generator . \n")
    sleep(2)
    print(f"{color_red} THE APP HAS BEEN CLOSED {color_blue}")
    sleep(1.5)
    clean()