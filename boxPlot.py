
import random as r
from typing import List, Dict

def generate_random_data(num_points: int, lower_bound: int = 1, upper_bound: int = 100, seed: int | None = None) -> List[int]:
    """
    Generate a list of random integers.

    Parameters:
        num_points (int): Number of random points to generate (> 0).
        lower_bound (int): Inclusive lower bound for random values.
        upper_bound (int): Inclusive upper bound for random values.
        seed (int | None): Optional seed for reproducibility.

    Returns:
        List[int]: A list of random integers.

    Raises:
        ValueError: If num_points <= 0 or lower_bound > upper_bound.
    """
    if num_points <= 0:
        raise ValueError("num_points must be > 0")
    if lower_bound > upper_bound:
        raise ValueError("lower_bound must be <= upper_bound")
    if seed is not None:
        r.seed(seed)
    return [r.randint(lower_bound, upper_bound) for _ in range(num_points)]


def median(data: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Convention:
        Standard median: middle value for odd n; average of the two middle values for even n.

    Parameters:
        data (List[float]): A list of numerical values (non-empty).

    Returns:
        float: The median value.

    Raises:
        ValueError: If data is empty.
    """
    if not data:
        raise ValueError("Data list is empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def _median_of_sorted(sorted_data: List[float]) -> float:
    """Helper: median assuming input is already sorted and non-empty."""
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def q1(data: List[float]) -> float:
    """
    Calculate the first quartile (Q1) using Tukey's method (exclude median for odd n).

    Parameters:
        data (List[float]): Numerical values.

    Returns:
        float: Q1.

    Raises:
        ValueError: If data has fewer than 2 elements.
    """
    if len(data) < 2:
        raise ValueError("At least 2 data points required for quartiles")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    lower_half = sorted_data[:mid]           # exclude median if odd
    return _median_of_sorted(lower_half)


def q3(data: List[float]) -> float:
    """
    Calculate the third quartile (Q3) using Tukey's method (exclude median for odd n).

    Parameters:
        data (List[float]): Numerical values.

    Returns:
        float: Q3.

    Raises:
        ValueError: If data has fewer than 2 elements.
    """
    if len(data) < 2:
        raise ValueError("At least 2 data points required for quartiles")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    upper_half = sorted_data[mid:] if n % 2 == 0 else sorted_data[mid + 1:]
    return _median_of_sorted(upper_half)


def box_plot_stats(data: List[float]) -> Dict[str, float]:
    """
    Compute five-number summary using Tukey's quartiles.

    Returns:
        dict: { 'min', 'Q1', 'median', 'Q3', 'max' }

    Raises:
        ValueError: If data is empty.
    """
    if not data:
        raise ValueError("Data list is empty")

    sorted_data = sorted(data)
    return {
        'min': sorted_data[0],
        'Q1': _median_of_sorted(sorted_data[:len(sorted_data)//2]),
        'median': _median_of_sorted(sorted_data),
        'Q3': _median_of_sorted(sorted_data[len(sorted_data)//2:] if len(sorted_data) % 2 == 0
                                else sorted_data[len(sorted_data)//2 + 1:]),
        'max': sorted_data[-1]
    }


def draw_box_plot(data: List[float], title: str = "Box Plot", horizontal: bool = False):
    """
    Draw a (horizontal) box plot using matplotlib.

    Parameters:
        data (List[float]): Numerical values.
        title (str): Plot title.
        horizontal (bool): True for horizontal orientation.

    Returns:
        matplotlib.figure.Figure: The figure object.
    """
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.boxplot(data, vert=not horizontal)
    ax.set_title(title)
    ax.set_ylabel("Values" if not horizontal else "")
    ax.set_xlabel("Values" if horizontal else "")
    return fig


def generate_Test_Questions(filename: str = "boxPlotTestQuestions.txt", seed: int | None = None):
    """
    Generate multiple random datasets and write their five-number summaries to a file.

    Parameters:
        filename (str): Output file path.
        seed (int | None): Optional RNG seed for reproducibility.
    """
    if seed is not None:
        r.seed(seed)
    with open(filename, "w") as f:
        for i in range(10, 23, 4):   # 10, 14, 18, 22
            for _ in range(4):       # Four datasets per size
                myList = generate_random_data(i)
                f.write('Data Set: ')
                f.write(' '.join(str(x) for x in myList))
                f.write('\n\n')
                stats = box_plot_stats(myList)
                for key in ['min', 'Q1', 'median', 'Q3', 'max']:
                    f.write(f"{key.capitalize()}: {stats[key]}\n")
                f.write('\n\n\n')
