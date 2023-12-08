<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/Valentina042/Consideraciones-eticas-en-Colombia/blob/main/static/logos_entidades.png" width="650" height="300">
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



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
