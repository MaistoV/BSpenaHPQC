# References
1. <a id="1"></a> [Apache Hadoop](https://hadoop.apache.org/)
1. <a id="2"></a> [Apache Hadoop Architecture – HDFS, YARN & MapReduce](https://techvidvan.com/tutorials/hadoop-architecture/)
1. <a id="3"></a> [10 Features Of Hadoop That Made It The Most Popular](https://data-flair.training/blogs/features-of-hadoop-and-design-principles/)
1. <a id="4"></a> [HDFS Architecture](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
1. <a id="5"></a> [HDFS Erasure Coding](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)
1. <a id="6"></a> [MapReduce Tutorial](https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
1. <a id="7"></a> "MapReduce: Simplified Data Processing on Large Cluster",Jeffrey Dean,Sanjay Ghemawat
1. <a id="8"></a> [Hadoop MapReduce Flow – How data flows in MapReduce?](https://data-flair.training/blogs/hadoop-mapreduce-flow/)
1. <a id="9"></a> [Apache Hadoop YARN](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/YARN.html)
1. <a id="10"></a> [Introduction to YARN](https://www.youtube.com/watch?v=5vmP1-6xd6Y&ab_channel=OracleLearning)
1. <a id="11"></a> [Hadoop Yarn Tutorial for Beginners](https://data-flair.training/blogs/hadoop-yarn-tutorial/)
1. <a id="12"></a> [Hadoop: Writing YARN Applications](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/WritingYarnApplications.html)
1. <a id="13"></a> [Hadoop Cluster Setup](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
1. <a id="14"></a> [hdfs-defult.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
1. <a id="15"></a> [yarn-defult.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
1. <a id="16"></a> [Hadoop: YARN Resource Configuration](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/ResourceModel.html)


# References Utili
## hadoop
* https://data-flair.training/blogs/hadoop-architecture/

## mapreduce
* https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html

## installazione
* https://www.adaltas.com/en/2020/08/04/installing-hadoop-from-source/
* https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html

## maven
* https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html
* https://github.com/eirslett/frontend-maven-plugin
* https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html


## Note 
* Per configurare la dimensione del block modificare la proprietà dfs.block.size in hdfs-site.xml (https://data-flair.training/blogs/data-block/)
* In [7] parla di Hadoop Streaming, utility che permette di creare ed eseguire job con qualsiasi eseguibile e di creare mapper e reducer
* In [7] indica quali interfacce devono essere implementate dalle classi key e value
* In [13] viene spiegato come avviare e stoppare il cluster di hadoop7
* In [2] C'è la spiegazione di un cluster hadoop e ci sono altre cose utili