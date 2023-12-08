<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/logos_entidades.png" width="1000" height="300">
  </a>
  <h3 align="center">Consideraciones éticas para la formación de ingenieros en inteligencia artificial en Colombia</h3>

  <p align="Justify">
    Esta investigación tiene como objetivo explorar en diferentes facultades de ingeniería de Colombia cuál es la aproximación ética de los docentes y estudiantes durante la formación académica para el diseño y desarrollo de algoritmos en inteligencia artificial, al mismo tiempo describir la opinión, conocimientos y aplicación hipotética de la ética en la inteligencia artificial por parte de los estudiantes de pregrado en ingeniería y describir la opinión, conocimientos y uso en la enseñanza de la ética en la
inteligencia artificial por parte de los docentes de ingeniería; por último, sugerir contenidos mínimos en ética para un programa de formación en inteligencia artificial dentro de las facultades de ingeniería.

<!-- ABOUT THE PROJECT -->
## Sobre el repositorio
<p align="Justify">
En este repositorio se enuentra el código fuente en Python para realizar el proceso de extracción y descarga de datos (app.py) que se encuentran alojados en el servicio de Microsoft Forms de la siguiente forma:
<p align="Justify">
*El servicio de Jenkins dispara la tarea programada en un intervalo de tiempo de 10 segundos.
<p align="Justify">
*Este script a partir de autenticación por la cabecera MUID (Microsoft User ID) la cual permite la identificación única de un usuario propietario de un formulario y lograr el seguimiento de las repsuestas a dicho formulario; permite realizar una petición HTTPS para poder descargar un conjunto de bytes.
<p align="Justify">
*A partir de una función en este script se transforma el arreglo de bytes en un archivo de extensión .xlsx.
<p align="Justify">
*La nomenclatura que lleva este archivo es a partir de un formato compuesto por nombre base (encuesta-estudiantes) y la fecha del momento en el que se ejucuta este script (AAAA-MM-DD).
<p align="Justify">
Adicionalmente, se encuentra un archivo de extensión .ipynb (Jupyter Notebook) con el que se hizo el análisis de la base de datos recolectada por medio de la libreria propia de Python, Seaborn; con la que se realizó el relacionamiento de diferentes variables presentes en la base de datos para su posterior interpretación y documentación de la investigación. 

### Librerías

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/biblioteca_pandas_logo.jpg" width="370" height="120">
  </a>
<p align="Justify">
-Pandas: Es una poderosa biblioteca de Python utilizada para la manipulación y análisis eficiente de datos tabulares. Su estructura central es el DataFrame, que permite trabajar con datos en forma de tablas bidimensionales. Pandas facilita la carga y escritura de datos desde y hacia diversos formatos, así como operaciones avanzadas de indexación, selección y manipulación de datos. Además, ofrece herramientas para limpiar y preprocesar datos, realizar operaciones estadísticas y visuales, y es fundamental en tareas de análisis de datos y ciencia de datos en Python.
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/numpy-image-logo.jpg" width="360" height="100">
  </a>
<p align="Justify">
-Numpy: Es una biblioteca fundamental de Python para computación numérica. Proporciona estructuras de datos eficientes para arreglos multidimensionales y funciones que permiten operaciones matemáticas en estos arreglos de manera rápida. NumPy es esencial para tareas científicas y de ingeniería, ya que optimiza operaciones numéricas y facilita la manipulación de datos en forma de matrices. Su capacidad para realizar cálculos vectorizados mejora significativamente el rendimiento en comparación con las operaciones tradicionales de Python, haciéndolo un componente esencial en el ámbito de la programación científica y de datos.
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/seaborn-logo.png" width="360" height="130">
  </a>
<p align="Justify">
-Seaborn: Es una biblioteca de visualización de datos en Python que se construye sobre Matplotlib. Diseñada para crear visualizaciones atractivas y informativas con menos código, Seaborn simplifica la creación de gráficos estadísticos complejos. Ofrece funciones de alto nivel para la representación visual de distribuciones, relaciones y patrones en datos. Seaborn facilita la creación de gráficos como diagramas de dispersión, diagramas de caja, mapas de calor y más, con paletas de colores atractivas. Es una herramienta valiosa para analizar y comunicar patrones en datos, especialmente en el ámbito de la ciencia de datos y la exploración visual de conjuntos de datos.
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/matplotlib-logo.png" width="400" height="120">
  </a>
<p align="Justify">
-MatPlotlib: Es una biblioteca de visualización de datos en Python que proporciona una amplia gama de herramientas para crear gráficos estáticos, interactivos y personalizados. Permite crear gráficos 2D y 3D de alta calidad, así como diagramas de dispersión, barras, líneas, histogramas y más. Matplotlib es muy versátil y es utilizada tanto para visualizaciones simples como para gráficos más complejos en diversos campos, incluyendo ciencia de datos, investigación científica, ingeniería y más. Además, su integración con otras bibliotecas como NumPy y Pandas hace que sea una herramienta poderosa para representar y comunicar visualmente patrones y tendencias en los datos.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tecnologías

El análisis de la base de datos encontrada en este repositorio, llamada encuesta-estudiantes-2023-11-26.xlsx, que corresponde a la última versión recolectada, fueron necesarias las siguientes tecnologías.
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/excel-logo.png" width="240" height="80">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/forms-logo.png" width="240" height="80">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/jenkins-logo.png" width="240" height="80">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/python-logo.png" width="240" height="80">
  </a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Trabajo futuro
<p align="Justify">
La presente investigación se encuentra aún vigente en la recolección de información por medio de las encuestas a estudiantes de ingeniería de pregrado y docentes del área. Si gustas participar y sumar con tu experiencia sobre ética plaicada a la inteligencia artificial, aquí debajo encuentras los links habilitados para completar el formuario el cual es completamente anónimo y voluntario.
  
Link para estudiantes: https://forms.office.com/r/K4sng7t4sn
 

