from itertools import product

import elkplot
from elkplot import UNITS
import shapely
from shapely.affinity import translate


def square_grid(rows: int, cols: int, gap: float) -> shapely.MultiLineString:
    """
    Creates a grid of squares with small gaps between them
    :param rows: How many rows in the grid
    :param cols: How many columns in the grid
    :param gap: How big should the gap between squares be, represented in terms of a percent of the width of a square.
        (So 0 means the squares are touching and 1 means that you could fit a full square between each square.)
    :return: The grid as a MultiLineString
    """
    square = shapely.LinearRing([(0, 0), (0, 1), (1, 1), (1, 0)])
    offset = 1 + gap
    squares = [
        translate(square, c * offset, r * offset)
        for r, c in product(range(rows), range(cols))
    ]
    return shapely.union_all(squares)


def main():
    size = (11 * UNITS.inch, 8.5 * UNITS.inch)

    text = elkplot.text("ElK Plot Works!")
    text = elkplot.scale_to_fit(text, *size, 2)
    text = elkplot.center(text, *size)

    rows = 20
    cols = round(rows * size[0].m / size[1].m)
    grid = square_grid(rows, cols, 0.2)
    grid = elkplot.scale_to_fit(grid, *size, 0.5)
    grid = elkplot.center(grid, *size)
    grid = grid.difference(text.buffer(0.05))

    drawing = shapely.GeometryCollection([grid, text])
    print(elkplot.metrics(drawing))
    drawing = elkplot.optimize(drawing, 0.01)
    print(elkplot.metrics(drawing))

    elkplot.draw(drawing, *size, plot=False, preview_dpi=80)


if __name__ == "__main__":
    main()
