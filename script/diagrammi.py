import pandas
from matplotlib import pyplot as plt 
import numpy as np
import statistics


def find_mean(df_test_result,string):
    list = []
    i = 0       
    j = 8

    while(j <= 81):
        group = df_test_result.iloc[i : j]   # Extract the rows            
        list.append(statistics.mean(group[string]))             # Add the mean of the choosen row to the list
        i = i + 9
        j = j + 9

    return list


def bar_plot(y,title,x_label,y_label):    
    plt.figure(figsize=(6,5))
    ax = plt.axes()
    ax.bar([1,2,4],y,color='blue',width = 0.35)                    
    ax.set_title(title)                                  
    ax.set_xlabel(x_label)                 
    ax.set_ylabel(y_label)
 

def line_plot(y,title,x_label,y_label):  
    plt.figure(figsize=(6,5))
    ax = plt.axes()
    ax.set_title(title)
    ax.set_xlabel(x_label)                 
    ax.set_ylabel(y_label)
    ax.grid(linestyle='--', color='0.85')  
    x= [10,12,16]                                                 
    ax.plot(x,y, color='red') 


if __name__=='__main__':

    df_test_list = pandas.read_csv('test_list.csv')  
    df_test_result = pandas.read_csv('test_result.csv')                 

    tests_number = []
    for i in range(1,len(df_test_list.index)+1):
        string = 'test' + str(i)
        tests_number.append(string)

    df_test_list.index = tests_number
    df_test_result.index = tests_number

    df_total = pandas.concat([df_test_list, df_test_result], axis=1)    #Concatenate pandas objects along a particular axis
    df_total_sort = df_total.sort_values(by=['mapreduce.map.cpu.vcores','dfs.datanode.handler.count'])

    pandas.set_option('display.max_rows', None)                         # Display all dataframe rows
    #pandas.set_option('display.max_columns', None)                     # Display all dataframe columns

    # Mean values
    throughput_mean = find_mean(df_total_sort,'throughput_value')
    average_io_mean = find_mean(df_total,'average_io_value')
    cpu_mt_mean = find_mean(df_total,'cpu.time.map.task')
    # cpu_rt_mean = find_mean(df_total,'cpu.time.reduce.tasks')

    # Labels
    x_label_t_a = 'Number of Server Threads for DataNode'
    y_label_t = 'Throughput mb/s'

    x_label_cpu = 'Number of Server Threads for DataNode'
    y_label_cpu = 'Throughput mb/s'
      
    # Line Plots Throughput
    line_plot(throughput_mean[0:3],'Throughput (1 Vcore for each Map Task)',x_label_t_a,y_label_t)
    line_plot(throughput_mean[3:6],'Throughput (2 Vcores for each Map Task)',x_label_t_a,y_label_t)
    line_plot(throughput_mean[6:9],'Throughput (4 Vcores for each Map Task)',x_label_t_a,y_label_t)

    # Line Plots Average IO
    line_plot(average_io_mean[0:3],'Average IO rate (1 Vcore for each Map Task)',x_label_t_a,y_label_t)
    line_plot(average_io_mean[3:6],'Average IO rate (2 Vcores for each Map Task)',x_label_t_a,y_label_t)
    line_plot(average_io_mean[6:9],'Average IO rate (4 Vcores for each Map Task)',x_label_t_a,y_label_t)

    # Bar Plots
    bar_plot(cpu_mt_mean[0:3],'CPU Time Spent by all Map Tasks (10 Server Threads for Datanode)',x_label_cpu,y_label_cpu)
    bar_plot(cpu_mt_mean[3:6],'CPU Time Spent by all Map Tasks (12 Server Threads for Datanode)',x_label_cpu,y_label_cpu)
    bar_plot(cpu_mt_mean[6:9],'CPU Time Spent by all Map Tasks (14 Server Threads for Datanode)',x_label_cpu,y_label_cpu)

    plt.show()