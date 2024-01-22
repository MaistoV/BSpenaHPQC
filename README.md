# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni su DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.


## Hadoop
Hadoop is a **freamwork** written in java used to store massive datasets on a **cluster** in a distributed manner; It offers reliabily, scalability and fault-tolerance [[2]](#2). The ecosystem has different components [[1]](#1), three of them are:
* **HDFS**: the storage unit
* **MapReduce**: the processing unit
* **Yarn**: the menager unit

![Links](https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/04/Hadoop-Ecosystem-2-01.jpg)

### Hadoop Cluster
The Hadoop cluster is a group of computers connected together via LAN, based on the **master-slave architecture**. There is one master node and multiple slave nodes [[2]](#2) [[3]](#3) [[4]](#4):
* **Master node** : asigns and manages task to the slave nodes; there are two daemons (processes running in background) running on it known as NameNode and Resource Menager. 
* **Slave nodes** : performs computation operations and store the data. Inside the slave node, there are two tasks, Map and Reduce, and two daemons, DataNode and Node Manager.

![Link](https://data-flair.training/blogs/wp-content/uploads/sites/2/2019/02/Hadoop-Architecture2-01.jpg)


### HDFS
HDFS (Hadoop Distributed File System) is a java based distributed file system [[1]](#1) running on on low-cost commodity hardware. HDFS splits files in blocked-sized chunks known as **data blocks** (default configurable size of 128 MB); since blocks are chunck of data, their metadata are not stored with the data blocks [[6]](#6). The file system has two types of **deamons**[[4]](#4) [[5]](#5):
* **NameNode**: runs on the master node, manages the DataNodes and the modifications to file system namespace. Finally, NameNode stores metadata (number of data blocks,their locations,numeber of replicas, etc...).
* **DataNodes**: run on the slave node,so they execute read/write operation from the file system’s client. In addition, DataNodes perform data block operations (creation, deletion and replication) and store the actual data.  

HDFS uses the **replication method** (by default with replication factor of three) to replicate the data and store the copies on different nodes across the cluster in a distributed manner; in this way the file system guarantees a **fault-tolerant** storage layer, as well as data reliability and availability [[5]](#5). However, the replication method generates an 200% overhead in storage space and other resources [[]](). Finally, HDFS provides high scalability through expanding or contracting the cluster  [[5]](#5).

#### HDFS Read Operation
During the read operation, the following operations are performed [[5]](#5):
* A client interacts with the distributed file system API and sends a request to a NameNode which checks the client access privilegs.
* If the client has the right privileges, the NameNode sends the **address** of Datanode with a copy of that block and a **security token**.
* Once the token is checked, the client opens an **input stream** and read the block.
* Then the client close the input stream.
If during the reading the DataNode crashes, the client returns to the NameNode in order to retrieve a new block location.

#### HDFS Write Operation
During the write operation, the following operations are performed [[5]](#5):
* The authentication operation is similar to the read operation, but here the NameNode sends the address of the DataNode that contains the data has to be written by the client.
* Once the token is checked, the client opens an **outuput stream**.
* When the client is done, the DataNode copies the same block to a second DataNode and the second one copies the block to a third DataNode(replication factor of three).
* After the replica creation, the third DataNode sends an **acknowledgment** to the second DataNode, the second one sends an acknowledgment to the first one and the first one send the final acknowledgment to the client.
* The client close the stream and sends a completion message to the NameNode.


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

## Erasure Coding
L'fs di Hadoop deve essere tollerante ai fallimenti ed essere in grado di funzionare quando un nodo cade. Uno dei modi per fare ciò è replicare i chunck di dati n volte, la configuarazione base prevede una replicazione 3x per ogni dato la quale causa un overhead del 200% (ogni modifica alle scrittura viene rplicata in tre chunk diversi). Per risolvere questo problema, si usa l'Eresure Coding (tipo di codice a correzione di errore con blocchi dati e blocchi di parità). Attraverso l'Eresure Coding, non si replica il blocco tre volte ma i blocchi sono posti in maniera successiva. In questo modo se venisse perso un blocco dati o uno di parità, attravarso l'albegra lineare (o altre tecniche) è possibile riscostruire il blocco perso. Il codice si chiama Read Solomon (parametro di configuarazione dell'fs).
Error-correcting code --> da vedere (?)


## Environment Setup
* Ubuntu 22.04 LTS on vm
* HADOOP 3.3.5
* Java 8
* Maven


## References
* <a id="1"></a> [Hadoop Ecosystem](https://data-flair.training/blogs/hadoop-ecosystem-components/)
* <a id="2"></a> [Hadoop Tutorial for Big Data Enthusiasts](https://data-flair.training/blogs/hadoop-tutorial/) <!-- Qua si parla anche di erasure coding-->
* <a id="3"></a> [What is Hadoop Cluster? Learn to Build a Cluster in Hadoop](https://data-flair.training/blogs/what-is-hadoop-cluster/)
* <a id="4"></a> [Hadoop Architecture in Detail – HDFS, Yarn & MapReduce](https://data-flair.training/blogs/hadoop-architecture/)
* <a id="5"></a> [HDFS Tutorial – A Complete Hadoop HDFS Overview](https://data-flair.training/blogs/hadoop-hdfs-tutorial/)
* <a id="6"></a> [HDFS Blocks](https://data-flair.training/blogs/data-block/)
* <a id="7"></a> 

* https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/
* https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/
* https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html
* "MapReduce: Simplified Data Processing on Large Clusters"
* https://data-flair.training/blogs/hadoop-yarn-tutorial/


# Cose da fare
* Approfondire MapReduce
* Approfondire YARN
* Installare Hadoop (sorgente github)
* Creare un cluster virtuale a container (build con Maven)
* Setup del cluster virtuale su singolo nodo
* Cambiare parametri di configurazione di Yarn
* Misurare i fattori all'interno dei wrokload
* Gli script generati devono essere portati sul cluster fisico