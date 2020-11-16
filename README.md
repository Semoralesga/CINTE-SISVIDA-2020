# CINTE-SISVIDA-2020

### feature/dba
- Punto 0.1.1: Fue realizado en Draw.io se adjuntan el xml, png que genera la plataforma.
- Punto 0.1.2: Fue realizado en MySql WorkBench.

### feature/back
- Punto 0.2.1: Los diagramas fueron realizados en Draw.io y para cada uno se exporto un png y archivo draw.io. Se implemento el codigo en Java una parte del codigo de adapto de Codigo tomado de https://www.w3schools.com/java/java_files_create.asp y https://www.oscarblancarteblog.com/2014/07/18/patron-de-diseno-factory/
- Punto 0.2.2: Se encuentra en una presentacion con nextension .odp(Open Document Presentation).

### feature/api
- Punto 0.3.1: Se encuentra dentro la carpeta `RestFull` fue escrito en python3 puro utilizando la libreria http server. Se ejecuta con el comando `python3 server.py`, se puede probar en `localhost:8080/cycling_teams`, este codigo fue adaptado de los siguientes videos https://www.youtube.com/watch?v=s105UdO6nVQ y https://www.youtube.com/watch?v=m2NRZimOIWg, la parte de la autenticacion fue adaptada de https://gist.github.com/dragermrb/108158f5a284b5fba806#file-server-py-L20
- Punto 0.3.2: Se encuentra dentro la carpeta `GraphQL`, fue escrito en python3 y fue basado totalmente en https://tartiflette.io/docs/tutorial/getting-started, no conocia la herramienta y desarrollando el tutorial, me parecio muy interesante. Se puede probar en `http://localhost:8080/graphiql`

### feature/front
- Punto 0.4.2: Se desarrollo en Angular 10 con Node 10.23, para este utilice un CRUD de python hecho en flask muy similar al del punto 0.3.1, este se encuentra en la carpeta `backend` y se levanta ejecuntado el `.sh` de nombre `bootstrap.sh` y pone el api en `localhost:3030`. Para la parte web se realizaron todos los puntos, exceptuando el ultimo ya que Angular ya posee un pipe de Date el cual es muy completo y este se ejecuta haciendo `npm install` y `luego ng serve`
