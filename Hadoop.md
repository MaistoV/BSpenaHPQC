# Apache Hadoop

## Introduction
Apache Hadoop software library <sup>[[1]](References.md#hadoop)</sup> is a **freamwork** used for the distributed processing of massive datasets across **clusters** of commodity hardware. Hadoop Cluster is a computational cluster used for storing and analyzing huge amounts of unstructured or structured data in a distributed computing environment. Hadoop has a **master-slave** architecture<sup>[[2]](References.md#hadoop_architecture)</sup> :
* **Master Node** : There is one per cluster. It assigns tasks to the slave nodes. The master node stores metadata and manages the resources across the cluster.
* **Slave Nodes** : Store data and perform the computing.

<p align="center">
  <img src="https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/hadoop-architecture.jpg" width="700">
</p>

Besides, the architecture has three layers :
* **HDFS** : The storage layer.
* **MapReduce** : The data processing layer.
* **Yarn** : The resource management layer.

Hadoop provides different features<sup>[[3]](References.md#hadoop_features)</sup> such as :
* Fault Tolerance.
* High Availability.
* Data Locality.
* Data Reliability.
* Very Cost-Effective.


## HDFS
HDFS (Hadoop Distributed File System)<sup>[[4]](References.md#hdfs_architecture)</sup> is a java-based distributed file system running on commodity hardware which supports a traditional hierarchical file organization. This file system :
* Stores user data in files.
* Splits file in one or more blocked-sized chunks known as **data blocks**,with size of 128 MB by default (the size is configurable per file).  
* Replicates the data blocks. The replication factor is three by default, but it can be configurable per file.
* Supports **write-once-read-many** access model for on files. After closing a fila, it cannnot be updated at any point, but content can be append at the end.
* Support the **snapshot** to execute a roll back of a corrupted istance

HDFS has a **master-slave architecture** :
* **NameNode** : There is one **master daemon** per cluster, it executes file system namespace operations (opening, closing, and renaming files and directories) and handles clients access to files. The NameNode assigns the blocks to DataNodes and stores the metadata (number of data blocks,their locations,numeber of replicas, etc...). Finally, it makes all decisions regarding blocks replication.
* **DataNode**  : There is one **slave daemon** per node in the cluster, it executes read/write operation from the file system’s client. The DataNode performs data blocks operations (creation, deletion and replication) and stores the actual data. Moreover, DataNodes ara gathered together in **racks**.

<p align="center">
  <img src="https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/HDFS-Architecture.jpg" width="600">
</p>

> [!NOTE]
> [Here](https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/) a detailed description of Hadoop HDFS Data Read and Write Operations and [here](https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/) an introductory guide to the rack awareness.

The architecture can be **rebalanced** moving data from one Datanode to another. HDFS provides :
* Data reliability.
* Data availability.
* Data Locality.
* A fault-tolerant system.

> [!NOTE]
> [Here](https://data-flair.training/blogs/learn-hadoop-hdfs-fault-tolerance/) a detailed description of how HDFS achieves fault tolerance.

### Erasure Coding
The 3x replication generates an 200% overhead in storage space and other resources. An alterntive method is the **erasure coding (EC)**<sup>[[5]](References.md#EC)</sup>, which provides the same level of fault-tolerance with much less storage space. In storage system, an EC implementation is **Redundant Array of Inexpensive Disks (RAID)**. RAID implements EC by:
* Diving logically sequantial data (file) into smaller units.
* Storing consecutive units on differnt disks.

The dividing opertation is known as striping, and the generated units are known as **striping cell**. EC has two main processes :
* **Encoding** : For each of striping cell, are calculated and stored a certain number of **parity cell**.
* **Decoding** : Using pararity cells and remaining data, it is possible to recover the error of any striping cell.

EC works the **policy concept** wich describes how encode/decode a file. Each policy contains :
* **EC Schema** : It includes the numbers of data and parity blocks in an EC group , as well as the codec algorithm.
* **Striping cell size** : It determines the granularity of striped reads and writes, including buffer sizes and encoding work.

Policies are named as follow **codec - num data blocks - num parity blocks - cell size**, the supported policies are :
* **RS-3-2-1024k**
* **RS-6-3-1024k**
* **RS-10-4-1024k**
* **RS-LEGACY-6-3-1024k**
* **XOR-2-1-1024k**

One of codec algorithm are the **Reed–Solomon codes**<sup>[[6]](References.md#RS)</sup>. They are a group of error-correcting codes which help in recovering corrupted messages that are being transferred over a network.


## MapReduce 
MapReduce<sup>[[7]](References.md#mapred_tutorial)</sup> is a software framework for writing applications (which need not be written in Java) that process large datasets in parallel on large clusters. The framework :
* Operates on sets of **<key,value> pairs**.
* Splits input into fixed-size splits called **InputSplit** in order to be processed. 
* Starts up many copies of the program on the nodes of the cluster, the copies are divided into :
  * **Master** : There is only one master who assigns each worker a **map task** or a **reduce task**. MapReduce creates a map task for each InputSplit, instead the number of reduce task can be set by the user (set as zero if no reduction is desired).
  * **Workers** : Execute tasks. A worker is known as **mapper** if it is assigned a map task, insted it is known as **reducer** if it is assigned a reduce task.

Each map task uses a user-defined **map function** which is implemented through interfaces and/or abstract-classes, the same goes for each reduce task with a **reduce function**.

A **MapReduce job** is a complete execution of a **map phase** and a **reduce phase**<sup>[[8]](References.md#mapred_tutorial)</sup><sup>[[9]](References.md#mapred_flow)</sup> : 
* **Map Phase** : The mapper maps the input <key,value> pair to zero or multiple **intermetdiate <key,value> pairs**.
* **Shuffling and Sorting** (occur simultaneously) :
  * **Shuffle Phase** : Fetches the values of the output of the mappers.
  * **Sort Phase** : Groups the intermediate pairs by keys.
* **Reduce Phase** : The reducer reduces set of intermediate values, which share a key, to a **smaller set of values**. The smaller set is the final output.

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/11/how-map-reduce-work-together-tutorial.jpg" width="800">
</p> 

> [!NOTE]
> [Here](https://data-flair.training/blogs/how-hadoop-mapreduce-works/) is a complete MapReduce job execution flow.


## YARN
YARN (Yet Another Resource Negotiator)<sup>[[10]](References.md#yarn)</sup><sup>[[11]](References.md#yarn_intro)</sup><sup>[[12]](References.md#yarn_tutorial)</sup> is a freamwork for distributed computing which separates resorse menagement and processing components. YARN :
* Allows the exectution of different kind of **applications**, like MapReduce job, DAG of job , Stream processing, etc... 
* Sends computations where the data is stored on locak disks (property of **data locality**)
* Uses the **containers**, collection of all the resources necessary to run an application on a node in a cluster.
* Has a **master-slave nodes architecture**.

YARN has the following components :
* **ResourceManager** : The **master daemon** runs on master node. It manages the resources among all the applications in the system. The daemon assigns tasks to the NodeManager and schedules containers. The ResourceManager has two main components :
    * **Scheduler** : It is a pure scheduler (does not perform monitoring or tracking of the applications' status), it allocates resources or container to the running applications.
    * **ApplicationsManager** : Accepts **job submissions** by the clients<sup>[[13]](References.md#yarn_app)</sup> and secures resources on a node (an operation known as "**negotiating the first container**") to launch the ApplicationMaster.
* **NodeManager** : The **slave deamon** runs on the worker node. It launches, manages and monitors resource usage of the containers on a node.
* **ApplicationMaster** : It is a framework specific library, so there is one per application. The ApplicationMaster negotiates resources for the running application from the ResourceManager and works with the NodeManager to execute and monitor the tasks. 

<p align="center">
  <img src="https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/apache-hadoop-yarn.jpg" width="600">
</p> 

ResourceManager/NodeManager rapresents the **data-computation framework**. YARN supports the following schedulers<sup>[[11]](References.md#yarn_intro)</sup> :
* **FIFO** : Allocates resources based on arrival time.
* **Capacity scheduler** (default in hadoop) : Allocates resources to pools or queues, with FIFO scheduling to each pool.
* **Fair scheduler** : Organizes applications into queues or pools and allows to share resources fairly between quees (every application belongs to a queue). It grants container with the least amount of allocated resources.


## Hadoop Cluster Configuration
The Hadoop's cluster can be configured by setting two type of files<sup>[[14]](References.md#cluster_setup)</sup>:
* **Read-only default configuration files** :
  * core-default.xml.
  * hdfs-default.xml. 
  * yarn-default.xml.
  * mapred-default.xml.
* **Site-specific configuration files** :
  * core-site.xml.
  * hdfs-site.xml.
  * yarn-site.xml.
  * mapred-site.xml.

Besides, it is possible to set site-specific values via : 
  * hadoop-env.sh.
  * yarn-env.sh.

### HDFS<sup>[[5]](References.md#EC)</sup><sup>[[15]](References.md#hdfs_default_xml)</sup>
#### NameNode
| Parameter | Description |
| :---: | :---: |
| dfs.namenode.handler.count | The number of Namenode RPC(Remote Procedure Call) server threads that listen to requests from clients |
| dfs.namenode.replication.max-streams-hard-limit | Hard limit for all replication streams |
| dfs.replication | Default block replication |
| dfs.namenode.replication.min | Minimal block replication |
| dfs.blocksize | The default block size for new files, in bytes |
| dfs.namenode.maintenance.replication.min | Minimal number of live replicas that all blocks of DataNodes undergoing maintenance need to satisfy |

#### DataNode
| Parameter | Description |
| :---: | :---: |
|dfs.datanode.volumes.replica-add.threadpool.size | Specifies the maximum number of threads to use for adding block in volume |
|dfs.datanode.max.transfer.threads | Specifies the maximum number of threads to use for transferring data in and out of the DataNode |
|dfs.datanode.fsdatasetcache.max.threads.per.volume | Maximum number of threads (consume  both I/O and CPU) per volume to use for caching new data on the datanode |
|dfs.datanode.data.dir |Comma separated list of paths on the local filesystem of a DataNode where it should store its blocks  |
|dfs.datanode.ec.reconstruction.stripedread.timeout.millis | Timeout for striped reads |
|dfs.datanode.ec.reconstruction.stripedread.buffer.size | Buffer size for reader service |
|dfs.datanode.ec.reconstruction.threads |Number of threads used by the Datanode for background reconstruction work |
|dfs.datanode.ec.reconstruction.xmits.weight| Relative weight of xmits (maximum value between the number of read streams and the number of write streams) used by EC background recovery task comparing to replicated block recovery |
|dfs.stream-buffer-size | The size of buffer to stream files |


### MapReduce<sup>[[17]](References.md#yarn_resource_configuration)</sup>
| Parameter | Description |
| :---: | :---: |
|mapreduce.map.resource.memory-mb |Sets the memory requested for the all map task containers to the value in MB  |
|mapreduce.map.resource.vcores |Sets the CPU requested for the all map task containers to the value  |
|mapreduce.reduce.resource.memory-mb |Sets the memory requested for the all reduce task containers to the value in MB  |
|mapreduce.reduce.resource.vcores |Sets the CPU requested for the all reduce task containers to the value  |

> [!NOTE]
>* mapreduce.map.resource.memory-mb is preferred over mapreduce.map.resource.memory
>* mapreduce.map.resource.vcores is preferred over mapreduce.map.cpu.vcores
>* mapreduce.reduce.resource.memory-mb is preferred over mapreduce.reduce.resource.memory
>* mapreduce.reduce.resource.vcores is preferred over mapreduce.reduce.cpu.vcores


### YARN<sup>[[14]](References.md#cluster_setup)</sup><sup>[[16]](References.md#yarn_default_xml)</sup><sup>[[17]](References.md#yarn_resource_configuration)</sup>
#### ResourceMenager
| Parameter | Description |
| :---: | :---: |
|yarn.scheduler.minimum-allocation-vcores |Minimum allocation for every container request at the RM in terms of virtual CPU cores  |
|yarn.scheduler.maximum-allocation-vcores | Maximum allocation for every container request at the RM in terms of virtual CPU cores |
|yarn.resourcemanager.scheduler.class |ResourceManager Scheduler class (CapacityScheduler, FairScheduler or FifoScheduler)  |
|yarn.scheduler.minimum-allocation-mb |Minimum limit of memory in MBs to allocate to each container request at the Resource Manager  |
|yarn.scheduler.maximum-allocation-mb |Maximum limit of memory in MBs to allocate to each container request at the Resource Manager  |


#### NodeMenager
| Parameter | Description |
| :---: | :---: |
|yarn.nodemanager.resource.memory-mb | Defines total available resources on the NodeManager to be made available to running containers |