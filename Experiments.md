# Test Cases Script
The script is designed to run on a node set in **Pseudo-distributed Mode**. To run the script you need to set up the **test cases** in the in *test_list.csv* file; along the rows are set the test cases, while parameters are set along the columns. There are two types of parameters :
* **cluster configuration parameters** for the three Hadoop layers :
    * [HDFS](Parameters.md#hdfsparanalysis)
    * [MapReduce](Parameters.md#maprredparanalysis)
    * [YARN](Parameters.md#yarnparanalysis)
* **DFSIO benchmark parameters and values**<sup>[[19]](References.md#dfsio)</sup><sup>[[20]](References.md#benchmark)</sup> :
  * **-write** : Runs the write test.
  * **-read** : Runs the read test.
  * **-nrFiles** : The number of files (equal to the number of map tasks).
  * **-fileSize** : The size of a file to generate B|KB|MB|GB|TB is allowed.
  * **-resFile** : Set the file name where the results will be saved.
  * **-bufferSize** : The buffer size flag describes the length of the write buffer in bytes.

The results of each test case will be saved in the rows of *test_result.csv* file.

> [!NOTE]
> By deafult the results are saved in TestDFSIO_results.log file in /benchmarks/TestDFSIO directory.
>
> The read test of TestDFSIO does not generate its own input files. For this reason, it is a convenient practice to first run a write test and then follow-up with a read test (using the same parameters).

## Script Description <a name="scriptdesc"></a>
The script execution following steps.

### Step 0
Variables and structures needed

### Step 1
Reads *test_list.csv* file and saves the parameters in a dataframe; for each dataframe row are executed the steps from 2 to 6.

### Step 2
Configures the Hadoop clusters by setting **-site.xml* files.

### Step 3
Start the cluster in pseudo-distributed mode : (using os module)
  * Stop HDFS deamons,YARN deamons and JobHistoryServer
  ```bash
  $ $HADOOP_HOME/sbin/stop-dfs.sh
  $ $HADOOP_HOME/sbin/stop-yarn.sh
  $ $HADOOP_HOME/sbin/mr-jobhistory-daemon.sh --config $HADOOP_HOME/etc/hadoop stop historyserver
  ```
  * Format the filesystem
  ```bash
  $ $HADOOP_HOME/bin/hdfs namenode -format
  ```
  * Start HDFS deamons,YARN deamons and JobHistoryServer
  ```bash
  $ $HADOOP_HOME/sbin/start-dfs.sh
  $ $HADOOP_HOME/sbin/start-yarn.sh
  $ $HADOOP_HOME/sbin/mr-jobhistory-daemon.sh --config $HADOOP_HOME/etc/hadoop start historyserver
  ```
  * Make the HDFS directories required to execute MapReduce jobs
  ```bash
  $ $HADOOP_HOME/bin/hdfs dfs -mkdir /user
  $ $HADOOP_HOME/bin/hdfs dfs -mkdir /user/$(whoami)
  ```

### Step 4 
Start the DFSIO test
```bash
$ $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -read | -write [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```

### Step 5
Start the measurement scripts and saves the results in *test_result.csv* file. (using subprocess module)

SCrivere python 3.10

### Step 6
Clean up test results using the same values used for run the test
```bash
$ $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```


### Tenere conto di 
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>


## ????
Motivare la scelta dei fattori (scheduling/calcolo) e le variabili di risposta (tempistiche)
* **Indipendent Factors** : 
  * dfs.namenode.handler.count
  * dfs.datanode.handler.count
  * mapreduce.job.reduces
  * mapreduce.reduce.cpu.vcores
  * yarn.scheduler.minimum-allocation-vcores
  * yarn.scheduler.maximum-allocation-vcores
  * yarn.resourcemanager.scheduler.class
* **Response variables** : 
  * number of map tasks
  * execution time of the job (elapsed time)
  * vcores allocated for the application
  * memory allocated for the application
  * execution time of the map tasks
  * execution time of the reduce tasks

* Motivare scelta parametri applicacioni
* Definire job/applicazione nell'intro di hadoop

## Comandi di misura
* bin/yarn application -list
* bin/yarn application -status <appID>
* bin/mapred job -list all
* bin/mapred job -history <jobID>
* bin/mared job -status <jobID>


## ???
* Web UI
  * NameNode - http://localhost:9870/
  * DataNode -  http://localhost:9864/
  * ResourceManager - http://localhost:8088/
  * JobHistory - http://localhost:19888/
     
* Logs : Into /logs directory


$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -write -nrFiles 16 -fileSize 100MB