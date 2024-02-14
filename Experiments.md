# Test Cases Script

## Introdution <a name="scriptintro"></a>
The script is designed to run on a node set in **Pseudo-distributed Mode**. To run the script you need to set up the **test cases** in the in *test_list.csv* file; along the rows are set the teste cases, while parameters are set along the columns. There are two types of parameters :
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

### Step 1
Reads *test_list.csv* file and saves the parameters in a dataframe; for each dataframe row are executed the steps from 2 to 6.

### Step 2
Configures the Hadoop clusters by setting **-site.xml* files.

### Step 3
Start the cluster in pseudo-distributed mode : 
  * Stop hdfs and yarn deamons
    ```bash
  $ sbin/stop-dfs.sh
  $ sbin/stop-yarn.sh
    ```
  * Format the filesystem
  ```bash
  $ bin/hdfs namenode -format
  ```
  * Start hdfs and yarn deamons
  ```bash
  $ sbin/start-dfs.sh
  $ sbin/start-yarn.sh
  ```
  * Make the HDFS directories required to execute MapReduce jobs
  ```bash
  $ bin/hdfs dfs -mkdir /user
  $ bin/hdfs dfs -mkdir /user/<username>
  ```
  * Copy the input files into the distributed filesystem
  ```bash
  $ bin/hdfs dfs -mkdir input
  $ bin/hdfs dfs -put etc/hadoop/*.xml input
  ```

### Step 4 
Start the DSFIO test
```bash
$ bin/hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -read | -write [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```

### Step 5
Start the measurement scripts and saves the results in *test_result.csv* file. 

### Step 6
Clean up test results using the same values used for run the test
```bash
$ bin/hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```


## ????
* **Indipendent Factors** : 
  * dfs.namenode.handler.count
  * dfs.datanode.handler.count
  * mapreduce.job.reduces
  * mapreduce.reduce.resource.vcores
  * yarn.scheduler.minimum-allocation-vcores
  * yarn.scheduler.maximum-allocation-vcores
  * yarn.resourcemanager.scheduler.class
* **Response variables** : 
  * number of map tasks
  * timeout for each map task
  * timeout for each reduce task
  * vcores allocated for the job execution
  * memory allocated for the job execution
  * bandwidth


## Comandi di misura
* bin/yarn application -list
* bin/yarn application -status <appID>
* bin/mapred job -list all


## ???
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