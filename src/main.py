from services.logic import Logic
from app import App
from console_io import ConsoleIO


def main():
    logic = Logic()
    io = ConsoleIO()
    app = App(io, logic)

    app.run()


if __name__ == "__main__":
    main()
