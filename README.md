# Slurm-Hydra-Submitit

This repository is a minimal working example on how to:

- setup [Hydra](https://github.com/facebookresearch/hydra)
- setup batch of slurm jobs on top of Hydra via
  [submitit-launcher](https://hydra.cc/docs/next/plugins/submitit_launcher/)

## Set up Hydra

> :warning: You need to install `hydra-core` for this step.

Hydra is fairly easy to set-up:

- [one .yaml configuration](./slurm_hydra_submitit/configuration.yaml)
  file containing the default config values
- a [`@hydra.main` wrapper](./slurm_hydra_submitit/script.py#L15) on your
  main experiment function to pass the configurations values as argument.

By simply running `python slurm_hydra_submitit/script.py`, you'll see
how the main function takes the arguments from the configuration file and pass
them to the following underlying functions.

## Launch jobs on a SLURM cluster with Hydra submitit launcher

### Launch a job on the cluster

> :warning: You need to install `hydra-submitit-launcher` for this step.

Now that our Hydra conf is setup, we want to run the job on a SLURM cluster
instead of our local computer. For that, we need to:

- specify the hydra launcher to work on the SLURM cluster
- specify the hardware specifications for the SLURM job

If you connect to your SLURM cluster scheduler node, just by installing
`hydra-submitit-launcher`, you can already launch jobs on the cluster with:

`python slurm_hydra_submitit/script.py --multirun hydra/launcher=submitit_slurm`

To test locally before sending to the cluster, you can switch the `hydra/launcher`
argument to `submitit_local`.

### Adapt node parameters

You can easily adapt the SLURM parameters by modifying the
[following arguments](cpus_per_task) SLURM launcher arguments.


For example, the following script is executed on nodes with 10 CPUs:
`python slurm_hydra_submitit/script.py --multirun hydra/launcher=submitit_slurm hydra.launcher.cpus_per_task=10`

## Launch array of jobs on the SLURM cluster

### Grid Search

You can launch multiple jobs at once by specifying their values in the launch command.

For example, the following command launches 4 jobs which corresponds to all
the possible combinations of arguments.

`python slurm_hydra_submitit/script.py --multirun hydra/launcher=submitit_slurm project_name=P1,P2 train.epochs=30,40`

### Specific Parameters Combinations

<!-- This section is a backlink for Jean Zay docs. Be careful if changing name of the section. -->

Alternatively, you can pass sets of parameters to test together:

`python slurm_hydra_submitit/script.py --multirun hydra/launcher=submitit_slurm +compile="{project_name:P1,train.epochs:30}, {project_name:P2,train.epochs:40}"`

To clean this command a bit, we can create a bash script similar to this:

```bash
#!/bin/bash
params=(
    '{project_name:P1,train.epochs:10},'
    '{project_name:P2,train.epochs:20}'
)

slurm_hydra_submitit/script.py --multirun hydra/launcher=submitit_slurm +compile="${params[*]}"
```
