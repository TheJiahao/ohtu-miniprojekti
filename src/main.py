from app import App
from console_io import ConsoleIO
from services.logic import Logic


def main():
    logic = Logic()
    io = ConsoleIO()
    app = App(io, logic)

    app.run()


if __name__ == "__main__":
    main()
