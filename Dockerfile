FROM ubuntu
RUN apt-get update && apt-get install python3-pip -y && apt-get install python3-dev -y
WORKDIR /tarefa
COPY halfstack  /tarefa/halfstack/
COPY pedido  /tarefa/pedido/
COPY itens /tarefa/itens/
COPY cliente /tarefa/cliente/
COPY empresa /tarefa/empresa
COPY produto /tarefa/produto/
COPY manage.py /tarefa/
COPY db.sqlite3 /tarefa/
COPY requirements.txt /tarefa/
RUN pip3 install --upgrade pip
RUN pip3 install -r /tarefa/requirements.txt 
EXPOSE 5000
CMD ["python3", "manage.py", "runserver", "127.0.0.1:5000"]