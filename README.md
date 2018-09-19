# JupyterHub - deauthorized


# Build it

To build this (Docker) container just go for:

```bash
$ docker build -t myjupyterhub dockerfile/.
```

The image from `continuumio/miniconda3` is inherited, do the
setup of JupyterHub and Notebook should be a smooth 5 minutes run.


# Run it

When you run the image (`myjupyterhub` in this case),
```bash
$ docker run --rm -it -p 8000:8000 myjupyterhub
```
, you'll then be sitting inside the container as `root` (default).

Run *JupyterHub* as:
```bash
$ jupyterhub --no-ssl
```
Which will start *JupyterHub* at por `8000` (default).


# Access it

*JupyterHub* container running, (in your host) go to your browser
and ask for:
```
http://localhost:8000
```
A *login* screen should be answered to you.

You may now authenticate -- and user Jupyter-notebooks -- with the 
default user:
```
Username: user
Password: 123456
```


/.\

