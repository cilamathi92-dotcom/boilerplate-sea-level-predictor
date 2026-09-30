import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from CSV
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )

    # Extend line to 2050
    years = pd.Series(range(df["Year"].min(), 2051))
    predicted_sea_level = slope * years + intercept

    ax.plot(years, predicted_sea_level)

    # Line of best fit using data from 2000 onwards
    recent_df = df[df["Year"] >= 2000]

    slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = linregress(
        recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"]
    )

    years_2 = pd.Series(range(2000, 2051))
    predicted_sea_level_2 = slope_2 * years_2 + intercept_2

    ax.plot(years_2, predicted_sea_level_2)

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return figure
    plt.savefig("sea_level_plot.png")
    return plt.gca()