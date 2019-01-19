FROM continuumio/miniconda3

RUN conda install -y -c conda-forge jupyterhub &&\
    conda install -y notebook

RUN pip install oauthenticator
RUN pip install requests

RUN useradd -m -d /home/user user &&\
    echo "user:123456" | chpasswd

RUN mkdir -p /configs/

COPY jupyterhub_config_github.py /configs/
COPY jupyterhub_config_ultraauth.py /configs/

RUN chown -R root:root /configs/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

