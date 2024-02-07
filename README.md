# HPQC
Sviluppare degli script, che in base ad un file di configurazione, configurano il file system distribuito (esistono dei comandi). Gli esperimenti devono essere estendibili e replicabili ed eventualmente portabili sul cluster fisico.
Benchmark di Yarn in base alle configurazioni su DFSIO/Teragen, il benchmark sono lanciati in parallelo agli script di misura.
Il file system è virtualmente distribuito perché i vari componenti sono dei container.


# Table of Contents
1. [Apache Hadoop](Hadoop.md)
1. [Parameters Description](Parameters.md)
1. [Exeperiments ???](Experiments.md)
1. [Environment Setup](Setup.md)
1. [Troubleshooting](Troubleshooting.md)
1. [References](References.md)

# Cose da fare
* Approfondimento parametri di riconfigurazione (timeouts, num mappers, num reducers, buffer size, scheduling policy, Resource Profiles, num threads, mb, vcores, ...)
* Esperimenti con workload DFSIO (variabili di risposta : num threads, num mappers, num reducers)
* Gli script generati devono essere portati sul cluster fisico









