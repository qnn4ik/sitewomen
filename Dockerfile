FROM python:3.10

SHELL ["/bin/bash", "-c"]

# set environment variables
# no .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# no logs is bufferized
ENV PYTHONUNBUFFERED 1

# execute cmds with SHELL
RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc locales vim

RUN useradd -rms /bin/bash sitewomen && chmod 777 /opt /run

# as root do mkdir `sitewomen` && cd `sitewomen`
WORKDIR /sitewomen

# media and static files
RUN mkdir /sitewomen/static && mkdir /sitewomen/media && chown -R sitewomen:sitewomen /sitewomen && chmod 755 /sitewomen

# copy all files from local to docker container's workdir
COPY --chown=sitewomen:sitewomen . .

# install dependencies
RUN pip install -r requirements.txt

USER sitewomen

# change test web server on gunicorn ???
CMD ["python3", "manage.py", "runserver", "localhost:8080"]
