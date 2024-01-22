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
HDFS (Hadoop Distributed File System) is a java based distributed file system [[2]](#2) which provides different features [[3]](#3):
* Splits data into **data blocks**.
* Stores data in a distributed manner on cluster.
* 

 that stores data in a distributed manner running on cluster of commodity hardware (inexpensive hardware) 


It provides data reliability and availability and fault-tolerant storage layer thanks to the replication method. In addiction, HDFS offers parallel data access increasing the throughput access to application and offers scalabilty by increasing and decreasing the cluster size.


Objectives and Assumptions Of HDFS
1. System Failure: As a Hadoop cluster is consists of Lots of nodes with are commodity hardware so node failure is possible, so the fundamental goal of HDFS figure out this failure problem and recover it. 

2. Maintaining Large Dataset: As HDFS Handle files of size ranging from GB to PB, so HDFS has to be cool enough to deal with these very large data sets on a single cluster. 

3. Moving Data is Costlier then Moving the Computation: If the computational operation is performed near the location where the data is present then it is quite faster and the overall throughput of the system can be increased along with minimizing the network congestion which is a good assumption. 

4. Portable Across Various Platform: HDFS Posses portability which allows it to switch across diverse Hardware and software platforms. 

5. Simple Coherency Model: A Hadoop Distributed File System needs a model to write once read much access for Files. A file written then closed should not be changed, only data can be appended. This assumption helps us to minimize the data coherency issue. MapReduce fits perfectly with such kind of file model.

6. Scalability: HDFS is designed to be scalable as the data storage requirements increase over time. It can easily scale up or down by adding or removing nodes to the cluster. This helps to ensure that the system can handle large amounts of data without compromising performance.

7. Security: HDFS provides several security mechanisms to protect data stored on the cluster. It supports authentication and authorization mechanisms to control access to data, encryption of data in transit and at rest, and data integrity checks to detect any tampering or corruption.

8. Data Locality: HDFS aims to move the computation to where the data resides rather than moving the data to the computation. This approach minimizes network traffic and enhances performance by processing data on local nodes.

9. Cost-Effective: HDFS can run on low-cost commodity hardware, which makes it a cost-effective solution for large-scale data processing. Additionally, the ability to scale up or down as required means that organizations can start small and expand over time, reducing upfront costs.

10. Support for Various File Formats: HDFS is designed to support a wide range of file formats, including structured, semi-structured, and unstructured data. This makes it easier to store and process different types of data using a single system, simplifying data management and reducing costs.

#### Nodes and Daemons
HDFS has master and slave **nodes**, whiche typically forms an HDFS cluster: 
* **NameNode**: master node which manages and mantains the slave nodes, assigning tasks to them. Besides, regulates the client’s access to files and executes file system namespace operations like opening, closing, and renaming files and directories [[3]](#3).
* **DataNode** : slave node which performs tasks,read/write operations from the file system’s clients and **data blocks** operation (creation, delation and replication). Datanodes are arranged in **racks**  and in a cluster there are multiple racks.

*** <!-- In questo modo le frasi che danno inizio ai due elenchi sono sulla stessa linea -->

Besides, there are two types of **deamons** (processes running in background on HDFS for data storage) [[3]](#3):
* **Namenodes**: run on the master node and store metadata (number of data blocks,their locations,numeber of replicas, etc...).
* **Datanodes**: run on the slave node and store the actual data.  
At startup, each Datanode does **handshaking** in order to connect with its corresponding Namenode, during the handshaking there is the verification of namespace ID and software version. At the time of mismatch found, DataNode goes down automatically[[2]](#2).  

#### Data Blocks
HDFS splits files in blocked-sized chunks known as **data blocks**; each block has a default size of 128 MB, but it can be configured by modifying the appropriate property [[4]](#4). HDFS uses a replication factor of three to replicate the data and store the copies across the cluster in a distributed manner on different DataNodes [[3]](#3), but the replication method causes an 200% overhead. Thanks to the block fixed size, it it possible calculate the number of blocks that can be stored on a given disk. Besides, since blocks are chunck of data, their metadata are not stored with data blocks [[4]](#4).

#### HDFS Read Operation
During the read operation, the following operations are performed [[3]](#3):
* A client interacts with the distributed file system API and sends a request to a NameNode.
* NameNode checks the client access privilegs.
* If the client has the right privileges, the NameNode sends the **address** of Datanode with a copy of that block and a **security token**.
* The client shows the security token to the DataNode.
* Once the token is checked, the client opens an **input stream** and read the block.
* Then the client close the input stream.
If during the reading the DataNode crashes, the client returns to the NameNode in order to retrieve a new block location.

![Links](https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/05/Data-Read-Mechanism-in-HDFS.gif)

#### HDFS Write Operation
During the write operation, the following operations are performed [[3]](#3):
* The authentication operation is similar to the read operation, but here the NameNode sends the address of the DataNode that contains the data has to be written by the client.
* Once the token is checked, the client opens an **outuput stream**.
* When the client is done, the DataNode copies the same block to a second DataNode and the second one copies the block to a third DataNode. (replication factor of three).
* After the replica creation, the third DataNode sends an **acknowledgment** to the second DataNode, the second one sends an acknowledgment to the first one and the first one send the final acknowledgment to the client.
* The client close the stream and sends a completion message to the NameNode.

![Links](https://data-flair.training/blogs/wp-content/uploads/sites/2/2016/05/Data-Write-Mechanism-in-HDFS.gif)


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
* <a id="5"></a> [Hadoop – HDFS (Hadoop Distributed File System)](https://www.geeksforgeeks.org/hadoop-hdfs-hadoop-distributed-file-system/)
* https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/
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