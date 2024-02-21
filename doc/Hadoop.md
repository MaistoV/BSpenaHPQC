# Apache Hadoop

## Introduction <a name="intro"></a>
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


## HDFS <a name="hdfs"></a>
HDFS (Hadoop Distributed File System)<sup>[[4]](References.md#hdfs_architecture)</sup> is a java-based distributed file system running on commodity hardware which supports a traditional hierarchical file organization. This file system :
* Stores user data in files.
* Splits file in one or more blocked-sized chunks known as **data blocks**,with size of 128 MB by default (the size is configurable per file).  
* Replicates the data blocks. The replication factor is three by default, but it can be configurable per file.
* Supports **write-once-read-many** access model for on files. After closing a fila, it cannnot be updated at any point, but content can be append at the end.
* Support the **snapshot** to execute a roll back of a corrupted istance

HDFS has a **master-slave architecture** :
* **NameNode** : There is one **master daemon** per cluster, it executes file system namespace operations (opening, closing, and renaming files and directories) and handles clients access to files. The NameNode assigns the blocks to DataNodes and stores the metadata (number of data blocks,their locations,numeber of replicas, etc...). Finally, it makes all decisions regarding blocks replication.
* **DataNode**  : There is one **slave daemon** per node in the cluster, it executes read/write operation from the file system’s client. The DataNode performs data blocks operations (creation, deletion and replication) and stores the actual data. Moreover, DataNodes ara gathered together in **racks**.

> [!NOTE]
> The deafult replication factor is 3, it generates an 200% overhead in storage space and other resources. The solution is the **Erasure Coding**, which provides the same level of fault-tolerance with much less storage space.

<p align="center">
  <img src="https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/HDFS-Architecture.jpg" width="600">
</p>

The architecture can be **rebalanced** moving data from one Datanode to another. HDFS provides :
* Data reliability.
* Data availability.
* Data Locality.
* A fault-tolerant system.


## MapReduce <a name="mapred"></a>
MapReduce<sup>[[2]](References.md#hadoop_architecture)</sup><sup>[[5]](References.md#mapred_tutorial)</sup> is a software framework for writing applications (which need not be written in Java) that process large datasets in parallel on large clusters. The framework :
* Works on sets of **<key,value> pairs**.
* Splits input into fixed-size splits called **InputSplit** in order to be processed. 

A **MapReduce job**  is the unit of work the client wants to perform, it is performed throught the execution of **map tasks** and **reduce tasks**. Each map task uses a user-defined **map function** which is implemented through interfaces and/or abstract-classes, the same goes for each reduce task with a **reduce function**. MapReduce creates a map task for each InputSplit, instead the number of reduce task can be set by the user (set as zero if no reduction is desired).

MapReduce has two phases<sup>[[5]](References.md#mapred_tutorial)</sup><sup>[[6]](References.md#mapred_flow)</sup> : 
* **Map Phase** : Maps the input <key,value> pair to zero or multiple **intermetdiate <key,value> pairs**.
* **Reduce Phase** : Reduces set of intermediate values, which share a key, to a **smaller set of values**. The smaller set is the final output. This phase has **Shuffle** and **Sort** sub-phases which occur simultaneously :
  * **Shuffle** : Fetches the values of the output of the mappers.
  * **Sort** : Groups the intermediate pairs by keys.

<p align="center">
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/11/how-map-reduce-work-together-tutorial.jpg" width="800">
</p> 


## YARN <a name="YARN"></a>
YARN (Yet Another Resource Negotiator)<sup>[[7]](References.md#yarn)</sup><sup>[[8]](References.md#yarn_intro)</sup><sup>[[9]](References.md#yarn_tutorial)</sup> is a freamwork for distributed computing which separates resorse menagement and processing components. YARN :
* Allows the exectution of an **application**, it can be a **single MapReduce job** or **DAG of jobs**. 
* Sends computations where the data is stored on locak disks (property of **data locality**)
* Uses the **containers**, collection of all the resources necessary to run an application on a node in a cluster.
* Has a **master-slave nodes architecture**.

YARN has the following components :
* **ResourceManager** : The **master daemon** runs on master node. It manages the resources among all the applications in the system. The daemon assigns map and reduce tasks to the NodeManager and schedules containers. The ResourceManager has two main components :
    * **Scheduler** : It is a pure scheduler (does not perform monitoring or tracking of the applications' status), it allocates resources or container to the running applications.
    * **ApplicationsManager** : Accepts **job submissions** by the clients<sup>[[10]](References.md#yarn_app)</sup> and secures resources on a node (an operation known as "**negotiating the first container**") to launch the ApplicationMaster.
* **NodeManager** : The **slave deamon** runs on the worker node. It launches, manages and monitors resource usage of the containers on a node.
* **ApplicationMaster** : It is a framework specific library, so there is one per application. The ApplicationMaster negotiates resources for the running application from the ResourceManager and works with the NodeManager to execute and monitor the tasks. 

<p align="center">
  <img src="https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/apache-hadoop-yarn.jpg" width="600">
</p> 

ResourceManager/NodeManager rapresents the **data-computation framework**. YARN supports the following schedulers<sup>[[8]](References.md#yarn_intro)</sup> :
* **FIFO** : Allocates resources based on arrival time.
* **Capacity scheduler** (default in hadoop) : Allocates resources to pools or queues, with FIFO scheduling to each pool.
* **Fair scheduler** : Organizes applications into queues or pools and allows to share resources fairly between quees (every application belongs to a queue). It grants container with the least amount of allocated resources.
