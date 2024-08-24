from weather_fetcher import WeatherDataFetcher
from data_parser import DataParser
from user_interface import UserInterface

def main():
    fetcher = WeatherDataFetcher()
    parser = DataParser()
    ui = UserInterface(fetcher, parser)
    ui.main()

if __name__ == "__main__":
    main()
