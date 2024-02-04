# References
* <a id="1"></a> [[1] Apache Hadoop](https://hadoop.apache.org/)
* <a id="2"></a> [[2] Hadoop Ecosystem](https://data-flair.training/blogs/hadoop-ecosystem-components/)
* <a id="3"></a> [[3] HDFS Architecture](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
* <a id="4"></a> [[4] HDFS Erasure Coding](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/HDFSErasureCoding.html)
* <a id="5"></a> [[5] MapReduce Tutorial](https://hadoop.apache.org/docs/r3.3.5/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
* <a id="6"></a> [6] "MapReduce: Simplified Data Processing on Large Cluster",Jeffrey Dean,Sanjay Ghemawat
* <a id="7"></a> [[7] Hadoop MapReduce Flow – How data flows in MapReduce?](https://data-flair.training/blogs/hadoop-mapreduce-flow/)
* <a id="8"></a> [[8] Apache Hadoop YARN](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/YARN.html)
* <a id="9"></a> [[9] Introduction to YARN](https://www.youtube.com/watch?v=5vmP1-6xd6Y&ab_channel=OracleLearning)
* <a id="10"></a> [[10] Hadoop Yarn Tutorial for Beginners](https://data-flair.training/blogs/hadoop-yarn-tutorial/)
* <a id="11"></a> [[11] Hadoop: Writing YARN Applications](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/WritingYarnApplications.html)
* <a id="12"></a> [[12] Hadoop Cluster Setup](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
* <a id="13"></a> [[13] hdfs-defult.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
* <a id="14"></a> [[14] yarn-defult.xml File](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
* <a id="15"></a> [[15] Hadoop: YARN Resource Configuration](https://hadoop.apache.org/docs/r3.3.5/hadoop-yarn/hadoop-yarn-site/ResourceModel.html)



# References Utili
* https://techvidvan.com/tutorials/hadoop-architecture/
* https://data-flair.training/blogs/hadoop-architecture/
* https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
* https://data-flair.training/blogs/hadoop-hdfs-data-read-and-write-operations/
* https://data-flair.training/blogs/rack-awareness-hadoop-hdfs/
* https://data-flair.training/blogs/learn-hadoop-hdfs-fault-tolerance/
* https://www.geeksforgeeks.org/hadoop-yarn-architecture/
* https://data-flair.training/blogs/wp-content/uploads/sites/2/2019/02/Hadoop-Architecture2-01.jpg --> da inserire

* https://www.adaltas.com/en/2020/08/04/installing-hadoop-from-source/

* https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/SingleCluster.html

* https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html

* https://github.com/eirslett/frontend-maven-plugin

* https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

* https://data-flair.training/blogs/features-of-hadoop-and-design-principles/

* https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/03/HDFS-Architecture.jpg --> da sostituire all'immagine in hdfs


## Note 
* Per configurare la dimensione del block modificare la proprietà dfs.block.size in hdfs-site.xml (https://data-flair.training/blogs/data-block/)
* In [6] parla di Hadoop Streaming, utility che permette di creare ed eseguire job con qualsiasi eseguibile e di creare mapper e reducer
* In [6] indica quali interfacce devono essere implementate dalle classi key e value
* In [12] viene spiegato come avviare e stoppare il cluster di hadoop