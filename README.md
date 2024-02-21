# HPQC
The purpose of the project is to develop a script that, given **independent factors**, runs the **TestDFSIO benchmark** on a **Single-Node Hadoop Cluster** set in **pseudo-distributed mode** and measures the **response variables**. The independent factors are stored into the *test_list.csv* file, while the response variables are saved within the *test_result.csv* file.

## Table of Contents
1. [Apache Hadoop](doc/Hadoop.md)
    * [Introduction](doc/Hadoop.md#intro)
    * [HDFS](doc/Hadoop.md#hdfs)
    * [MapReduce](doc/Hadoop.md#mapred)
    * [YARN](doc/Hadoop.md#YARN)
1. [Cluster Configuration](doc/Parameters.md)
    * [HDFS](doc/Parameters.md#hdfsparanalysis)
    * [MapReduce](doc/Parameters.md#maprredparanalysis)
    * [YARN](doc/Parameters.md#yarnparanalysis)
1. [Environment Setup](doc/Setup.md)
    * [Tools](doc/Setup.md#tool)
        * [Java 1.8](doc/Setup.md#java1.8)
        * [Python Libraries](doc/Setup.md#pl)
        * [Maven 3.6](doc/Setup.md#maven3.6)
        * [Hadoop 3.3.5](doc/Setup.md#hadoop3)
        * [Libraries](doc/Setup.md#l)
        * [SSH and PDSH](doc/Setup.md#ssh)
    * [Building Hadoop](doc/Setup.md#build)
    * [Setting up Hadoop Cluster](doc/Setup.md#cluster)
1. [Test Cases Script](doc/Experiments.md)
    * [How the Script works](doc/Experiments.md#scriptwork)
    * [How to run the Script](doc/Experiments.md#scriptrun)
1. [Troubleshooting](doc/Troubleshooting.md)
1. [References](doc/References.md)
    * [Further References](doc/References.md#fref)








