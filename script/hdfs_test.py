import sys
import hdfs_test_config as config                # HDFS test configuration file
import hdfs_test_utils as utils                  # Utility functions

if __name__=='__main__':
    print("STEP 0: Check enviroment and user configuration")
    # Check Python version
    assert sys.version_info >= (3, 10), "Use Python 3.10 or newer"

    # Check test_list configuration
    utils.assert_config()

    # Read parameters from config file
    print("STEP 1: Create dataframes")
    df_test_list, df_test_result, df_mapred_commands, df_dfsio_logs = utils.initTest()

    # For each row in df_test_list
    for i,row in df_test_list.iterrows():
        print("\n")

        # test_index to increase the dataframe rows of the test via command line
        test_index = int(i.split('test')[1]) - 1                 
        print("Test n. " + i.split('test')[1] + "/" + str(df_test_list.shape[0]) )
    
        # Configure cluster
        print("STEP 2: Cluster Configuration \n")
        utils.configCluster( row )
        
        # # Start cluster
        # print("STEP 3: Start the cluster in pseudo-distributed mode")
        # utils.startCluster()
        # print("\n")

        # Start on-line tests
        # print("STEP 4: Start the TestDFSIO and Online Test")
        # utils.onlineTest( row )
        # print("\n")

        # # Start off-line tests
        # print("STEP 5: Start the Offline Test")
        # utils.offlineTest(
        #     test_index,
        #     df_mapred_commands,
        #     df_dfsio_logs,
        #     )
        # print("\n")

        # Clean-up
        # print("STEP 6: Clean up TestDFSIO results")
        # utils.cleanUp(
        #         config.path_test_dfsio_logs
        #     )
        # print("\n")     

        # # Write out
        # print("STEP 7: Save response variables on" + config.path_test_result)
        # utils.saveResults(
        #         config.path_test_result,
        #         df_test_result,
        #         df_mapred_commands,
        #         df_dfsio_logs
        #     )