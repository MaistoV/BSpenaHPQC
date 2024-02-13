# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni con workload DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.
Il file system è virtualmente distribuito perché i vari componenti sono dei container.


# Table of Contents
1. [Apache Hadoop](Hadoop.md)
    * [Introduction](Hadoop.md#intro)
    * [HDFS](Hadoop.md#hdfs)
    * [MapReduce](Hadoop.md#mapred)
    * [YARN](Hadoop.md#YARN)
1. [Environment Setup](Setup.md)
    * [Overview](Setup.md#overview)
    * [Tools](Setup.md#tool)
        * [Java 1.8](Setup.md#java1.8)
        * [Maven 3.6](Setup.md#maven3.6)
        * [Hadoop 3.3.5](Setup.md#hadoop3)
        * [Native libraries](Setup.md#nl)
        * [Protocol Buffers 3.7.1](Setup.md#pb3.7)
        * [Other Packages](Setup.md#op)
        * [SSH and PDSH](Setup.md#ssh)
    * [Building Hadoop](Setup.md#build)
1. [Cluster Configuration](Parameters.md)
    * [HDFS](Parameters.md#hdfsparanalysis)
        * [NameNode](Parameters.md#namenodeparanalysis)
        * [DataNode](Parameters.md#datanodeparanalysis)
    * [MapReduce](Parameters.md#maprredparanalysis)
    * [YARN](Parameters.md#yarnparanalysis)
        * [ResourceMenager](Parameters.md#resourcemanagerparanalysis)
        * [NodeMenager](Parameters.md#nodemagaerparanalysis)
1. [Exeperiment Script](Experiments.md)
    * [DFSIO](Experiments.md#dfsio)
    * [Experiments Steps ???](Experiments.md#exsteps)
1. [Troubleshooting](Troubleshooting.md)
1. [References](References.md)
    * [Useful References](References.md#usefullref)


# Script









