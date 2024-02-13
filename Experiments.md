# Experiment Script

## Introdution <a name="scriptintro"></a>
The experiment script has two phases:
* Configuration Phase
* Execution Phase

## Configuration Phase <a name="confphase"></a>
During this phase, the user will set the parameters in the *test_list.csv* file. 


## Execution Phase <a name="exphase"></a>



1. Definire la lista test da eseguire in termini di parametri in un file di configurazione (test_list.csv):
    1.1. Scegli uno o più parametri di configurazione per due/tre dei sottosistemi principali di Hadoop (tra YARN, MapReduce, NameNode, DataNode).
    1.2. Scegli i parametri e valori della suite di benchmark, e.g. una tra DFSIO, Terasort, nnbench, etc. (-read/write, -nrFiles, –fileSize, etc).
    1.3. In generale, non esagerare nè con i parametri, nè con i livelli degli stessi. Per questa PoC, limitiamoci a valori binari, e.g. yarn.scheduler.maximum-allocation-vcores={4,8}.
    1.4. Nota che non ci interessano tutte le combinazioni di valori ed interazioni tra parametri (e.g. full-factorial design). L'importante è poter aggiungere una nuova riga o modificare un parametro e poter subito lanciare la nuova lista di test senza modificare null'altro che il primo file test_list.csv.
2. Da script (run_test.sh/py), per ogni riga del file test_list.csv:
    2.1. Configurare il sistema:
        2.1.1. Configurare Hadoop, modificando i parametri nei vari file *-site.xml e/o da linea di comando (come ti risulti più convenieninte). NB: assicurati che le modifiche abbiano effetto sul sistema, dato che per alcune potrebbe essere necessario riavviare yarn o tutto il DFS.
        2.1.2. Configurare la suite di benchmark (semplicemente settando delle variabili che poi andrai ad utilizzare nella chiamata alla suite).
    3.1. Eseguire il test chiamando la suite di benchmark.
    3.2. Raccogliere i valori delle variabili di risposta in una riga di un file CSV (test_result.csv).


## DFSIO <a name="dfsio"></a>
DFSIO<sup>[[18]](References.md#dfsio)</sup><sup>[[19]](References.md#benchmark)</sup> is a built-in benchmark tool for HDFS I/O test, it runs a MapReduce job. The syntax for running a DFSIO test is as follows:

```bash
$ hadoop jar $HADOOP_HOME/hadoop-*test*.jar TestDFSIO -read | -write | -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```
and each flag has a specific function :
* **-write** : Runs the write test.
* **-read** : Runs the read test.
* **-clean** : Runs the clean up of the results.
* **-nrFiles** : The number of files (equal to the number of map tasks).
* **-fileSize** : The size of a file to generate B|KB|MB|GB|TB is allowed.
* **-resFile** : Set the file name where the results will be saved, by deafult the results are saved in TestDFSIO_results.log file in /benchmarks/TestDFSIO directory.
* **-bufferSize** : The buffer size flag describes the length of the write buffer in bytes.

* If there are outputs, use fs commands to see the contents e.g.
hadoop fs -cat /benchmarks/TestDFSIO/io_write/part*



> [!NOTE]
> The read test of TestDFSIO does not generate its own input files. For this reason, it is a convenient practice to first run a write test and then follow-up with a read test (using the same parameters).




* variables of interest : num threads, num mappers, num reducers
* independent factors :
* Input : worload DFSIO (lanciati in parallelo agli script di misura)


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


## Experiments Steps ???  <a name="exsteps"></a>
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

Note : All experiments have the parameters configuration described in https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html


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


## Experiment 2

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