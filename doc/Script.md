# Test Cases Script

## TestDFSIO <a name="testdfsio"></a>
TestDFSIO benchmark is a read and write test for HDFS<sup>[[16]](References.md#dfsio)</sup><sup>[[27]](References.md#benchmark)</sup>. The benchmark syntax  is the following
```bash
$ $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-*test*.jar TestDFSIO -read | -write | -clean [-nrFiles N] [-fileSize MB] [-resFile resultFileName] [-bufferSize Bytes]
```
with the following flags :
* **-write** : To run the write test.
* **-read** : To run the read test. 
* **-clean** : To clean up test results.
* **-nrFiles** : The number of files (equal to the number of map tasks).
* **-fileSize** : The size of a file to generate B|KB|MB|GB|TB is allowed.
* **-resFile** : Set the file name where the results will be saved (by deafult the results are saved in TestDFSIO_results.log file in /benchmarks/TestDFSIO directory)
* **-bufferSize** : The buffer size flag describes the length of the write buffer in bytes

It is convenient, at the first, run a write test and then run the read test using the same parameters.


## Script Steps <a name="scriptsteps"></a>
The test cases script has six steps.

### Step 1
Read *test_list.csv* file, saving the **indipendet factors** in a dataframe, and the *test_result.csv* file through **csv** and **pandas module**. The *read_csv* function takes :
* The path to test_list.csv
* The row names for test_list.csv
* The path to test_result.csv
* The column names for test_result.csv
```python
def read_csv(path_test_list,tests_numer,path_test_result,columns_name):
    df_test_list = pandas.read_csv(path_test_list)                  
    df_test_list.index = tests_numer                          # Set the indexes of the dataframe

    with open(path_test_result,'w') as file:          
        writer=csv.writer(file)
        writer.writerow(columns_name)  

    return df_test_list
```
and returns the indipendet factors a dataframe.

For each dataframe row are executed the steps from 2 to 6.

### Step 2
Cluster configuration by setting *-site.xml* files through **xml.etree.ElementTree module**. The *config_cluster* function takes :
    #1. the path to the hdfs-site.xml
    #2. the tuple with hdfs parameters
    #3. the path to the mapred-site.xml
    #4. the tuple with mapred parameters
    #5. the path to the yarn-site.xml
    #6. the tuple with yarn parameters
    #7. the dataframe row
    #8. the special parameters need for the cluster configuration
```python
def config_cluster(path_hdfs_site,hdfs_t,path_mapred_site,mapred_t,path_yarn_site,yarn_t,row,special_parameters):
    update_xml(path_hdfs_site,row,hdfs_t,special_parameters)          # Configure hdfs-site.xml
    update_xml(path_mapred_site,row,mapred_t,special_parameters)      # Configure mapred-site.xml
    update_xml(path_yarn_site,row,yarn_t,special_parameters)          # Configure yarn-site.xml
```
  #1. the xml fila path
    #2. the dataframe row
    #3. the tuple with the configuration parameters
    #4. the special parameters need for the cluster configuration
```python
def update_xml(file,row,tuple,special_parameters):    
    tree = ET.parse(file)                                             # Parse the XML file
    root = tree.getroot()  

    for property in root.findall('property'):                         # Remove the previous tags
        name = property.find('name').text                             # Find the tags with the parameters configured for the pseudo-distributed mode 
        if name not in special_parameters:    
            root.remove(property)

    for t in tuple:
        property = ET.Element('property')                             # Create property,name and value elements
        name = ET.Element('name')
        value = ET.Element('value')
        name.text = t                                                 # Set the new tags
        value.text = str(row[t])
        root.append(property)                                         # Add the new elements to the root element
        property.append(name)
        property.append(value)                  

    ET.indent(tree, space='  ', level=0)                              # Indent the xml file
                                                                      # level = 0 means that you are starting the indentation from the root
    tree.write(file, encoding="utf-8", xml_declaration=True)          # Write on xml file
```

### Step 3
Start the cluster in Start the cluster in Pseudo-Distributed Mode using the os module
```python
 os.system('./start_cluster.sh')
```

```bash
#!/bin/bash

# Stop HDFS deamons,YARN deamons and JobHistoryServer
$HADOOP_HOME/sbin/stop-dfs.sh                      
$HADOOP_HOME/sbin/stop-yarn.sh
$HADOOP_HOME/bin/mapred --daemon stop historyserver
sleep 4

# Format the filesystem
#$HADOOP_HOME/bin/hdfs namenode -format             
#sleep 5

# Start HDFS deamons,YARN deamons and JobHistoryServer
$HADOOP_HOME/sbin/start-dfs.sh                     
$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave                  # Forcefully let the namenode leave safemode
$HADOOP_HOME/sbin/start-yarn.sh
$HADOOP_HOME/bin/mapred --daemon start historyserver
sleep 2

# Make the HDFS directories required to execute MapReduce jobs
$HADOOP_HOME/bin/hdfs dfs -mkdir /user             
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/$(whoami)
sleep 2

# Copy the input files into the distributed filesystem
$HADOOP_HOME/bin/hdfs dfs -mkdir input
$HADOOP_HOME/bin/hdfs dfs -put $HADOOP_HOME/etc/hadoop/*.xml input
```

### Step 4 
Start the DFSIO test
#1. the dataframe row
#2. the tuple with dfsio parameters

descrivere il fatto della fork (modulo multiprocessing) con l'immagine 
```python
def create_dfsio(row,dfsio_t):
    s = '$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -' + str(row['dfsio.operation'])
    for t in dfsio_t:
        s = s + ' -' + t.split('.')[1] + ' ' + str(row[t])  

    dfsio_process = mp.Process(target = start_dfsio, args=(s,))             # Create the new process
    dfsio_process.start()                                                   # Start the process
    dfsio_process.join()  
```

it takes the string with che command to run    
```python
def start_dfsio(string):
    os.system(string)
```

### Step 5
Start the measurement scripts and saves the results in *test_result.csv* file. (using subprocess,linecache module)

    #1. dataframe of the test_result.csv file
    #2. index of the test, to increase the row
    #3. path to the log file
    #4. path to the result file
```python
def start_offline_test(index,path_test_dfsio_logs,path_test_result):

    # Test via command line
    map_number,cpu_time_map,cpu_time_red,cpu_time_tot = test_via_command_line()
    
    # Results TestDFSIO via logs
    throughput_value,avarege_io_value = test_dfsio_logs(index,path_test_dfsio_logs)

    # Save values on test_result.csv
    with open(path_test_result,'a') as file:          
        writer=csv.writer(file)
        writer.writerow([map_number,cpu_time_map,cpu_time_red,cpu_time_tot,throughput_value,avarege_io_value]) 
```
```python
def test_via_command_line():
    # Find jobID
    job_id_sub = subprocess.run('$HADOOP_HOME/bin/mapred job -list all | grep "job_"',shell = True ,capture_output=True)
    job_id = job_id_sub.stdout.decode().split('\t')[0]

    #1: Find the number of map tasks
    map_number_sub = subprocess.run('$HADOOP_HOME/bin/mapred job -status ' + job_id + ' | grep "Number of maps"',shell = True ,capture_output=True)
    map_number = int(map_number_sub.stdout.decode().split(':')[1])

    #2: the CPU time spent for map tasks and reduce tasks
    cpu_time_sub = subprocess.run('$HADOOP_HOME/bin/mapred job -history ' + job_id + ' | grep "CPU time spent"',shell = True ,capture_output=True)
    cpu_time_map = int(cpu_time_sub.stdout.decode().replace(',','').split('|')[3])
    cpu_time_red = int(cpu_time_sub.stdout.decode().replace(',','').split('|')[4])
    cpu_time_tot = int(cpu_time_sub.stdout.decode().replace(',','').split('|')[5])

    return map_number,cpu_time_map,cpu_time_red,cpu_time_tot
```
    #1. index to increase the rows
    #2. path to the log file
```python
def test_dfsio_logs(index,file):
    throughput_line =  5 + (9 * index)                                                  # Position of the lines
    avarege_io_line =  6 + (9 * index)
    throughput_value = float(linecache.getline(file, throughput_line).split(':')[1])    # Get a specific line
    avarege_io_value = float(linecache.getline(file, avarege_io_line).split(':')[1])
    return throughput_value,avarege_io_value
```
### Step 6
Clean up test results
```python
os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')
```

## Run the Script <a name="scriptrun"></a>
### Prerequisites
Set : 
* mapred-site.xml and yarn-site.xml files as shown in Single Cluster.....
* The test_list.csv
* The tuples with the choosen parameters

### Run
* at the start run $HADOOP_HOME/bin/hdfs namenode -format


* Questo da mettere nel paragrafo di run. To run the script you need to set up the **test cases** in the in *test_list.csv* file, by setting the parameters along the columns. There are two types of parameters :
* **cluster configuration parameters** for the three Hadoop layers :
    * [HDFS](Parameters.md#hdfsparanalysis)
    * [MapReduce](Parameters.md#maprredparanalysis)
    * [YARN](Parameters.md#yarnparanalysis)



The **response variables** can be captured throught an "online test" (like linuxperf), which is not implemented yed, and throught an "offline test". The results of each test case will be saved in the rows of *test_result.csv* file.




## My Test Cases
Motivare la scelta dei fattori (scheduling/calcolo) e le variabili di risposta (tempistiche)
* **Indipendent Factors** : 
  * dfs.namenode.handler.count
  * dfs.datanode.handler.count
  * mapreduce.job.reduces
  * mapreduce.reduce.cpu.vcores
  * yarn.scheduler.minimum-allocation-vcores
  * yarn.scheduler.maximum-allocation-vcores
  * yarn.resourcemanager.scheduler.class
* **Response variables** : 
  * number of map tasks
  * execution time of the job (elapsed time)
  * vcores allocated for the application
  * memory allocated for the application
  * execution time of the map tasks       
  * execution time of the reduce tasks

* Motivare scelta parametri applicazioni


## Comandi di misura
* bin/yarn application -list
* bin/yarn application -status <appID>
* bin/mapred job -list all
* bin/mapred job -history <jobID>
* bin/mapred job -status <jobID>  --> to get stat of the job
* mapred job -status {job_id} | grep "CPU time" --> execution time for a job

## ???
* Web UI
  * NameNode - http://localhost:9870/
  * DataNode -  http://localhost:9864/
  * ResourceManager - http://localhost:8088/
  * JobHistory - http://localhost:19888/
     
* Logs : Into /logs directory
