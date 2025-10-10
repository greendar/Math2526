



def median(data):
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    float: The median value.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def q1(data):
    """
    Calculate the first quartile (Q1) of a list of numbers.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    float: The first quartile value.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        lower_half = sorted_data[:mid]
    else:
        lower_half = sorted_data[:mid]  # Exclude median for odd-length lists

    return median(lower_half)

def q3(data):
    """
    Calculate the third quartile (Q3) of a list of numbers.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    float: The third quartile value.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        upper_half = sorted_data[mid:]
    else:
        upper_half = sorted_data[mid + 1:]  # Exclude median for odd-length lists

    return median(upper_half)

def box_plot_stats(data):
    """
    Calculate the five-number summary for a list of numbers.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    dict: A dictionary containing min, Q1, median, Q3, and max.
    """
    if not data:
        raise ValueError("Data list is empty")

    sorted_data = sorted(data)
    return {
        'min': sorted_data[0],
        'Q1': q1(sorted_data),
        'median': median(sorted_data),
        'Q3': q3(sorted_data),
        'max': sorted_data[-1]
    }

def draw_box_plot(data):
    """
    Draw a box plot for a list of numbers using matplotlib.

    Parameters:
    data (list): A list of numerical values.
    """
    import matplotlib.pyplot as plt

    plt.boxplot(data)
    plt.title("Box Plot")
    plt.ylabel("Values")
    plt.show()      

def draw_box_plot_horizontal(data):
    """
    Draw a horizontal box plot for a list of numbers using matplotlib.

    Parameters:
    data (list): A list of numerical values.
    """
    import matplotlib.pyplot as plt

    plt.boxplot(data, vert=False)
    plt.title("Horizontal Box Plot")
    plt.xlabel("Values")
    plt.show()
    
def main():
    a = [13, 12,9,11,14,12,10,15,11,10,7]
    print("Box plot statistics for dataset a:")
    for key, value in box_plot_stats(a).items():
       print(f"  {key}: {value}")

    draw_box_plot(a)
    draw_box_plot_horizontal(a)

#### End of Main ####


if __name__ == "__main__":
    main()
