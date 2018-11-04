# JupyterHub - deauthorized


## Build it

To build this (Docker) container just go for:

```bash
$ docker build -t myjupyterhub dockerfile/.
```

The image from `continuumio/miniconda3` is inherited, the
setup of JupyterHub and Notebook should be a smooth 5-minutes run.


## Run it

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


## Access it

*JupyterHub* container running, (in your host) go to your browser
and ask for:
```
http://localhost:8000
```
A *login* screen should be answered to you.

You may now authenticate -- and use Jupyter-notebooks -- with the
default user:
```
Username: user
Password: 123456
```

## GitHub authentication

To authenticate using GitHub is a pretty straightforward process.
The file `jupyterhub_config_github.py` is set to authenticate using
GitHub OAuth interface.

Before running JupyterHub with the config, though, you have to create a OAuth App
in your GitHub's Developer settings.
In this step you'll need to give the App (this jupyterhub container) a name (any name you want),
a Homepage URL (I associated with my PC's dynamic DNS as from No-IP, but I don't really know
how important this is, also because in reality my port 8000 is blocked) and a
callback URL.

The figure below shows pretty much my setup.
![GitHub Oauth App settings](github_oauth_app_settings.png)

After creating the App, the site will give you an `Client ID` and `Client Secret`,
those values we have to define as variables `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`
in our container's environment. Those variables will be read by our *config.py* when
we start the service:

```bash
$ jupyterhub -f jupyterhub_config_github.py
```

By now, JupyterHub should be running, accessible through URL `http://localhost:8000`
and ready to authenticate using GitHub.

/.\

## Demo Steps:

- 1. Run docker container
- 2. Review config.yaml
- 3. Create UltraAuth Application (access id / secret)
- 4. Update config.yaml
- 5. Update UltraAuth Application settings with JupyterHub instance oauth_callback / oauth_logout
- 6. Authenticate using UltraAuth
