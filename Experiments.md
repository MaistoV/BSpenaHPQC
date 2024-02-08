# Experiments

* variables of interest : num threads, num mappers, num reducers
* independent factors :
* Input : worload DFSIO (lanciati in parallelo agli script di misura)


## Web GUI
* NameNode - http://localhost:9870/
* DataNode -  http://localhost:9864/
* ResourceManager - http://localhost:8088/
19888 --> JobHistory

## Log
Into /logs directory

## DFSIO
DFSIO<sup>[[18]](References.md#dfsio)</sup> is a built-in benchmark tool for HDFS I/O test, it runs a MapReduce job.

hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -read | -write | -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]

* Flags
-nrFiles: the number of files (equal to the number of map tasks)
-fileSize: the size of a file to generate B|KB|MB|GB|TB is allowed
-resFile : set the file name where the results will be saved, by deafult the results are saved in TestDFSIO_results.log file in /benchmarks/TestDFSIO directory
-bufferSize : The buffer size flag describes the length of the write buffer in bytes
-write
-read
-clean

* Write test
hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.7.1.jar TestDFSIO -write -nrFiles 16 -fileSize 1GB -resFile /tmp/$USER-dfsio-write.txt

* Read test
hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.7.1.jar TestDFSIO -read -nrFiles 16 -fileSize 1GB -resFile /tmp/$USER-dfsio-read.txt

* Clean up 
Don’t forget to clean up test results after the completion, otherwise available storage space will be consumsed by the benchmark output files
hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.7.1.jar TestDFSIO -clean

* If there are outputs, use fs commands to see the contents e.g.
hadoop fs -cat /benchmarks/TestDFSIO/io_write/part*


## YARN Configuration
Fair scheduler configuartion --> two files : yarn-site.xml and Fair-scheduler.xml used to configure ResourceMenager and NodeMenager

The configuration file must be set for all the nodes in the cluster 
yarn-site.xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
</property>


fair-scheduler.xml
<?xml version="1.0"?>
<allocations>
  <queue name="sample_queue">
    <minResources>10000 mb,0vcores</minResources>
    <maxResources>90000 mb,0vcores</maxResources>
    <maxRunningApps>50</maxRunningApps>
    <maxAMShare>0.1</maxAMShare>
    <weight>2.0</weight>
    <schedulingPolicy>fair</schedulingPolicy>
    <queue name="sample_sub_queue">
      <aclSubmitApps>charlie</aclSubmitApps>
      <minResources>5000 mb,0vcores</minResources>
    </queue>
    <queue name="sample_reservable_queue">
      <reservation></reservation>
    </queue>
  </queue>
  
  <queueMaxAMShareDefault>0.5</queueMaxAMShareDefault>
  <queueMaxResourcesDefault>40000 mb,0vcores</queueMaxResourcesDefault>
</allocations>

## Experiment 1

* configurare i parametri scelti
* Configurare yarn
* configurare ec
* avviare dfsio