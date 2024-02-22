import config_file as cf                        # Variables module
import functions as f                           # Functions module
import os


if __name__=='__main__':

    #Step 1: Read test_list.csv and test_result.csv files
    print("Step 1: Read test_list.csv and test_result.csv\n")
    df_test_list = f.read_csv(cf.path_test_list,cf.tests_numer,cf.path_test_result,cf.columns_name)             

    for i,row in df_test_list.iterrows():

        # Index to increase the rows in the TestDFSIO log file 
        index_log = int(i.split('test')[1]) - 1
        
        #Step 2: Cluster configuration by setting **-site.xml* files
        print("Step 2: Cluster Configuration \n")
        f.config_cluster(cf.path_hdfs_site,cf.hdfs_t,cf.path_mapred_site,cf.mapred_t,cf.path_yarn_site,cf.yarn_t,row,cf.special_parameters)
        
        #Step 3: Start the cluster in pseudo-distributed mode
        print("Step 3: Start the cluster in pseudo-distributed mode")
        os.system('./start_cluster.sh')
        print("\n")

        #Step 4: Start the DFSIO test
        print("Step 4: Start the TestDFSIO")
        f.create_dfsio(row,cf.dfsio_t)
        print("\n")
                                
        #Step 5: Start the offline test and save save response variables in *test_result.csv* file
        print("Step 5: Start the Offline Test")
        f.start_offline_test(index_log,cf.path_test_dfsio_logs,cf.path_test_result)
        print("\n")

        #Step 6: Clean up test results 
        print("Step 6: Clean up test results")
        os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')