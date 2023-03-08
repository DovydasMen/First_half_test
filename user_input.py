import logging

logging.basicConfig(level=logging.DEBUG, filename='user_input_error.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def get_password_lenght()-> int:
    while True:
        try:
            password_lenght = int(
                input("Please define your password lenght(should be integer): "))
            if password_lenght < 1:
                raise Exception
        except (ValueError, KeyboardInterrupt, EOFError):
            logging.warning(f"Client trying to break our code. Entered bad value, o tried to paste or copy in our program.")
            print(f"You should specify integer, try again.")
        except Exception:
            print(f"Please enter value from 1 to +infinity")
            continue
        else:
            break
    return password_lenght


if __name__ == "__main__":
    get_password_lenght()
