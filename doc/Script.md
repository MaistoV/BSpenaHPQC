# Script in detail

## Control Flow <a name="flow_control"></a>
```mermaid
stateDiagram-v2
    state fork_state <<fork>>
    state join_state <<join>>
    s1: Dataframes Creation
    s2: Cluster Configuration
    s3: Start Cluster in Pseudo-Distributed Mode
    s4: Start TestDFSIO and Online Test
    s4_1 : Online Test
    s5: Start Offline Test
    s6: Clean up TestDFSIO results
    s7: Save Response Variables
        
        [*] --> s1
        s1 --> s2
        s2 --> s3
        s3 --> s4
        s4 --> fork_state
        fork_state --> TestDFSIO
        fork_state --> s4_1

        TestDFSIO --> join_state
        s4_1 --> join_state
        join_state --> s5
        s5 --> s6
        s6 --> s7
        s7 --> [*]
```

## Script Structure <a name="script_struc"></a>
The Test Cases Script has 5 different files :
* `hdfs_test.py` : Python "main" script.
* `hdfs_test_utils.py` : Python file which holds the functions implementations.
* `hdfs_test_conf.py` : Python file which holds the variables needed by the script.
* `start_hadoop_cluster.sh` : Bash script which holds the line commnds to stop and start the hadoop cluster.
* `test_list.csv` : CSV file which holds the configuration paramters.


## Python Modules <a name="python_mod"></a>
* `xml.etree.ElementTree` : Module for parsing and creating XML data.
* `subprocess` : Module to spawn new processes and capture stout/stderr.
* `pandas` : Module for data manipulation and analysis.
* `os` : Module to use OS-dependent functionality.
* `multiprocessing` : Module to spawn new processes.
* `requests` : For HTTP requests


## How to Run <a name="run"></a>
### Prerequisites
* Set indipendent factors and TestDFSIO flags as the first row of `test_list.csv` file.
* Set variables in `hdfs_test_conf.py`.

### Run
```bash
$ cd script
$ python3 hdfs_test.py
```