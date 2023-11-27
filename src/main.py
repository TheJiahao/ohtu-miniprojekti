from ui.ui import UI
from infrastructure.console_io import ConsoleIO
from services.logic import Logic


def main():
    logic = Logic()
    io = ConsoleIO()
    app = UI(io, logic)

    app.run()


if __name__ == "__main__":
    main()
