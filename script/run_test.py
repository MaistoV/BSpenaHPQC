import config_file as conf                        # Variables module
import functions as func                          # Functions module
import os


if __name__=='__main__':

    #Step 1: Create one dataframe from test_list.csv and one needed for test_result.csv
    print("Step 1: Create dataframes\n")
    df_test_list,df_test_result = func.create_dataframe(conf.path_test_list,conf.tests_numer,conf.path_test_result,conf.columns_name)             

    for i,row in df_test_list.iterrows():

        # Index to increase the rows in the TestDFSIO log file 
        index_log = int(i.split('test')[1]) - 1
        
        #Step 2: Cluster configuration by setting **-site.xml* files
        print("Step 2: Cluster Configuration \n")
        func.config_cluster(conf.path_hdfs_site,conf.hdfs_t,conf.path_mapred_site,conf.mapred_t,conf.path_yarn_site,conf.yarn_t,row,conf.special_parameters)
        
        #Step 3: Start the cluster in pseudo-distributed mode
        print("Step 3: Start the cluster in pseudo-distributed mode")
        os.system('./start_cluster.sh')
        print("\n")

        #Step 4: Start the DFSIO test
        print("Step 4: Start the TestDFSIO")
        func.create_dfsio(row,conf.dfsio_t)
        print("\n")
                                
        #Step 5: Start the offline test
        print("Step 5: Start the Offline Test")
        func.start_offline_test(index_log,conf.path_test_dfsio_logs,df_test_result,conf.path_test_result,conf.columns_name)
        print("\n")

        #Step 6: Clean up test results 
        print("Step 6: Clean up test results")
        os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')