"""
    main.py
    --------------
    This is the main module. Implements the UI and business logic.

"""
import sys
import WiSSCI_GUI


def main():
    # Create the QT application
    app = WiSSCI_GUI.QtWidgets.QApplication(sys.argv)

    # Create the main window
    win = WiSSCI_GUI.WissciGui()
    win.show()

    # Start QT application
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
