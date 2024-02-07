## Hadoop Cluster Configuration Parameters
The Hadoop's cluster can be configured by setting two type of files<sup>[[13]](References.md#13)</sup>:
* **Read-only default configuration files** :
  * core-default.xml.
  * hdfs-default.xml. 
  * yarn-default.xml.
  * mapred-default.xml.
* **Site-specific configuration files** :
  * core-site.xml.
  * hdfs-site.xml.
  * yarn-site.xml.
  * mapred-site.xml.

Besides, it is possible to set site-specific values via : 
  * hadoop-env.sh.
  * yarn-env.sh.

### HDFS Configuration Parameters
#### NameNode
* **dfs.namenode.replication.max-streams-hard-limit**<sup>[[14]](References.md#14)</sup> : Hard limit for all replication streams.
* **dfs.replication** : Default block replication.
* **dfs.namenode.replication.min** : Minimal block replication.
* **dfs.replication.max** : Maximal block replication.
* **dfs.blocksize** : HDFS blocksize.
* **dfs.namenode.handler.count** : Server threads to handle RPCs (Remote Procedure Call).
* **dfs.namenode.maintenance.replication.min** : Minimal number of live replicas that all blocks of DataNodes undergoing maintenance need to satisfy.

#### DataNode
* **dfs.datanode.volumes.replica-add.threadpool.size**<sup>[[14]](References.md#14)</sup> : Specifies the maximum number of threads to use for adding block in volume.
* **dfs.datanode.max.transfer.threads** : Specifies the maximum number of threads to use for transferring data in and out of the DN.
* **dfs.datanode.fsdatasetcache.max.threads.per.volume** : Maximum number of threads (consume  both I/O and CPU) per volume to use for caching new data on the datanode.
* **dfs.datanode.data.dir** : Comma separated list of paths on the local filesystem of a DataNode where it should store its blocks.
* **dfs.datanode.ec.reconstruction.stripedread.timeout.millis**<sup>[[5]](References.md#5)</sup> : Timeout for striped reads.
* **dfs.datanode.ec.reconstruction.stripedread.buffer.size** : Buffer size for reader service.
* **dfs.datanode.ec.reconstruction.threads** : Number of threads used by the Datanode for background reconstruction work.
* **dfs.datanode.ec.reconstruction.xmits.weight** : Relative weight of xmits (maximum value between the number of read streams and the number of write streams) used by EC background recovery task comparing to replicated block recovery.
* **dfs.stream-buffer-size** : The size of buffer to stream files.

### YARN Configuration Parameters
#### ResourceMenager
* **yarn.scheduler.minimum-allocation-vcores**<sup>[[15]](References.md#15)</sup> : Minimum allocation for every container request at the RM in terms of virtual CPU cores. 
* **yarn.scheduler.maximum-allocation-vcores** : Maximum allocation for every container request at the RM in terms of virtual CPU cores.
* **yarn.resourcemanager.scheduler.class** : ResourceManager Scheduler class (CapacityScheduler, FairScheduler or FifoScheduler).
* **yarn.scheduler.minimum-allocation-mb** : Minimum limit of memory in MBs to allocate to each container request at the Resource Manager.
* **yarn.scheduler.maximum-allocation-mb** : Maximum limit of memory in MBs to allocate to each container request at the Resource Manager.

#### NodeMenager
* **yarn.nodemanager.resource.memory-mb**<sup>[[13]](References.md#13)</sup> : Defines total available resources on the NodeManager to be made available to running containers.
* **yarn.app.mapreduce.am.resource.memory-mb**<sup>[[16]](References.md#16)</sup> :	Sets the memory requested for the application master container to the value in MB.
* **yarn.app.mapreduce.am.resource.vcores** :	Sets the CPU requested for the application master container to the value.
* **mapreduce.map.resource.memory-mb** : Sets the memory requested for the all map task containers to the value in MB.
* **mapreduce.map.resource.vcores	Sets** : The CPU requested for the all map task containers to the value.
* **mapreduce.reduce.resource.memory-mb** :	Sets the memory requested for the all reduce task containers to the value in MB.
* **mapreduce.reduce.resource.vcores** : Sets the CPU requested for the all reduce task containers to the value.


# Parameters Description ????

dfs.namenode.handler.count
dfs.datanode.volumes.replica-add.threadpool.size
dfs.stream-buffer-size

yarn.scheduler.minimum-allocation-vcores
yarn.scheduler.maximum-allocation-vcores

mapreduce.map.resource.memory-mb
mapreduce.map.resource.vcores
mapreduce.reduce.resource.memory-mb
mapreduce.reduce.resource.vcores