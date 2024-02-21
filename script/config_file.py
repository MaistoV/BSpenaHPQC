# Files path
path_hdfs_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/hdfs-site.xml'
path_mapred_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/mapred-site.xml'
path_yarn_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/yarn-site.xml'
path_test_list = 'test_list.csv'
path_test_result = 'test_result.csv'
path_test_dfsio_logs = 'TestDFSIO_results.log'

# String array with the number of tests
tests_numer = ['test1']

# Tuples with the parameters (same order as of test_list file)
hdfs_t = ('dfs.namenode.handler.count','dfs.datanode.handler.count')
mapred_t = ('mapreduce.job.reduces','mapreduce.reduce.cpu.vcores')
yarn_t = ('yarn.scheduler.minimum-allocation-vcores',)
dfsio_t = ('dfsio.nrFiles','dfsio.fileSize')


# String array with the colums names of test_result.csv
columns_name = ['maps.number','cpu.time.map.task','cpu.time.reduce.tasks','cpu.time.tot','throughput_value','avarege_io_value']



########################### DO NOT MODIFY ######################################

# String array with the special parameters needed for the cluster configuration in psuedo-distributed mode
special_parameters = ['dfs.replication','mapreduce.framework.name','mapreduce.application.classpath','yarn.nodemanager.aux-services','yarn.nodemanager.env-whitelist']  

