from classes.sistema import Sistema
from classes.dashboard import Dashboard


def main():

    sistema = Sistema()

    dashboard = Dashboard(sistema)

    dashboard.iniciar()


if __name__ == "__main__":
    main()