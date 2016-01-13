Title: Problems with mpi4py and mvapich2 (on stampede)
Date: 2015-07-15 14:07
Modified: 2015-07-15 14:07
Category: computing
Tags: cluster, xsede, mpi, python
Slug: mpi4py-and-mvapich
Authors: adrn
Summary: resolving issues with mpi4py and mvapich2 on large compute clusters

In my research, I make use of our local compute cluster [Yeti]() to run large parallel jobs. I do almost all of my programming in Python, so I've been using mpi4py and especially [mpipool]() to distribute tasks over anywhere from 16-256 processors. Yeti uses [OpenMPI]() for MPI programming. Recently, the cluster has been maxed out by people running massive numbers of 1 node, 1 core jobs with 16 GB of memory and thus queue times for people like me are getting a bit out of control (3-4 days).

Luckily, I have a [startup allocation]() on [XSEDE](), so I do have access to other cluster resources. It was pretty easy to get set up on Stampede (one of the XSEDE clusters)---a nice surprise---but when I tried running some of my larger jobs (128 MPI tasks), the jobs failed with some rather opaque errors:

```
Fatal error in PMPI_Init_thread:
Other MPI error, error stack:
MPIR_Init_thread(436)...:
MPID_Init(371)..........: channel initialization failed
MPIDI_CH3_Init(285).....:
MPIDI_CH3I_CM_Init(1106): Error initializing MVAPICH2 ptmalloc2 library

[c425-201.stampede.tacc.utexas.edu:mpispawn_5][readline] Unexpected End-Of-File on file descriptor 17. MPI process died?
[c425-201.stampede.tacc.utexas.edu:mpispawn_5][mtpmi_processops] Error while reading PMI socket. MPI process died?
[c425-201.stampede.tacc.utexas.edu:mpispawn_5][child_handler] MPI process (rank: 85, pid: 33026) exited with status 1
[cli_18]: aborting job:
Fatal error in PMPI_Init_thread:
Other MPI error, error stack:
MPIR_Init_thread(436)...:
MPID_Init(371)..........: channel initialization failed
MPIDI_CH3_Init(285).....:
MPIDI_CH3I_CM_Init(1106): Error initializing MVAPICH2 ptmalloc2 library
...
and on and on and on...
```

TODO: how did I get it to work? (spoiler: I didn't yet...)
