# HPQC
The purpose of the project is to develop a `Test Cases Script` that, given `independent factors`, runs the `TestDFSIO benchmark` on a `Single-Node Hadoop Cluster` set in `Pseudo-Distributed M;Mode`. Also the script measures the `response variables`.

The independent factors are the `cluster configuration parameters` and are stored into the *test_list.csv* file. The response variables can be both cluster configuration parameters and `TestDSFIO results`, them are saved within the *test_result.csv* file.

## Table of Contents
1. [Apache Hadoop](doc/Hadoop.md)
    * [Introduction](doc/Hadoop.md#intro)
    * [HDFS](doc/Hadoop.md#hdfs)
    * [MapReduce](doc/Hadoop.md#mapred)
    * [YARN](doc/Hadoop.md#YARN)
    * [Hadoop Cluster Configurarion](doc/Hadoop.md#clusterconfig)
    * [TestDFSIO](doc/Hadoop.md#testdfsio)
1. [Environment Setup](doc/Setup.md)
    * [Tools](doc/Setup.md#tool)
    * [Building Hadoop](doc/Setup.md#build)
    * [Setting up the Hadoop Cluster](doc/Setup.md#cluster)
1. [Test Cases Script](doc/Script.md)
    * [Script Structure](doc/Script.md#script_struc)
    * [Control Flow](doc/Script.md#flow_control)
    * [Python Modules](doc/Script.md#python_mod)
    * [How to Run](doc/Script.md#run)
1. [Experiments](doc/Experiments.md)
    * [Response Variables Analysis](doc/Script.Experiments#rv_analysis)
1. [Troubleshooting](doc/Troubleshooting.md)
1. [References](doc/References.md)
    * [Further References](doc/References.md#fref)