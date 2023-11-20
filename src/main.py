from services.logic import Logic
from app import App


def main():
    logic = Logic()
    app = App(logic)

    app.run()


if __name__ == "__main__":
    main()
