# Manual de Usuario "SimpleQL"
Este Programa permite poder meter reportes JSON y hacer distintas acciones en estos archivos, estos archivos solo tienen 4 atributos:Promedio,Nombre,Edad y Activo.
Al ejecutar el main se le pedira ingresar un comando, estos comandos utilizables son:
 * cargar
 * seleccionar
 * maximo
 * minimo
 * suma
 * cuenta
 * reportar
 * salir
los comandos ingresados pueden ser tanto Mayusculas y Minusculas.la primera vez que lo corren, debe cargar los archivos, de otra forma no le permitira hacer otro 
comando dando el mensaje "No hay archivos cargados", una vez cargado 1 archivo puede seguir agregando o utilizar el resto de comandos.

### **Comandos**
cada comando tiene su uso especial y acciones.
* cargar: carga los archivos JSON uno o N cantidades
uso: cargar archive1.json,archive2.json, ... ,archiven.json
 * seleccionar:hace una consulta de alguno o todos los atributos cargados
 uso: seleccionar * (para seleccionar todos) , seleccionar nombre,edad,activo
 * maximo: hace una consulta para  los atributos con numeros(edad,promedio) de los archivos cargados devolviendo el maximo de estos
 uso: maximo edad ó maximo promedio
 * minimo: hace una consulta para  los atributos con numeros(edad,promedio) de los archivos cargados devolviendo el minimo de estos
 uso: minimo edad ó minimo promedio
 * suma: hace una suma de  los atributos con numeros(edad,promedio) de los archivos cargados 
 uso: suma edad ó suma promedio
 * cuenta: hace una cuenta de todos los archivos ingresados en la memoria solo menciona los archivos.
 uso:cuenta
 * reportar: hace un reporte de un archivo generando un html y abriendolo, se accede mencionando el numero de archivo que es
 en la cuenta sabemos cuantos archivos hay, solo se cuenta de 0 a N-1 cantidad que aparece en cuenta
 uso: reportar 0 hasta reportar 9 (suponemos que hay 10 archivos)
 * salir: permite salir de el menu de ingreso de comandos


