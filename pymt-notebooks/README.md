# pymt-notebooks

Run the pymt demo Notebooks from a Docker container.
The technique is based on material from https://github.com/austinbrian/jupydocker.

Build the image with:
```
docker build --tag pymt-notebooks .
```

Launch a container with:
```
docker run --publish 8899:8888 --rm pymt-notebooks 
```

Open http://localhost:8899 in a web browser and enter the token `csdms` when prompted.
Select the **welcome.ipynb** Notebook to start.

To finish, hit `Ctrl-C` in the terminal where the container is running.
