import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def grouped_bar_graph_var(input_data, labels, x_axis, y_axis, var_div, title):
        '''
            Creates bar graphs that show the min, mean, max, and variance of all labels in the dataset

            Args:
                input_data (Pandas Series): each label and its assocated data as a list

                labels (list): the list of keys

                x_axis (str): title of x-axis

                y_axis (str): title of y-axis
            
            Returns:
                None: shows bar graph
        '''
        assert isinstance(input_data, pd.Series), 'input_data must be a pandas series'
        assert isinstance(labels, list), 'lables must be a list'
        for l in labels:
             assert isinstance(l, str), 'each value in the labels must be a string'
        assert isinstance(var_div, int), 'div_int must be a int'
        assert var_div > 0, 'div_int must be non zero'
        assert isinstance(title, str), 'title must be a string'
        assert isinstance(x_axis, str), 'x_axis must be a string'
        assert isinstance(y_axis, str), 'y_axis must be a string'

        compare_charging_data = []
        cities = labels
        city_labels = []
        colors = ['red', 'blue', 'green', 'cyan', 'orange', 'purple', 'coral', 'pink']
        colors = colors[:len(labels)]

        var_loc = input_data.apply(lambda temps: np.var(temps))
        

        for i, city in enumerate(cities):
            rates = input_data[city]
            var = var_loc[city]
            compare_charging_data.extend([min(rates), np.mean(rates), max(rates), var/var_div])
            city_labels.extend([city] * 4)

        plt.figure(figsize=(10, 6))

        bar_width = 0.8
        positions = np.arange(len(compare_charging_data))

        for i, city in enumerate(cities):
            city_position = positions[i * 4: (i + 1) * 4]
            plt.bar(city_position, compare_charging_data[i * 4:(i + 1) * 4], 
                    color=colors[i], edgecolor='black', width=bar_width)

        plt.title(f'{title} (Min, Mean, Max, Var/{var_div})')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)

        plt.xticks(ticks=np.arange(0, len(compare_charging_data), 4), labels=cities, rotation=0)
        plt.tight_layout()
        return plt
