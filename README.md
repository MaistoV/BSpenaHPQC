# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni su DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.
Il file system è virtualmente distribuito perché i vari componenti sono dei container.


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
* **NameNode** : There is one master daemon per cluster, it executes file system namespace operations (opening, closing, and renaming files and directories) and handles clients access to files. The NameNode assigns the blocks to DataNodes and stores the metadata (number of data blocks,their locations,numeber of replicas, etc...). Finally, it makes all decisions regarding blocks replication.
* **DataNode**  : There is one slave daemon per node in the cluster, it executes read/write operation from the file system’s client. The DataNode performs data blocks operations (creation, deletion and replication) and stores the actual data. Moreover, DataNodes ara gathered together in **racks**.

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
* **Shuffling and Sorting** (occur simultaneously) :
  * **Shuffle Phase** : Fetches the values of the output of the mappers.
  * **Sort Phase** : Groups the intermediate pairs by keys.
* **Reduce Phase** : The reducer reduces set of intermediate values, which share a key, to a smaller set of values. The smaller set is the final output.

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/06/hadoop-mapreduce-flow.jpg" width="600">
</p> 

## YARN
YARN (Yet Another Resource Negotiator)<sup>[[8]](#8)</sup><sup>[[9]](#9)</sup><sup>[[10]](#10)</sup> is a freamwork for distributed computing which separates resorse menagement and processing components. YARN :
* Allows the exectution of different kind of **applications**, like MapReduce job, DAG of job , Stream processing, etc... 
* Sends computations where the data is stored on locak disks (property of **data locality**)
* Uses the concept of containers. 
* Has a **master-worker nodes architecture**.

YARN architecture has the following components :
* **ResourceManager** : The **master daemon** runs on master node. It manages the resources among all the applications in the system. The daemon assigns tasks to the NodeManager and schedules containers. The ResourceManager has two main components :
    * **Scheduler** : It is a pure scheduler (does not perform monitoring or tracking of the applications' status), it allocates resources or container to the running applications.
    * **ApplicationsManager** : Accepts **job submissions** by the clients<sup>[[11]](#11)</sup> and secures resources on a node (an operation known as "**negotiating the first container**") to launch the ApplicationMaster.
* **NodeManager** : The **worker deamon** runs on the worker node. It launches, manages and monitors resource usage of the containers on a node.
* **ApplicationMaster** : It is a framework specific library, so there is one per application. The ApplicationMaster negotiates resources for the running application from the ResourceManager and works with the NodeManager to execute and monitor the tasks. 
* **Containers** : Collection of all the resources necessary to run an application, specified by the ApplicationMaster, on a node in a cluster.

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/05/Apache-YARN-architecture-min.jpg" width="600">
</p> 

ResourceManager/NodeManager rapresents the **data-computation framework**.

YARN supports the following schedulers :
* **FIFO** : Allocates resources based on arrival time.
* **Capacity scheduler** (default in hadoop) : Allocates resources to pools or queues, with FIFO scheduling to each pool.
* **Fair scheduler** : Organizes applications into queues or pools and allows to share resources fairly between quees (every application belongs to a queue).



# Implementation

## Environment Setup
### Overview
* Virtual machine running **Ubuntu 22.04 LTS** :
  * 8 GB of RAM 
  * 4 cores
  * 150 GB of memory
* **Tools** :
  * **Java 1.8**<sup>[[12]](#12)</sup>
  * **Hadoop 3.3.5**
  * **Maven 3.9.6**<sup>[[13]](#13)</sup>
  * **Docker Container**

### Tools Installation
#### Java 1.8
* Install Java via the following commands:
```bash
$ sudo apt update
$ sudo apt install openjdk-8-jdk
$ java -version                                 # Check java version 
```
* Setting the JAVA_HOME environment variable (necessary to install Maven) via the following commands:
```bash
$ sudo nano /etc/environment                    # Open the /etc/environment
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"   # Add this line to the end of the file
$ source /etc/environment                       # To take effect the changes
$ sudo reboot                                   # Restart the system
$ echo $JAVA_HOME                               # To verify is the variable is set correctly
```
#### Hadoop 3.3.5
```bash
$ git clone https://github.com/apache/hadoop.git --branch rel/release-3.3.5 --single-branch
```
#### Maven 3.9.6
* [Download Maven releases](https://maven.apache.org/download.cgi)
* Install Maven via the following commands :
```bash
$ unzip apache-maven-3.9.6-bin.zip        # Extract distribution archive in any directory
      
# Add the apache-maven-3.9.6 bin directory to the PATH environment variable
$ sudo nano /etc/environment              # Open the /etc/environment
":/path/to/apache-maven-3.9.6/bin"        # Add this line to PATH environment variable      
$ source /etc/environment                 # To take effect the changes
$ sudo reboot                             # Restart the system
$ echo $PATH                              # To verify is the variable is set correctly         

$ mvn -v                                  # Check maven version 
```
#### Docker Container

## Hadoop Cluster Setup
The Hadoop's cluster can be configured by setting <sup>[[14]](#14)</sup>:
* **Hadoop deamons exectuion environment** via read-only default configuration files :
  * core-default.xml.
  * hdfs-default.xml. 
  * yarn-default.xml.
  * mapred-default.xml.
* **Hadoop deamonds configuration parameters** via site-specific configuration files :
  * core-site.xml.
  * hdfs-site.xml.
  * yarn-site.xml.
  * mapred-site.xml.
* **Site-specific values** via : 
  * hadoop-env.sh.
  * yarn-env.sh.

In the next paragraph I will analyze a few **HDFS and YARN deamonds configurations parameters**.

### Configuring HDFS Deamons
<sup>[[14]](#14)</sup>

hdfs-site.xml

#### NameNode
dfs.blocksize is the HDFS blocksize
dfs.namenode.handler.count server threads to handle RPCs (Remote Procedure Call)

#### DataNode


### Configuring YARN Deamons
<sup>[[14]](#14)</sup>
yarn-site.xml

#### ResourceMenager
yarn.scheduler.minimum-allocation-mb  Minimum limit of memory to allocate to each container request at the Resource Manager. in MBs
yarn.scheduler.maximum-allocation-mb Maximum limit of memory to allocate to each container request at the Resource Manager. in MBs

#### NodeMenager
yarn.nodemanager.resource.memory-mb Defines total available resources on the NodeManager to be made available to running containers


<sup>[[]](#)</sup> ??????
MapReduce requests three different kinds of containers from YARN: the application master container, map containers, and reduce containers. For each container type, there is a corresponding set of properties that can be used to set the resources requested.  
yarn.app.mapreduce.am.resource.vcores	Sets the CPU requested for the application master container to the value. Defaults to 1.


# Cose da fare
* Documentare i principali parametri di configurazione di HDFS e YARN in hdfs-site.xml, yarn-site.xml, etc (ad esempio 3x replication, EC-config, #vcpus, memory per thread, etc.)
* Creare un cluster virtuale a container (build con Maven)
* Setup del cluster virtuale su singolo nodo
* Cambiare parametri di configurazione di Yarn
* Misurare i fattori all'interno dei wrokload
* Gli script generati devono essere portati sul cluster fisico


https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html


sudo apt-get -y install openjdk-8-jdk
sudo apt-get -y install maven
sudo apt-get -y install build-essential autoconf automake libtool cmake zlib1g-dev pkg-config libssl-dev libsasl2-dev
curl -L -s -S https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protobuf-java-3.7.1.tar.gz -o protobuf-3.7.1.tar.gz
mkdir protobuf-3.7-src
tar xzf protobuf-3.7.1.tar.gz --strip-components 1 -C protobuf-3.7-src && cd protobuf-3.7-src
./configure
make -j$(nproc)
sudo make install
# Optionals for native libraries
sudo apt-get install snappy libsnappy-dev
sudo apt-get install bzip2 libbz2-dev
sudo apt-get install fuse libfuse-dev
sudo apt-get install libzstd1-dev

mvn package -Pdist -Dtar -DskipTests
mvn compile -Pdist -Dtar -DskipTests

