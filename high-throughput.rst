High-throughput computing
=========================

A frequent problem in research is the need to run lots of analysis scripts which may take a long time to run.
These scripts frequently need access to large amounts of system resources and data, and so they're ill-suited to running on a normal user machine.

The solution to this problem comes in the form of *batch processing* or *high throughput computing*.
This is normally done by setting up a machine, or a cluster of networked machines, which can access resources over a period of days, weeks, or even months.


.. sidebar:: High-performance computing

   High-throughput computing constrasts with another paradigm, *high-performance computing*, or HPC.
   While The two share some common elements, HPC is normally assosicated with jobs which are highly parallelised, and which consume very large amounts of resources for a comparitively short amount of time.


``htcondor``: Scheduling jobs
-----------------------------

Submitting a jobs to condor
---------------------------

Checking the status of condor jobs
----------------------------------
