import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from floodsystem.Analysis import polyfit


def plot_water_levels(station, dates, levels):
    # Plot
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]

    plt.plot(dates, levels)
    plt.axhline(y=typical_low, color='r', linestyle='-')
    plt.axhline(y=typical_high, color='r', linestyle='-')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]

    dates_float = matplotlib.dates.date2num(dates)
    plt.plot(dates_float, levels, '.')
    plt.axhline(y=typical_low, color='r', linestyle='-')
    plt.axhline(y=typical_high, color='r', linestyle='-')

    poly_tuple = polyfit(dates, levels, p)

    if poly_tuple is None:
        print("invalid Tuple")
    else:
        # Plot polynomial fit at 30 points along interval (note that polynomial
        # is evaluated using the shift x)
        x1 = np.linspace(dates_float[0], dates_float[-1], 30)
        plt.plot(x1, poly_tuple[0](x1 - dates_float[0]))

        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station.name)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels

        # Display plot
        plt.show()
