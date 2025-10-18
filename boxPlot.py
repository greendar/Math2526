import random as r 

def generate_random_data(num_points, lower_bound=1, upper_bound=100):
    """
    Generate a list of random integers.

    Parameters:
    num_points (int): The number of random points to generate.
    lower_bound (int): The lower bound for the random values.
    upper_bound (int): The upper bound for the random values.

    Returns:
    list: A list of random integers.
    """
    return [r.randint(lower_bound, upper_bound) for _ in range(num_points)]


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

def print_box_plot_stats(data):
    """
    Print the five-number summary for a list of numbers.

    Parameters:
    data (list): A list of numerical values.
    """
    stats = box_plot_stats(data)
    print(f"Min: {stats['min']}")
    print(f"Q1: {stats['Q1']}")
    print(f"Median: {stats['median']}")
    print(f"Q3: {stats['Q3']}")
    print(f"Max: {stats['max']}")

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

def generate_Test_Questions():
    f = open("boxPlotTestQuestions.txt", "w")
    for i in range(10, 23, 4):
        for j in range(4):
            myList = generate_random_data(i)
            f.write('Data Set: ')
            for item in myList:
                f.write(str(item) + ' ')
            f.write('\n'*2)
            stats = box_plot_stats(myList)
            f.write(f"Min: {stats['min']}\n")
            f.write(f"Q1: {stats['Q1']}\n")
            f.write(f"Median: {stats['median']}\n")
            f.write(f"Q3: {stats['Q3']}\n")
            f.write(f"Max: {stats['max']}\n")
            f.write('\n'*3)

    
def main():
    generate_Test_Questions()



#### End of Main ####


if __name__ == "__main__":
    main()
