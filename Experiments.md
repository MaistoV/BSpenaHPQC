# Experiments

* variables of interest : num threads, num mappers, num reducers
* independent factors :
* Input : worload DFSIO (lanciati in parallelo agli script di misura)

## DFSIO
DFSIO<sup>[[18]](References.md#dfsio)</sup><sup>[[19]](References.md#benchmark)</sup> is a built-in benchmark tool for HDFS I/O test, it runs a MapReduce job.

```bash
$ hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -read | -write | -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```

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


The read test of TestDFSIO does not generate its own input files. For this reason, it is a convenient practice to first run a write test via -write and then follow-up with a read test via -read (while using the same parameters as during the previous -write run).


## ?????
* Web UI
  * NameNode - http://localhost:9870/
  * DataNode -  http://localhost:9864/
  * ResourceManager - http://localhost:8088/
  * JobHistory - http://localhost:19888/ ???
      * in map-site.xml
      ```xml
        <property>
            <name>mapreduce.jobhistory.webapps.address</name>
            <value>localhost:19888</value>
        </property>
      ```
* Logs : Into /logs directory


## Experiments Steps ???
All experiments follow this steps :
1. Configuration of 
    * Selected parameters
    * YARN ???
    * EC ???
1. Execution of the experiment : 
    * Start daemons
    * Execute commands 4-5 (https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html)
    * Execute dfsio test
    * Stop all deamons
1. Analysis of the variables of interest 

Note : All experiments have the parameter configuration described in https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html


## Experiment 1
* parameters : 
  * dfs.datanode.handler.count : 20 
  * mapreduce.job.reduces : 2
  * mapreduce.reduce.resource.vcores : 2

* dfsio
  * write
  * nrFiles 16
  * fileSize 200MB

bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -write -nrFiles 16 -fileSize 200MB

* Number of map tasks : 16 (terminal output)


## Experiment 

* parameters : 
  * dfs.datanode.handler.count : 20 
  * mapreduce.job.reduces : 2
  * mapreduce.reduce.resource.vcores : 2

* dfsio
  * read
  * nrFiles 16
  * fileSize 200MB

bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -read -nrFiles 16 -fileSize 200MB

* Number of map tasks : 16 (terminal output)



## Comandi utili
* bin/yarn application -list
* bin/yarn application -status <appID>
* bin/mapred job -list all

## Note
* yarn.resourcemanager.scheduler.class : org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler (non mi permette di avviare il resourcemenager) <sup>[[20]](References.md#fair_scheduler)</sup>

* EC policy : RS-10-4-1024k   <sup>[[5]](References.md#EC)</sup>

```bash
$ hdfs ec -enablePolicy -policy RS-10-4-1024k
```
Settata la policy, ho un errore per cui il cluster non supporta il tipo di policy visto che richiede un numero maggiore di nodi (14)