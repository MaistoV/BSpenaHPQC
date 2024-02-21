import config_file as cf                        # Variables module
import functions as f                           # Functions module
import pandas
import os
import csv


if __name__=='__main__':

    #Step 1: Read test_list.csv file and saves the parameters in a dataframe
    print("Step 1: Read test_list.csv \n")
    dataframe = pandas.read_csv(cf.path_test_list)                  
    dataframe.index = cf.tests_numer

    #Step 1.1 : Define colums names of test_result.csv
    with open(cf.path_test_result,'a') as file:          
        writer=csv.writer(file)
        writer.writerow(cf.colums_name)

    for i,row in dataframe.iterrows():
        
        #Step 2: Cluster configuration by setting **-site.xml* files
        print("Step 2: Cluster Configuration \n")
        f.config_cluster(cf.path_hdfs_site,cf.hdfs_t,cf.path_mapred_site,cf.mapred_t,cf.path_yarn_site,cf.yarn_t,row,cf.special_parameters)
        
        #Step 3: Start the cluster in Pseudo-Distributed Mode
        print("Step 3: Start the cluster in pseudo-distributed mode")
        os.system('./start_cluster.sh')
        print("\n")

        #Step 4: Start the DFSIO test
        print("Step 4: Start the TestDFSIO")
        f.start_dfsio(row,cf.dfsio_t)
        print("\n")
                                
        #Step 5: Start the offline test and save save response variables in *test_result.csv* file
        print("Step 5: Start the Offline Test")
        f.start_offline_test(int(i.split('test')[1]),cf.path_test_dfsio_logs,cf.path_test_result)

        #Step 6: Clean up test results 
        print("Step 6: Clean up test results")
        os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')