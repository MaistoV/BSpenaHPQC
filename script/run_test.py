import config_file as conf                       # Variables module
import functions as func                         # Functions module
import os
import pandas

if __name__=='__main__':

    print("Step 1: Create dataframes\n")
    df_test_list,df_test_result,df_comm_line,df_dfsio_logs = func.create_dataframe(conf.path_test_list)             

    for i,row in df_test_list.iterrows():
 
        index = int(i.split('test')[1]) - 1                 # Index to increase the dataframe rows of the test via command line 
        
        print("Step 2: Cluster Configuration \n")
        func.config_cluster(conf.path_hdfs_site,conf.hdfs_t,conf.path_mapred_site,conf.mapred_t,conf.path_yarn_site,conf.yarn_t,row,conf.special_parameters)
        
        print("Step 3: Start the cluster in pseudo-distributed mode")
        os.system('./start_cluster.sh')
        print("\n")

        print("Step 4: Start the TestDFSIO")
        func.create_dfsio(row,conf.dfsio_t)
        print("\n")
                                
        print("Step 5: Start the Offline Test (mapreduce commands)")
        func.mapred_commands(df_comm_line,index,conf.cn_comm_line)
        print("\n")


        print("Step 6: Clean up TestDFSIO results")
        os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')
        print("\n")


    print("Step 7: Read the response variables from TestDFSIO logs  ")
    for index in range(0,len(df_test_list.index)):
        func.test_dfsio_logs(index,conf.path_test_dfsio_logs,df_dfsio_logs,conf.cn_dfsio_logs)

    print("\n")

    print("Step 8: Plot and save response variables on test_result.csv")
    func.plot_save(df_test_result,conf.path_test_result,df_comm_line,df_dfsio_logs)