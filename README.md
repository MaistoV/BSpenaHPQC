# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni su DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.



# Apache Hadoop
Apache Hadoop software library <sup>[[1]](#1)</sup> <sup>[[2]](#2)</sup> is a **freamwork** used for the distributed processing of massive datasets across **clusters** of computers. It offers reliabily, scalability and fault-tolerance. Hadoop has these modules :
* **Hadoop Common** : The common utilities that support the other Hadoop modules
* **HDFS** : The distributed file system
* **MapReduce** : The data processing layer
* **Yarn** : The cluster resource management layer

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/04/Hadoop-Ecosystem-2-01.jpg" width="600">
</p>


## HDFS
HDFS (Hadoop Distributed File System)<sup>[[3]](#3)</sup> is a java-based distributed file system running on commodity hardware which supports a traditional hierarchical file organization. This file system :
* Stores user data in files.
* Splits file in one or more blocked-sized chunks known as **data blocks**,with size of 128 MB by default (the size is configurable per file).  
* Replicates the data blocks. The replication factor is three by default, but it can be configurable per file.
* Supports **write-once-read-many** access model for on files. After closing a fila, it cannnot be updated at any point, but content can be append at the end.
* Support the **snapshot** to execute a roll back of a corrupted istance

HDFS has a **master-slave architecture** :
* **NameNode** : There is one master per cluster, it executes file system namespace operations (opening, closing, and renaming files and directories) and handles clients access to files. The NameNode assigns the blocks to DataNodes and stores the metadata (number of data blocks,their locations,numeber of replicas, etc...). Finally, it makes all decisions regarding blocks replication.
* **DataNode**  : There is one slave per node in the cluster, it executes read/write operation from the file system’s client. The DataNode performs data blocks operations (creation, deletion and replication) and stores the actual data. Moreover, DataNodes ara gathered together in **racks**.

<p align="center">
  <img src="https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png" width="600">
</p>

Note that the architecture can be **rebalanced** moving data from one Datanode to another.
HDFS provides :
* Data reliability.
* Data availability.
* Data Locality.
* A fault-tolerant system.

### Erasure Coding
The 3x replication generates an 200% overhead in storage space and other resources. An alterntive method is the **erasure coding**<sup>[[4]](#4)</sup>, which provides the same level of fault-tolerance with much less storage space.  
**Redundant Array of Inexpensive Disks (RAID)** implements the eresure coding by diving logically sequantial data (such as file) into smaller units and stores consecutive units on differnt disks. 


## MapReduce 
MapReduce<sup>[[5]](#5)</sup> is a software framework for writing applications (which need not be written in Java) that process large datasets in parallel on large clusters. The framework :
* Operates on sets of **<key,value> pairs**.
* Splits the data into **InputSplit** in order to be processed. 
* Starts up many copies of the program on the nodes of the cluster, the copies are divided into :
  * **Master** : There is only one master who assigns each worker a **map task** or a **reduce task**. MapReduce creates a map task for each InputSplit, instead the number of reduce task can be set by the user (set as zero if no reduction is desired).
  * **Workers** : Execute tasks. A worker is known as **mapper** if it is assigned a map task, insted it is known as **reducer** if it is assigned a reduce task.

Note that each map task uses a user-defined **map function** which is implemented through interfaces and/or abstract-classes, the same goes for each reduce task with a **reduce function**.

A **MapReduce job** is a complete execution of a **map phase** and a **reduce phase**<sup>[[6]](#6)</sup><sup>[[7]](#7)</sup> (a complete [MapReduce job execution flow](https://data-flair.training/blogs/how-hadoop-mapreduce-works/)) : 
* **Map Phase** : The mapper maps the input <key,value> pair to an **intermetdiate <key,value> pair**.
* **Shuffling and Sorting** : Occur simultaneously
  * **Shuffle Phase** : Fetches the values of the output of the mappers.
  * **Sort Phase** : Groups the intermediate pairs by keys.
* **Reduce Phase** : The reducer reduces set of intermediate values, which share a key, to a smaller set of values. The smaller set is the final output.

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/06/hadoop-mapreduce-flow.jpg" width="600">
</p> 

## YARN
YARN (Yet Another Resource Negotiator)<sup>[[8]](#8)</sup><sup>[[10]](#10)</sup> is the resource menagement layer. It allows the exectution of different kind of applications, like MapReduce job, DAG of job , Stream processing, etc... 

YARN architecture has the following components :
* **Client** : Submits the application <sup>[[9]](#9)</sup> to the ResourceManager.
* **ResourceManager** : The **master daemon** manages the resources among all the applications in the system. The ResourceManager has two main components :
    * **Scheduler** : It is a pure scheduler (does not perform monitoring or tracking of the applications' status), it allocates resources to the running applications.
    * **ApplicationsManager** : Accepts job submissions and secures resources on a node (an operation known as "**negotiating the first container**") to launch the ApplicationMaster
* **NodeManager** : The **slave deamon** launches, manages and monitors resource usage of the containers on a node. The containers execute tasks as specified by the ApplicationMaster.
* **ApplicationMaster** : It is a framework specific library, so there is one per application. The ApplicationMaster works with the NodeManager to execute and monitor the tasks. 

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/05/Apache-YARN-architecture-min.jpg" width="600">
</p> 

The pair ResourceManager/NodeManager rapresents the **data-computation framework**.



# Implementation
## Environment Setup
* Virtual machine running Ubuntu 22.04 LTS :
  * 8 GB of RAM 
  * 4 cores
  * 150 GB of memory
* Tools :
  * [Java 1.8](https://linuxize.com/post/install-java-on-ubuntu-22-04/#uninstalling-java)
  * [Hadoop 3.3.5](https://www.adaltas.com/en/2020/08/04/installing-hadoop-from-source/)
  * [Maven](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
  * Docker Container



# References
* <a id="1"></a> [[1] Apache Hadoop](https://hadoop.apache.org/)
* <a id="2"></a> [[2] Hadoop Ecosystem](https://data-flair.training/blogs/hadoop-ecosystem-components/)
* <a id="3"></a> [[3] HDFS Architecture](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
* <a id="4"></a> [[4] HDFS Erasure Coding](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)
* <a id="5"></a> [[5] MapReduce Tutorial](https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
* <a id="6"></a> [6] "MapReduce: Simplified Data Processing on Large Cluster",Jeffrey Dean,Sanjay Ghemawat
* <a id="7"></a> [[7] Hadoop MapReduce Flow – How data flows in MapReduce?](https://data-flair.training/blogs/hadoop-mapreduce-flow/)
* <a id="8"></a> [[8] Apache Hadoop YARN](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/YARN.html)
* <a id="9"></a> [[9] Hadoop: Writing YARN Applications](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/WritingYarnApplications.html)
* <a id="10"></a> [[10] Hadoop Yarn Tutorial for Beginners](https://data-flair.training/blogs/hadoop-yarn-tutorial/)


# References non usate
* https://data-flair.training/blogs/hadoop-architecture/
* https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
* https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/
* https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/
* https://data-flair.training/blogs/learn-hadoop-hdfs-fault-tolerance/
* https://maven.apache.org/


## Note 
* Per configurare la dimensione del block modificare la proprietà dfs.block.size in hdfs-site.xml (https://data-flair.training/blogs/data-block/)
* In [6] parla di Hadoop Streaming, utility che permette di creare ed eseguire job con qualsiasi eseguibile e di creare mapper e reducer
* In [6] indica quali interfacce devono essere implementate dalle classi key e value
 
# Cose da fare
* Installare Hadoop (sorgente github)
* Creare un cluster virtuale a container (build con Maven)
* Setup del cluster virtuale su singolo nodo
* Cambiare parametri di configurazione di Yarn
* Misurare i fattori all'interno dei wrokload
* Gli script generati devono essere portati sul cluster fisico