import numpy as np
import pandas as pd


def main():
    filepath = "../dataset/airline-safety.csv"
    data = read_data(filepath)


def read_data(filepath):
    data = pd.read_csv(filepath)
    print(data.head())


if __name__ == "__main__":
    main()
