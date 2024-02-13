# References
1. <a id="hadoop"></a> [Apache Hadoop](https://hadoop.apache.org/)
1. <a id="hadoop_architecture"></a> [Apache Hadoop Architecture – HDFS, YARN & MapReduce](https://techvidvan.com/tutorials/hadoop-architecture/)
1. <a id="hadoop_features"></a> [10 Features Of Hadoop That Made It The Most Popular](https://data-flair.training/blogs/features-of-hadoop-and-design-principles/)
1. <a id="hdfs_architecture"></a> [HDFS Architecture](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
1. <a id="mapred_tutorial"></a> [MapReduce Tutorial](https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
1. <a id="mapred_paper"></a> "MapReduce: Simplified Data Processing on Large Cluster",Jeffrey Dean,Sanjay Ghemawat
1. <a id="mapred_flow"></a> [Hadoop MapReduce Flow – How data flows in MapReduce?](https://data-flair.training/blogs/hadoop-mapreduce-flow/)
1. <a id="yarn"></a> [Apache Hadoop YARN](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/YARN.html)
1. <a id="yarn_intro"></a> [Introduction to YARN](https://www.youtube.com/watch?v=5vmP1-6xd6Y&ab_channel=OracleLearning)
1. <a id="yarn_tutorial"></a> [Hadoop Yarn Tutorial for Beginners](https://data-flair.training/blogs/hadoop-yarn-tutorial/)
1. <a id="yarn_app"></a> [Hadoop: Writing YARN Applications](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/WritingYarnApplications.html)
1. <a id="cluster_setup"></a> [Hadoop Cluster Setup](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/ClusterSetup.html) 
1. <a id="hdfs_default_xml"></a> [hdfs-defult.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
1. <a id="mapred_default_xml"></a> [mapred-default.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
1. <a id="yarn_default_xml"></a> [yarn-defult.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
1. <a id="yarn_resource_configuration"></a> [Hadoop: YARN Resource Configuration](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/ResourceModel.html)
1. <a id="dfsio"></a> [Distributed I/O Benchmark of HDFS](https://bdaafall2015.readthedocs.io/en/latest/dfsio.html)
1. <a id="benchmark"></a> [Benchmarking and Stress Testing an Hadoop Cluster with TeraSort, TestDFSIO & Co.](https://www.michael-noll.com/blog/2011/04/09/benchmarking-and-stress-testing-an-hadoop-cluster-with-terasort-testdfsio-nnbench-mrbench/)
1. <a id="fair_scheduler"></a> [Hadoop: Fair Scheduler](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/FairScheduler.html)


# Useful References <a name="usefullref"></a>

* [Hadoop HDFS Data Read and Write Operations](https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/)
* [Rack Awareness in Hadoop HDFS – An Introductory Guide](https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/)
* [HDFS Erasure Coding](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)
* [What is Reed–Solomon Code?](https://www.geeksforgeeks.org/what-is-reed-solomon-code/)
* [How Hadoop MapReduce Works – MapReduce Tutorial](https://data-flair.training/blogs/how-hadoop-mapreduce-works/)

* [Maven Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)


* https://stackoverflow.com/questions/53293102/hadoop-multiple-datanode-configuration-in-pseudo-distributed-mode

## hadoop
* https://data-flair.training/blogs/hadoop-architecture/
* https://ercoppa.github.io/HadoopInternals/HadoopConfigurationParameters.html
* https://kontext.tech/article/265/default-ports-used-by-hadoop-services-hdfs-mapreduce-yarn  (porti)
* https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/CommandsManual.html
* https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/NativeLibraries.html

## mapreduce
* https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
* https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml
* https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredCommands.html
* https://cwiki.apache.org/confluence/display/HADOOP2/HowManyMapsAndReduces#

## Yarn
* https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/YarnCommands.html

## hdfs
* https://hawq.apache.org/docs/userguide/2.3.0.0-incubating/reference/HDFSConfigurationParameterReference.html
* https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.1.2/bk_system-admin-guide/content/config_properties.html

## installazione
* https://www.adaltas.com/en/2020/08/04/installing-hadoop-from-source/
* https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html

## maven
* https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html
* https://github.com/eirslett/frontend-maven-plugin
* https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html

## issue searcher
* https://issues.apache.org/jira/browse/ZOOKEEPER-4802?jql=



## Note 
* Per configurare la dimensione del block modificare la proprietà dfs.block.size in hdfs-site.xml (https://data-flair.training/blogs/data-block/)
* In [7] parla di Hadoop Streaming, utility che permette di creare ed eseguire job con qualsiasi eseguibile e di creare mapper e reducer
* In [7] indica quali interfacce devono essere implementate dalle classi key e value
* In [13] viene spiegato come avviare e stoppare il cluster di hadoop7
* In [2] C'è la spiegazione di un cluster hadoop e ci sono altre cose utili