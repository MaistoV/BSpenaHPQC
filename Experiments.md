# Experiment Script

## Introdution <a name="scriptintro"></a>
The experiment script has two phases:
* Configuration Phase
* Execution Phase


?????? Note : All experiments have the parameters configuration described in https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html

## Configuration Phase <a name="confphase"></a>
During this phase, the user will set the parameters in the *test_list.csv* file :
* **Configuration parameters** per the three Hadoop layers :
    * [HDFS](Parameters.md#hdfsparanalysis)
    * [MapReduce](Parameters.md#maprredparanalysis)
    * [YARN](Parameters.md#yarnparanalysis)
* **DFSIO Benchmark parameters and values**<sup>[[17]](References.md#dfsio)</sup><sup>[[18]](References.md#benchmark)</sup> :
  * **-write** : Runs the write test.
  * **-read** : Runs the read test.
  * **-nrFiles** : The number of files (equal to the number of map tasks).
  * **-fileSize** : The size of a file to generate B|KB|MB|GB|TB is allowed.
  * **-resFile** : Set the file name where the results will be saved.
  * **-bufferSize** : The buffer size flag describes the length of the write buffer in bytes.

> [!NOTE]
> By deafult the results are saved in TestDFSIO_results.log file in /benchmarks/TestDFSIO directory.
>
> The read test of TestDFSIO does not generate its own input files. For this reason, it is a convenient practice to first run a write test and then follow-up with a read test (using the same parameters).


## Execution Phase <a name="exphase"></a>
The execution script follows these steps : 
1. Stop hdfs and yarn deamons
  ```bash
    $ sbin/stop-dfs.sh
    $ sbin/stop-yarn.sh
  ```

2. Read test_list.csv file 
    * Save the parameters in a structure (dictionary/dataframe ???)

3. Comparing parameters to identify the *-site.xml file

4. Start the cluster in pseudo-distributed mode
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

5. Start the DSFIO test :
```bash
$ hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -read | -write [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```
6. Start the measurement scripts
    * Read the results in different structures (dictionary/dataframe ???)
    * Write results in test_result.csv

7. Clean up test results using the same values used for run the test
```bash
$ hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```



## Experiments 
### 1
* parameters : 
  * dfs.datanode.handler.count : 20 
  * mapreduce.job.reduces : 2
  * mapreduce.reduce.resource.vcores : 2
* dfsio
  * write
  * nrFiles 16
  * fileSize 200MB
* bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -write -nrFiles 16 -fileSize 200MB
* Number of map tasks : 16 (terminal output)

### 2
* parameters : 
  * dfs.datanode.handler.count : 20 
  * mapreduce.job.reduces : 2
  * mapreduce.reduce.resource.vcores : 2
* dfsio
  * read
  * nrFiles 16
  * fileSize 200MB
* bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -read -nrFiles 16 -fileSize 200MB
* Number of map tasks : 16 (terminal output)

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