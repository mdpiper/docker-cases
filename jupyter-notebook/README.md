# jupyter-notebook

An example of running a Jupyter Notebook from a Docker container.
The example is based on material from https://github.com/austinbrian/jupydocker.

Build the image with:
```
docker build --tag jupyter-notebook .
```

Launch a container with:
```
docker run --publish 8899:8888 --rm jupyter-notebook 
```

Open http://localhost:8899 in a web browser and enter the password `csdms` when prompted.
Select the **shell-commands.ipynb** notebook and run it.

To finish, hit `Ctrl-C` in the terminal where the container is running.
