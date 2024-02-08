# Parameters Analisys ????

## HDFS
### NameNode
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| dfs.namenode.handler.count | 10 | hdfs-site.xml/core-site.xml | The number of Namenode RPC server threads that listen to requests from clients |
| dfs.blocksize | 134217728 | hdfs-site.xml | The default block size for new files, in bytes |

### DataNode
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| dfs.datanode.handler.count | 10 | hdfs-site.xml/core-site.xml| The number of server threads for the datanode |
|dfs.stream-buffer-size | 4096 |hdfs-site.xml | The size of buffer to stream files|
|dfs.datanode.fsdatasetcache.max.threads.per.volume | 4 | hdfs-site.xml | The maximum number of threads per volume to use for caching new data on the datanode|


## MapReduce
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| mapreduce.job.maps | 2 | The number of map tasks is determinated by the number of input splits | The default number of map tasks per job |
| mapreduce.job.reduces | 1 | mapred-site.xml | The default number of reduce tasks per job |
|mapreduce.task.timeout | 600000 | mapred-site.xml | The number of milliseconds before a task will be terminated if it neither reads an input, writes an output, nor updates its status string|
|mapreduce.map.resource.vcores | 1 |mapred-site.xml | Sets the CPU requested for the all map task containers to the value|
|mapreduce.map.resource.memory-mb | 1024 | mapred-site.xml | Sets the memory requested for the all map task containers to the value in MB|
|mapreduce.reduce.resource.memory-mb | 1024 | mapred-site.xml | Sets the memory requested for the all reduce task containers to the value in MB  |
|mapreduce.reduce.resource.vcores | 1 | mapred-site.xml | Sets the CPU requested for the all reduce task containers to the value  |


## YARN
### ResourceMenager
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
| yarn.scheduler.minimum-allocation-vcores | 1 | yarn-site.xml | Minimum allocation for every container request at the RM in terms of virtual CPU cores |
| yarn.scheduler.maximum-allocation-vcores |4  | yarn-site.xml | The maximum allocation for every container request at the RM in terms of virtual CPU cores|
|yarn.scheduler.minimum-allocation-mb| 1024 | yarn-site.xml | The minimum allocation for every container request at the RM in MBs|
|yarn.scheduler.maximum-allocation-mb| 8192 | yarn-site.xml | The maximum allocation for every container request at the RM in MBs|


### NodeMenager
| Parameter | Default Value | Configuration File | Description |
| :---: | :---: | :---: | :---: |
|yarn.nodemanager.resource.memory-mb | -1 | yarn-site.xml | Defines total available resources on the NodeManager to be made available to running containers |