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
HDFS (Hadoop Distributed File System) <sup>[[3]](#3)</sup> is a java-based distributed file system running on commodity hardware which supports a traditional hierarchical file organization. This file system :
* Stores user data in files.
* Splits file in one or more blocked-sized chunks known as **data blocks**,with size of 128 MB by default (the size is configurable per file).  
* Replicates the data blocks, replication factor of three by default (the factor is configurable per file). However, the replication method generates an 200% overhead in storage space and other resources <sup>[[5]](#5)</sup>.
* Supports **write-once-read-many** access model for on files. After closing a fila, it cannnot be updated at any point, but content can be append at the end.
* Support the **snapshot** to execute a roll back a corrupted istance

HDFS has a **master-slave architecture** :
* **NameNode** (one per cluster) : The master node executes file system namespace operations (opening, closing, and renaming files and directories) and handles clients access to files. It assigns the blocks to DataNodes and stores the metadata (number of data blocks,their locations,numeber of replicas, etc...). Finally, it makes all decisions regarding replication of blocks.
* **DataNodes** (usually one per node in the cluster) : The slave nodes execute read/write operation from the file system’s clien and perform data blocks operations (creation, deletion and replication) and store the actual data. Moreover, DataNodes ara gathered together in **racks**.

<p align="center">
  <img src="https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png" width="600">
</p>

HDFS provides data reliability and availability, as well as a fault-tolerant system. The architecture can be rebalanced moving data from one Datanode to another.

### Read and Write Operation
During the read operation <sup>[[4]](#4)</sup>, the following operations are performed :
* A client interacts with the distributed file system API and sends a request to a NameNode which checks the client access privilegs.
* If the client has the right privileges, the NameNode sends the **address** of Datanode with a copy of that block and a **security token**.
* Once the token is checked, the client opens an **input stream** and read the block.
* Then the client close the input stream.
If during the reading the DataNode crashes, the client returns to the NameNode in order to retrieve a new block location.

Instead, during the write operation <sup>[[4]](#4)</sup>, the following operations are performed :
* The authentication operation is similar to the read operation, but here the NameNode sends the address of the DataNode that contains the data has to be written by the client.
* Once the token is checked, the client opens an **outuput stream**.
* When the client is done, the DataNode copies the same block to a second DataNode and the second one copies the block to a third DataNode(replication factor of three).
* After the replica creation, the third DataNode sends an **acknowledgment** to the second DataNode, the second one sends an acknowledgment to the first one and the first one send the final acknowledgment to the client.
* The client close the stream and sends a completion message to the NameNode.


## MapReduce 

### Map Abstraction 

### Reduce Abstraction

## Yarn
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



# Implementation

## Environment Setup
* Ubuntu 22.04 LTS on vm
* HADOOP 3.3.5
* Java 8
* Maven


# References
* <a id="1"></a> [Apache Hadoop](https://hadoop.apache.org/)
* <a id="2"></a> [Hadoop Ecosystem](https://data-flair.training/blogs/hadoop-ecosystem-components/)
* <a id="3"></a> [HDFS Architecture](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
* <a id="4"></a> [HDFS Tutorial – A Complete Hadoop HDFS Overview](https://data-flair.training/blogs/hadoop-hdfs-tutorial/)
* <a id="5"></a> [HDFS Erasure Coding](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)

* <a id=""></a> [MapReduce Tutorial](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
* <a id=""></a> [Hadoop MapReduce Tutorial – A Complete Guide to Mapreduce](https://data-flair.training/blogs/hadoop-mapreduce-tutorial/)
* <a id=""></a> "MapReduce: Simplified Data Processing on Large Clusters"

* https://data-flair.training/blogs/hadoop-architecture/
* https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
* https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/
* https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/


* https://data-flair.training/blogs/hadoop-mapreduce-flow/

* https://data-flair.training/blogs/hadoop-yarn-tutorial/



## Note 
* In [2] si parla dell'Erasure Coding
* Per configurare la dimensione del block modificare la proprietà dfs.block.size in hdfs-site.xml (https://data-flair.training/blogs/data-block/)

# Cose da fare
* Trovare foto architettura hdfs
* Approfondire MapReduce
* Approfondire YARN
* Installare Hadoop (sorgente github)
* Creare un cluster virtuale a container (build con Maven)
* Setup del cluster virtuale su singolo nodo
* Cambiare parametri di configurazione di Yarn
* Misurare i fattori all'interno dei wrokload
* Gli script generati devono essere portati sul cluster fisico