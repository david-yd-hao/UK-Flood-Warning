import matplotlib.dates
import numpy as np


def polyfit(dates, levels, p):
    if len(dates) != 0 and len(levels) != 0:
        dates_float = matplotlib.dates.date2num(dates)

        # Find coefficients of best-fit polynomial f(x) of degree 4
        p_coeff = np.polyfit(dates_float - dates_float[0], levels, p)

        # Convert coefficient into a polynomial that can be evaluated,
        # e.g. poly(0.3)
        poly = np.poly1d(p_coeff)

        output_value = (poly, dates_float[0])

        return output_value
