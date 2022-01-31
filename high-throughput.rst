High-throughput computing
=========================

A frequent problem in research is the need to run lots of analysis scripts which may take a long time to run.
These scripts frequently need access to large amounts of system resources and data, and so they're ill-suited to running on a normal user machine.

The solution to this problem comes in the form of *batch processing* or *high throughput computing*.
This is normally done by setting up a machine, or a cluster of networked machines, which can access resources over a period of days, weeks, or even months.

.. sidebar:: High-performance computing

   High-throughput computing constrasts with another paradigm, *high-performance computing*, or HPC.
   While The two share some common elements, HPC is normally assosicated with jobs which are highly parallelised, and which consume very large amounts of resources for a comparitively short amount of time.

.. note:: HTCondor 9

   These notes should be generally relevant to all versions of condor, but they've been written to align with version 9 of htcondor, which at the time of writing was the latest stable version.
   The `documentation <https://htcondor.readthedocs.io/en/feature/>`_ for this version of htcondor are substantially improved over earlier versions, too, which is a major bonus.
   

``htcondor``: Scheduling jobs
-----------------------------

High throughput computing (HTC) facilities are normally in high-demand, and if capacity was planned around the times of day when most people wanted to use them we'd end up with a very expensive facility which went largely unused at night.
To circumnavigate this HTC clusters are designed to queue jobs up, and run them when they have the available resources.
For some jobs this can be frustrating or unsuitable, but for many tasks in the natural sciences, where we don't need instant results, this is fine.

An unfortunate consequence of this is that we need to do a little more work to get a job running, and we need to write something akin to an advertisment for the cluster, so that it knows a job is available to run when it gets a chance.
Initially I'll describe how to get a very simple job running on an htcondor cluster, simply as an illustration, but as you get more familiar with the process you will find that some changes are needed in the way that you write code to take best advantage of the strengths of HTC.

.. sidebar:: HTCondor Clusters

	     Throughout these notes I'll make many reference to "clusters"; this is a term frequently used in HTC parlence, and refers to groupings of computers which share the load of running submitted jobs.
	     Different approaches to constructing such a cluster exist: sometimes all of the machines will be near-identical, running the same operating system, with the same processors.
	     Perhaps more frequently you'll encounter "heterogeneous" clusters, which are composed of a range of different types of machine running different OSes.
	     HTCondor allows the construction of such clusters (they can even be constructed from desktop machines set to run jobs when they're not being used), but allows jobs to specify the kind of machine they must run on, if it's important.
	     HTCondor normally refers to this collection of computers as a "pool"; there are probably some slight differences between what people mean by cluster and what HTCondor means by pool, but for most purposes they're one and the same.

In keeping with the majority of these notes I'm going to use ``python`` to write the demonstration script, but it should work equally well with other interpretted languages.
If you're using a compiled language, especially ``C``, then things might be a little trickier.

The job we're going to schedule will just write out some text to ``stdout``.

.. code-block:: python

		print("Hello htcondor!")

So let's see how we get this to run.

Submitting jobs to condor
-------------------------

Checking the status of condor jobs
----------------------------------

Condor and GPUs
---------------

Constructing complex jobs
-------------------------
