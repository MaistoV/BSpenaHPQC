# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni su DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.


## Hadoop
Hadoop is a freamwork that store and process big data [[1]](#1) [[2]](#2). The ecosystem has different components, three of them are:
* **HDFS**: the storage unit
* **MapReduce**: the process unit
* **Yarn**: the menager unit

![Links](https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/04/Hadoop-Ecosystem-2-01.jpg)

### HDFS
HDFS is a java based distributed file system [[2]](#2) that stores files running on cluster of commodity hardware [[3]](#3). It provides data reliability and availability and fault-tolerant storage layer thanks to the replication method. In addiction, HDFS offers parallel data access increasing the throughput access to application and offers scalabilty by increasing and decreasing the cluster size

#### Nodes and Daemons
HDFS has two types of **nodes** [[3]](#3):
* **NameNode** (master node): manages and mantains the slave nodes, assigning tasks to them. Besides, regulates the client’s access to files and executes file system namespace operations like opening, closing, and renaming files and directories [[3]](#3).
* **DataNode** (slave node): performs tasks,read/write operations from the file system’s clients and **data blocks** operation (creation, delation and replication). Datanodes are arranged in **racks**  and in a cluster there are multiple racks.
At startup, each Datanode does **handshaking** in order to connect with its corresponding Namenode, during the handshaking there is the verification of namespace ID and software version. At the time of mismatch found, DataNode goes down automatically[[2]](#2).
Besides, there are two types of **deamons** (processes runngin in background) running on HDFS for data storage [[3]](#3):
* **Namenodes**: run on the master node and store metadata (number of data blocks,their locations,numeber of replicas, etc...)
* **Datanodes**: run on the slave node and store the actual data

#### Data Blocks
HDFS splits files in blocked-sized chunks known as **data blocks**; each block has a default size of 128 MB, but it can be configured by modifying the appropriate property [[4]](#4). HDFS uses a replication factor of three to replicate the data and store the copies across the cluster in a distributed manner on different DataNodes [[3]](#3), but the replication method causes an 200% overhead. Thanks to the block fixed size, it it possible calculate the number of blocks that can be stored on a given disk. Besides, since blocks are chunck of data, their metadata are not stored with data blocks [[4]](#4).

#### HDFS Read Operation
During the read operation, the following operations are performed [[3]](#3):
* a client interacts with the distributed file system API and sends a request to a NameNode in order to obtain the data block location
* NameNode checks the client access privilegs; if the client has the right privileges, the NameNode sends to the client address (where the data are stored) 

In the Hadoop HDFS read operation, if the client wants to read data that is stored in HDFS, it needs to interact with NameNode first. So the client interacts with distributed file system API and sends a request to NameNode to send block location. Thus, NameNode checks if the client has sufficient privileges to access the data or not. If the client have sufficient privileges,  then NameNode will share the address at which data is stored in the DataNode.

With the address, NameNode also shares a security token with the client, which it needs to show to DataNode before accessing the data for authentication purposes.

When a client goes to DataNode for reading the file, after checking the token, DataNode allows the client to read that particular block. A client then opens the input stream and starts reading data from the specified DataNodes. Hence, In this manner, the client reads data directly from DataNode.

During the reading of a file, if the DataNode goes down suddenly, then a client will again go to the NameNode, and the NameNode will share another location where that block is present.

![Links](https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/05/Data-Read-Mechanism-in-HDFS.gif)


#### HDFS Write Operation


### MapReduce
It splits data in parts and processes each of them separately on different data nodes. The results are then combined to give the final output. This method saves a lot of time

### Yarn
It processes job requestes ad maneges cluster resources, tt has different units:
* Resource menager : assings the resources
* Node menager : handles the nodes and monitor the resource usage
* Application master
* Containers : hold a collection of physical resources
If we want to process the MapReduce job :
1) the Application master requests the container from the node menager
2) the node menager, obtainde the resources, sends it to the Resource menager

## Eresure Coding (?)
L'fs di Hadoop deve essere tollerante ai fallimenti ed essere in grado di funzionare quando un nodo cade. Uno dei modi per fare ciò è replicare i chunck di dati n volte, la configuarazione base prevede una replicazione 3x per ogni dato la quale causa un overhead del 200% (ogni modifica alle scrittura viene rplicata in tre chunk diversi). Per risolvere questo problema, si usa l'Eresure Coding (tipo di codice a correzione di errore con blocchi dati e blocchi di parità). Attraverso l'Eresure Coding, non si replica il blocco tre volte ma i blocchi sono posti in maniera successiva. In questo modo se venisse perso un blocco dati o uno di parità, attravarso l'albegra lineare (o altre tecniche) è possibile riscostruire il blocco perso. Il codice si chiama Read Solomon (parametro di configuarazione dell'fs).
Error-correcting code --> da vedere (?)


## Environment Setup
* Ubuntu 22.04 LTS on vm
* HADOOP 3.3.5
* Java 8
* Maven


## References
* <a id="1"></a> [What is Hadoop ?](https://www.youtube.com/watch?v=aReuLtY0YMI&t=1s)
* <a id="2"></a> [Hadoop Ecosystem](https://data-flair.training/blogs/hadoop-ecosystem-components/)
* <a id="3"></a> [HDFS Tutorial – A Complete Hadoop HDFS Overview](https://data-flair.training/blogs/hadoop-hdfs-tutorial/)
* <a id="4"></a> [HDFS Blocks](https://data-flair.training/blogs/data-block/)
* <a id="5"></a> [Hadoop HDFS Data Read and Write Operations](https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/)
* https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/
* https://data-flair.training/blogs/hadoop-hdfs-tutorial/
* "MapReduce: Simplified Data Processing on Large Clusters"


# Cose da fare
* Installare Hadoop (sorgente github)
* Creare un cluster virtuale a container (build con Maven)
* Setup del cluster virtuale su singolo nodo
* Cambiare parametri di configurazione di Yarn
* Misurare i fattori all'interno dei wrokload
* Gli script generati devono essere portati sul cluster fisico