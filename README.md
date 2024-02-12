# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni con workload DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.
Il file system è virtualmente distribuito perché i vari componenti sono dei container.


# Table of Contents
1. [Apache Hadoop](Hadoop.md)
1. [Environment Setup](Setup.md)
    * [Overview](Setup.md#Overview)
        *  [Hadoop 3.3.5](Setup.md#hadoop_3.3.5)
    * 
1. [Parameters Analisys ???](Parameters.md)
1. [Exeperiments ???](Experiments.md)
1. [Troubleshooting](Troubleshooting.md)
1. [References](References.md)

# Cose da fare
* Approfondimento parametri di configurazione per scheduling e calcolo (timeouts, num mappers, num reducers, buffer size, scheduling policy, Resource Profiles, num threads, mb, vcores, ...)
* Esperimenti con workload DFSIO (variabili di risposta DataNode : num threads, num mappers, num reducers)









