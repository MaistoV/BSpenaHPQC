# Cluster Configuration
The Hadoop's cluster can be configured by setting the parameters of the three layers in the **site-specific configuration files**<sup>[[12]](References.md#cluster_setup)</sup> such as:
* core-site.xml.
* hdfs-site.xml.
* yarn-site.xml.
* mapred-site.xml.
Besides. there are **read-only default configuration files** which contain parameters deafult values :
  * core-default.xml.
  * hdfs-default.xml. 
  * yarn-default.xml.
  * mapred-default.xml.

In this chapter, we will see a detailed description of some parameters.


## HDFS <a name="hdfsparanalysis"></a> <sup>[[13]](References.md#hdfs_default_xml)</sup>

### NameNode <a name="namenodeparanalysis"></a>
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| dfs.namenode.handler.count | 10 | hdfs-site.xml/core-site.xml | The number of Namenode RPC server threads that listen to requests from clients |
| dfs.blocksize | 134217728 | hdfs-site.xml | The default block size for new files, in bytes |
| dfs.namenode.ec.system.default.policy | RS-6-3-1024k | hdfs-site.xml | The default erasure coding policy name will be used on the path if no policy name is passed |
| dfs.replication | | |Default block replication |
| dfs.namenode.replication.min | ||Minimal block replication |


### DataNode <a name="datanodeparanalysis"></a>
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| dfs.datanode.handler.count | 10 | hdfs-site.xml/core-site.xml| The number of server threads for the datanode |
|dfs.stream-buffer-size | 4096 |hdfs-site.xml | The size of buffer to stream files|
|dfs.datanode.fsdatasetcache.max.threads.per.volume | 4 | hdfs-site.xml | The maximum number of threads per volume to use for caching new data on the datanode|
|dfs.datanode.volumes.replica-add.threadpool.size | ||Specifies the maximum number of threads to use for adding block in volume |
|dfs.datanode.max.transfer.threads | ||Specifies the maximum number of threads to use for transferring data in and out of the DataNode |
|dfs.datanode.data.dir |||Comma separated list of paths on the local filesystem of a DataNode |


## MapReduce <a name="maprredparanalysis"></a> <sup>[[14]](References.md#mapred_default_xml)</sup>
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| mapreduce.job.maps | 2 | The number of map tasks is determinated by the number of input splits | The default number of map tasks per job |
| mapreduce.job.reduces | 1 | mapred-site.xml | The default number of reduce tasks per job |
|mapreduce.task.timeout | 600000 | mapred-site.xml | The number of milliseconds before a task will be terminated if it neither reads an input, writes an output, nor updates its status string|
|mapreduce.map.resource.vcores | 1 |mapred-site.xml | Sets the CPU requested for the all map task containers to the value|
|mapreduce.map.resource.memory-mb | 1024 | mapred-site.xml | Sets the memory requested for the all map task containers to the value in MB|
|mapreduce.reduce.resource.memory-mb | 1024 | mapred-site.xml | Sets the memory requested for the all reduce task containers to the value in MB  |
|mapreduce.reduce.resource.vcores | 1 | mapred-site.xml | Sets the CPU requested for the all reduce task containers to the value  |


## YARN <a name="yarnparanalysis"></a> <sup>[[15]](References.md#yarn_default_xml)</sup>

### ResourceMenager <a name="resourcemanagerparanalysis"></a>
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| yarn.resourcemanager.scheduler.class | org.apache.hadoop.yarn.<br>server.resourcemanager.<br>scheduler.capacity.<br>CapacityScheduler | yarn-site.xml | The class to use as the resource scheduler |
| yarn.scheduler.minimum-allocation-vcores | 1 | yarn-site.xml | Minimum allocation for every container request at the RM in terms of virtual CPU cores |
| yarn.scheduler.maximum-allocation-vcores |4  | yarn-site.xml | The maximum allocation for every container request at the RM in terms of virtual CPU cores|
|yarn.scheduler.minimum-allocation-mb| 1024 | yarn-site.xml | The minimum allocation for every container request at the RM in MBs|
|yarn.scheduler.maximum-allocation-mb| 8192 | yarn-site.xml | The maximum allocation for every container request at the RM in MBs|

### NodeMenager <a name="nodemagaerparanalysis"></a>
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
|yarn.nodemanager.resource.memory-mb | -1 | yarn-site.xml | Defines total available resources on the NodeManager to be made available to running containers |