import pandas
from matplotlib import pyplot as plt 
import numpy as np
from scipy.interpolate import CubicSpline

def find_median(df_test_result,string):
    median_list = []
    i = 1       
    j = 9

    while(j <= 81):
        lower_bound = 'test' + str(i)
        upper_bound = 'test' + str(j)
        group = df_test_result.loc[lower_bound : upper_bound]   # Extract the rows            
        median_list.append(group[string].median())              # Add the median of the choosen row to the list
        i = i + 9
        j = j + 9

    return median_list


def stacked_bar_plot(cpu_mt_median,cpu_rt_median):    
    fig = plt.figure(figsize=(8,6))
    ax = plt.axes()
    ax.set_title('CPU Time Spent')
    ax.grid(linestyle='--', color='0.75', axis = 'y')
    ax.set_axisbelow(True)                                         # Grid behind the bars
    width = 0.75                                                   # Bar width

    test_numbers =  []
    for i in range(1,len(cpu_mt_median)+1):
        string = 'Test ' + str(i)
        test_numbers.append(string)

    cpu_mt_plot = ax.bar(test_numbers, cpu_mt_median, width, label='cpu.time.map.task')
    cpu_rt_plot = ax.bar(test_numbers, cpu_rt_median, width, bottom= cpu_mt_median,label='cpu.time.reduce.tasks')

    ax.bar_label(cpu_mt_plot, label_type='center')                 # Show the values inside the bars                     
    ax.bar_label(cpu_rt_plot, label_type='center')    
                                                                                   
    ax.legend()
    ax.bar_label(cpu_rt_plot)                                      # Show the sum of the values above the bars


def line_plot(throughput_median,average_io_median):
    x=np.linspace(1,9,9)   
    
    fig = plt.figure()
    ax_t = plt.axes()
    ax_t.set_title('Throughput mb/s')
    ax_t.set_xlabel('Test Numbers')                 
    ax_t.set_ylabel('Throughput')
    ax_t.grid(linestyle='--', color='0.85')                                                   
    ax_t.plot(x,throughput_median, color="red") 

    fig = plt.figure() 
    ax_a = plt.axes()
    ax_a.set_xlabel('Test Numbers')                 
    ax_a.set_ylabel('Average IO')
    ax_a.set_title('Average IO mb/s')
    ax_a.grid(linestyle='--', color='0.85')
    ax_a.plot(x,average_io_median, color="blue")   


if __name__=='__main__':

    df_test_result = pandas.read_csv('test_result.csv')                 

    tests_number = []
    for i in range(1,len(df_test_result.index)+1):
        string = 'test' + str(i)
        tests_number.append(string)

    df_test_result.index = tests_number

    cpu_mt_median = find_median(df_test_result,'cpu.time.map.task')
    cpu_rt_median = find_median(df_test_result,'cpu.time.reduce.tasks')
    throughput_median = find_median(df_test_result,'throughput_value')
    average_io_median = find_median(df_test_result,'average_io_value')

    stacked_bar_plot(cpu_mt_median,cpu_rt_median)
    line_plot(throughput_median,average_io_median)
    plt.show()