import pandas
import xml.etree.ElementTree as ET                                  # Module for parsing and creating XML data.
import os
import requests                                                     # Module to execute http requests
import subprocess
import time
import csv
import linecache                                                    # Module to axtract and access specific lines in python

# Function to add tags to the xml file, it receives :
    # 1. the xml file root (configuration)
    # 2. the name of the parameter
    # 3. the value of the paramter
def add_tags(root,n,v):
    property = ET.Element('property')                               # Create property,name and value elements
    name = ET.Element('name')
    value = ET.Element('value')
    name.text = n                                                   # Set the new tags
    value.text = str(v)
    root.append(property)                                           # Add the new elements to the root element
    property.append(name)
    property.append(value)


# Function to update the xml file, it receives :
    #1. the xml fila path
    #2. the dataframe row
    #3. the tuple with the configuration parameters
    #4. the special parameters need for the cluster configuration
def update_xml(file,row,tuple,special_parameters):    
    tree = ET.parse(file)                                           # Parse the XML file
    root = tree.getroot()  

    for property in root.findall('property'):                       # Remove the previous tags
        name = property.find('name').text                           # Find the tags with the parameters configured for the pseudo-distributed mode 
        if name not in special_parameters:    
            root.remove(property)

    for t in tuple:
        add_tags(root,t,row[t])                                  

    ET.indent(tree, space='  ', level=0)                            # Indent the xml file
    tree.write(file, encoding="utf-8", xml_declaration=True)        # Write on xml file



# Function for the cluster configuration, it takes:
    #1. the path to the hdfs-site.xml
    #2. the tuple with hdfs parameters
    #3. the path to the mapred-site.xml
    #4. the tuple with mapred parameters
    #5. the path to the yarn-site.xml
    #6. the tuple with yarn parameters
    #7. the dataframe row
    #8. the special parameters need for the cluster configuration
def config_cluster(path_hdfs_site,hdfs_t,path_mapred_site,mapred_t,path_yarn_site,yarn_t,row,special_parameters):
    update_xml(path_hdfs_site,row,hdfs_t,special_parameters)                 # Configure hdfs-site.xml
    #update_xml(path_mapred_site,row,mapred_t,special_parameters)             # Configure mapred-site.xml
    #update_xml(path_yarn_site,row,yarn_t,special_parameters)                 # Configure yarn-site.xml


# Function to start the cluster
def start_cluster():
    os.system('$HADOOP_HOME/sbin/stop-dfs.sh')                      # Stop HDFS deamons,YARN deamons and JobHistoryServer
    os.system('$HADOOP_HOME/sbin/stop-yarn.sh')
    os.system('$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh --config $HADOOP_HOME/etc/hadoop stop historyserver')
    time.sleep(2)
    #os.system('$HADOOP_HOME/bin/hdfs namenode -format')             # Format the filesystem
    time.sleep(2)
    os.system('$HADOOP_HOME/sbin/start-dfs.sh')                     # Start hdfs and yarn deamons 
    os.system('$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave')
    os.system('$HADOOP_HOME/sbin/start-yarn.sh')
    os.system('$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh --config $HADOOP_HOME/etc/hadoop start historyserver')
    os.system('$HADOOP_HOME/bin/hdfs dfs -mkdir /user')             # Make the HDFS directories required to execute MapReduce jobs
    os.system('$HADOOP_HOME/bin/hdfs dfs -mkdir /user/$(whoami)')

    # Togliere le sleep, aggiustare i comandi in un solo script bash (????)


# Function to create (using the paramters from test_list.csv) and start the dfsio test, it takes:
    #1. the dataframe row
    #2. the tuple with dfsio parameters
def start_dfsio(row,dfsio_t):
    s = '$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -' + str(row['dfsio.operation'])
    for t in dfsio_t:
        s = s + ' -' + t.split('.')[1] + ' ' + str(row[t])  

    print(s)
    os.system(s)

    # Start online test like linuxperf (not implemented yet)

    # Effettuare fork e poi join


# Function to start test via command line
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


# Function to read response variables from TestDFSIO logs, it takes:
    #1. index of the test, to increase the row
    #2. path to the log file
def test_dfsio_logs(index,file):
    throughput_line =  5 + (9 * index)                                      # Position of the lines
    avarege_io_line =  6 + (9 * index)
    throughput_value = float(linecache.getline(file, throughput_line).split(':')[1])              # Get a specific line
    avarege_io_value = float(linecache.getline(file, avarege_io_line).split(':')[1])
    return throughput_value,avarege_io_value


# Function to start offline test and to save response variables, it takes:
    #1. index of the test, to increase the row
    #2. path to the log file
    #3. path to the result file
def start_offline_test(index,path_test_dfsio_logs,path_test_result):

    # Test via command line
    map_number,cpu_time_map,cpu_time_red,cpu_time_tot = test_via_command_line()
    
    # Results TestDFSIO via logs
    throughput_value,avarege_io_value = test_dfsio_logs(index,path_test_dfsio_logs)

    # Test via REST API

    # Saves value on test_result.csv
    with open(path_test_result,'a') as file:          
        writer=csv.writer(file)
        writer.writerow([map_number,cpu_time_map,cpu_time_red,cpu_time_tot,throughput_value,avarege_io_value]) 


if __name__=='__main__':

    # Files path
    path_hdfs_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/hdfs-site.xml'
    path_mapred_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/mapred-site.xml'
    path_yarn_site = '/home/spena/hadoop/hadoop-dist/target/hadoop-3.3.5/etc/hadoop/yarn-site.xml'
    path_test_list = 'test_list.csv'
    path_test_result = 'test_result.csv'
    path_test_dfsio_logs = 'TestDFSIO_results.log'

    # Tuples with the parameters (same order as of test_list file)
    hdfs_t = ('dfs.namenode.handler.count','dfs.datanode.handler.count')
    mapred_t = ('mapreduce.job.reduces','mapreduce.reduce.cpu.vcores')
    yarn_t = ('yarn.scheduler.minimum-allocation-vcores',)
    dfsio_t = ('dfsio.nrFiles','dfsio.fileSize')

    # String array with the special parameters needed for the cluster configuration in psuedo-distributed mode
    special_parameters = ['mapreduce.framework.name','mapreduce.application.classpath','yarn.nodemanager.aux-services','yarn.nodemanager.env-whitelist']  


    #Step 1: Read test_list.csv file and saves the parameters in a dataframe
    print("Step 1: Read test_list.csv \n")
    dataframe = pandas.read_csv(path_test_list)                  
    dataframe.index = ['test1']

    #Step 1.1 : Definie colums names of test_result.csv
    with open(path_test_result,'a') as file:          
        writer=csv.writer(file)
        writer.writerow(['maps.number','cpu.time.map.task','cpu.time.reduce.tasks','cpu.time.tot','throughput_value','avarege_io_value'])

    for i,row in dataframe.iterrows():
        
        #Step 2: Cluster configuration by setting **-site.xml* files
        print("Step 2: Cluster Configuration \n")
        config_cluster(path_hdfs_site,hdfs_t,path_mapred_site,mapred_t,path_yarn_site,yarn_t,row,special_parameters)
        
        #Step 3: Start the cluster in Pseudo-Distributed Mode
        print("Step 3: Start the cluster in pseudo-distributed mode")
        start_cluster()
        print("\n")

        #Step 4: Start the DFSIO test
        print("Step 4: Start the TestDFSIO")
        start_dfsio(row,dfsio_t)
                                
        #Step 5: Start the offline test and save save response variables in *test_result.csv* file
        print("Step 5: Start the Offline Test")
        start_offline_test(int(i.split('test')[1]),path_test_dfsio_logs,path_test_result)
        print("\n")

        #Step 6: Clean up test results 
        print("Step 6: Clean up test results")
        os.system('$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.5-tests.jar TestDFSIO -clean')