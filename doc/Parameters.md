# Configuration Parameters

## HDFS <a name="hdfsparanalysis"></a> <sup>[[12]](References.md#hdfs_default_xml)</sup>

### NameNode
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| dfs.namenode.handler.count | 10 | hdfs-site.xml/core-site.xml | The number of Namenode RPC server threads that listen to requests from clients |
| dfs.blocksize | 134217728 | hdfs-site.xml | The default block size for new files, in bytes |
| dfs.replication | 3 | hdfs-site.xml |Default block replication |
| dfs.namenode.replication.min | 1 |hdfs-site.xml |Minimal block replication |


### DataNode
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| dfs.datanode.handler.count | 10 | hdfs-site.xml/core-site.xml| The number of server threads for the datanode |
|dfs.stream-buffer-size | 4096 |hdfs-site.xml | The size of buffer to stream files|
|dfs.datanode.fsdatasetcache.<br>max.threads.per.volume | 4 | hdfs-site.xml | The maximum number of threads per volume to use for caching new data on the datanode|
|dfs.datanode.volumes.replica-add.threadpool.size | ||Specifies the maximum number of threads to use for adding block in volume |
|dfs.datanode.max.transfer.threads | 4096|hdfs-site.xml|Specifies the maximum number of threads to use for transferring data in and out of the DataNode |
|dfs.datanode.data.dir |file://${hadoop.tmp.dir}/dfs/data|hdfs-site.xml|Comma separated list of paths on the local filesystem of a DataNode |


## MapReduce <a name="maprredparanalysis"></a> <sup>[[13]](References.md#mapred_default_xml)</sup>
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| mapreduce.job.maps | 2 | The number of map tasks is determinated by the number of input splits | The default number of map tasks per job |
| mapreduce.job.reduces | 1 | mapred-site.xml | The default number of reduce tasks per job |
|mapreduce.task.timeout | 600000 | mapred-site.xml | The number of milliseconds before a task will be terminated if it neither reads an input, writes an output, nor updates its status string|
|mapreduce.map.cpu.vcores | 1 |mapred-site.xml | The number of virtual cores to request from the scheduler for each map task|
|mapreduce.map.memory.mb | -1 | mapred-site.xml | The amount of memory to request from the scheduler for each map task|
|mapreduce.reduce.cpu.vcores | 1 | mapred-site.xml | The amount of memory to request from the scheduler for each reduce task |
|mapreduce.reduce.memory.mb | -1 | mapred-site.xml | Sets the memory requested for the all reduce task containers to the value in MB  |


## YARN <a name="yarnparanalysis"></a> <sup>[[14]](References.md#yarn_default_xml)</sup><sup>[[15]](References.md#yarn_resource_configuration)</sup>

### ResourceMenager
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| yarn.resourcemanager.scheduler.class | org.apache.hadoop.yarn.<br>server.resourcemanager.<br>scheduler.capacity.<br>CapacityScheduler | yarn-site.xml | The class to use as the resource scheduler |
| yarn.scheduler.minimum-allocation-vcores | 1 | yarn-site.xml |The minimum allocation for every container request at the RM in terms of virtual CPU cores |
| yarn.scheduler.maximum-allocation-vcores |4  | yarn-site.xml | The maximum allocation for every container request at the RM in terms of virtual CPU cores|
|yarn.scheduler.minimum-allocation-mb| 1024 | yarn-site.xml | The minimum allocation for every container request at the RM in MBs|
|yarn.scheduler.maximum-allocation-mb| 8192 | yarn-site.xml | The maximum allocation for every container request at the RM in MBs|

### NodeMenager
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
|yarn.nodemanager.resource.memory-mb | -1 | yarn-site.xml | Defines total available resources on the NodeManager to be made available to running containers |


## My Test Cases
Full factorial design 3^2 * 9 --> 2 indipendent factors, 3 levels and 9 replicas

* `Indipendent Factors` (computation): 
  * dfs.datanode.handler.count --> 10,12,16
  * mapreduce.map.cpu.vcores --> 1,2,4 (non può superare il numero di vcores disponibili  nel cluster, vedi yarn.nodemanager.resource.cpu-vcores)
* `Response variables` (time) : 
  * number of map tasks
  * CPU time spent by the map tasks : Total time that the all map tasks have spent executing on CPU's
  * CPU time spent by the reduce tasks : Total time that the all reduce tasks have spent executing on CPU's
  * CPU time spent by the mapreduce framework : Total time that the all map and reduce tasks have spent executing on CPU's
  * TestDSFIO Average IO rate mb/sec
  * TestDSFIO Throughput mb/sec

* Istogramma --> CPU time spent by the map tasks - CPU time spent by the reduce tasks / number of files
* lineplot --> throughput / file size
* lineplot --> avarege io / file size

* Mediana delle repliche per avere una repparesentazione più accurata del valore tipico