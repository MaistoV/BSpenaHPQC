# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni su DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.


## Hadoop
Freamwork that store and process big data using cluster of commodity hardware. The ecosystem has different components, for example:
1) HDFS is the storage unit
2) MapReduce is the process unit
3) Yarn is the menager unit

### HDFS
It is a java based distributed file system; it is fault tolerant and provides scalabilty and reliability. HDFS has two components [2]:
1) NameNode (master node) : stores metadata (i.e. number of data blocks,their locations,...) and performs different operations such as file system menagment
2) DataNode (slave node) : stores data blocks and performs different operations such as read/write operation (as per the request of the clients) and block replica creation

#### Blocks
HDFS splits the data into multiple blocks know as data blocks [3]; the HDFS data blocks are blocked-sized chunks whith deafult size of 128 MB (the size is configurable). The data blocks are stored on several slave nodes. Besides, thanks to the replication method, HDFS replicates the data blocks in order to prevent their lost [1](#1). By default, the replication method as a replication factor of 3, which cause which causes 200% overhead.

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

## Eresure Coding
L'fs di Hadoop deve essere tollerante ai fallimenti ed essere in grado di funzionare quando un nodo cade. Uno dei modi per fare ciò è replicare i chunck di dati n volte, la configuarazione base prevede una replicazione 3x per ogni dato la quale causa un overhead del 200% (ogni modifica alle scrittura viene rplicata in tre chunk diversi). Per risolvere questo problema, si usa l'Eresure Coding (tipo di codice a correzione di errore con blocchi dati e blocchi di parità). Attraverso l'Eresure Coding, non si replica il blocco tre volte ma i blocchi sono posti in maniera successiva. In questo modo se venisse perso un blocco dati o uno di parità, attravarso l'albegra lineare (o altre tecniche) è possibile riscostruire il blocco perso. Il codice si chiama Read Solomon (parametro di configuarazione dell'fs).
Error-correcting code --> da vedere (?)


## Environment Setp
* Ubuntu 22.04 LTS on vm
* HADOOP 3.3.5
* Java 8


## References
* <a id="1"></a> [What is Hadoop ?](https://www.youtube.com/watch?v=aReuLtY0YMI&t=1s)
* [Hadoop Ecosystem](https://data-flair.training/blogs/hadoop-ecosystem-components/) [2]
* [HDFS Blocks](https://data-flair.training/blogs/data-block/) [3]
* [Hadoop HDFS Data Read and Write Operations](https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/) [4]
* "MapReduce: Simplified Data Processing on Large Clusters" []


# Cose da fare
* Installare Hadoop (sorgente github)
* Creare un cluster virtuale a container (build con Maven)
* Setup del cluster virtuale su singolo nodo
* Cambiare parametri di configurazione di Yarn
* Misurare i fattori all'interno dei wrokload
* Gli script generati devono essere portati sul cluster fisico

# Cose da inserire
* Definizione di big data (?)
* Differenza tra file system e file system distribuiti (?)