# Experiments
I have conducted a `full factorial desing` 3<sup>2</sup>9, which consists of `2 independent factors`, each with `3 levels`. For each of the 9 combinations, were carried out `9 repetitions`, resulting in a total of 81 experiments. All experiments were write operations with a number of files equal to 10 and a file size of 100 MB.

The chosen independent factors are related to the computation field and are: 
* `dfs.datanode.handler.count` : The number of server threads for the datanode, with the following levels
  * 10 (default value)
  * 12
  * 16
* `mapreduce.map.cpu.vcores` : The number of virtual cores to request from the scheduler for each map task, with the following levels
  * 1 (default value)
  * 2
  * 4 

The levels depend on the `cluster configuration`.

On the other hand, the `response variables` are related to the time analysis :
* `Number of map tasks`
* `CPU time spent by the map tasks` : Total time that the all map tasks have spent executing on CPU's
* `CPU time spent by the reduce tasks` : Total time that the all reduce tasks have spent executing on CPU's
* `CPU time spent by the mapreduce framework` : Total time that the all map and reduce tasks have spent executing on CPU's
* `TestDSFIO Average IO rate mb/sec`
* `TestDSFIO Throughput mb/sec`

## Response Variables Analysis <a name="rv_analysis"></a>
Subsequently, the following graphs were designed to visualize the results. In order to conduct a more detailed study on the `throughput`, were considered additional points. Instead, the `number of map tasks` was not represented because its value was constant across all experiments and matched the number of files of the TestDFSIO. Indeed, TestDFSIO is designed in such a way that it will use 1 map task per file.

<img src="img/throughput.png" width="1000">
<img src="img/cpu_time.jpeg" width="1000">
<img src="img/average_io.png" width="1000">

