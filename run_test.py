if __name__=='__main__':
#1 Stop hdfs and yarn deamons

#2 Read test_list.csv file 
    #2.1 Save the parameters in a structure (dictionary/dataframe ???)

#3 Parameters configuration in *-site.xml file
    #3.1 Comparing parameters to identify the right xml file

    # Solution 1: Comparing name fild with strings such as "dfs","mapreduce" and "yarn"
    for i in parameters :                       # Parameters is a dummy structure
        if "dfs" in parameters.name :           # Parameters.name is the name field 
                save_to_hdfs_site()             # Start the right function for the parameters configuration
        # same goes for mapreduce and yarn

    # Solution 2: Comparing parameters with https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml
    # (same goes for mapreduce/yarn-default.xml)

#4 Start the cluster in pseudo-distributed mode
    #4.1 Format the filesystem
    #4.2 Start hdfs and yarn deamons
    #4.3 Make the HDFS directories required to execute MapReduce jobs
    #4.4 Copy the input files into the distributed filesystem

#5 Start the DSFIO test

#6 Start the measurement scripts
    #6.1 Read the results in different structures (dictionary/dataframe ???)
    #6.2 Write results in test_result.csv