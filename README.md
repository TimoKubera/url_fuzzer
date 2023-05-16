<a name="readme-top"></a>
[![MIT License][license-shield]][license-url]
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TimoKubera/url_fuzzer">
    <img src="https://raw.githubusercontent.com/TimoKubera/url_fuzzer/main/img/url_fuzzer.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center"><b>URL Fuzzer</b></h3>

  <p align="center">
  Prüft, ob es auf einer Website bestimmte Subpages gibt.</p>
    <br />
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Inhalt</summary>
  <ol>
    <li>
      <a href="#about-the-project">Über das Projekt</a>
    </li>
    <li>
      <a href="#requirements">Requirements</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">Lizenz</a></li>
    <li><a href="#contact">Kontakt</a></li>
  </ol>
</details>

<a name="about-the-project"></a>
<!-- ABOUT THE PROJECT -->
## Über das Projekt

Die Software kann verwendert werden, um zu prüfen, ob es auf einer Website bestimmte Subpages gibt. Sie kann über ein CLI ausgeführt werden und sowohl Website, als auch Subpages werden als Argumente im Terminal übergeben.
</br>

Anwendungen:
* IT Security, reconnaissance
* Bug Bounty 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<a name="requirements"></a>
<!-- GETTING STARTED -->
## Requirements
Es ist Python>=3.6 erforderlich, um das Programm auszuführen, sowie die Installation der folgenden Packages:
* requests

### Installation

1. Die Repo von <a href="https://github.com/timokubera/iira">GitHub</a> clonen.
2. Abhängigkeiten installieren
   ```sh
   pip3 install requests
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="usage"></a>
<!-- USAGE EXAMPLES -->
## Usage
<b>Programm ausführen</b></br>
Beispielaufruf mit der Website https://www.example.org und den subpages https://www.example.org/page1 ubnd https://www.example.org/page2.
Die einzelnen Subpages werden mit einem Semikolon getrennt.
   ```sh
   python main.py -u "https://www.example.org" -s "page1;page2"
   ```

Alternativ kann auch der Pfad zu einer .txt-Datei angegeben werden, in der die subpages zeilenweise gespeichert sind.
   ```sh
   python main.py -u "https://www.example.org" -p "~/path/to/file/wordlist.txt"
   ```

Auf dem folgenden Bild wird ein Beispielaufruf des Programms dargestellt:
<img src="https://raw.githubusercontent.com/TimoKubera/url_fuzzer/main/img/url-fuzzer-results.png" alt="url-fuzzer-results">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="license"></a>
<!-- LICENSE -->
## Lizenz

Das Projekt wurde unter der MIT-Lizenz veröffentlicht. Siehe in die `LICENSE.txt` für weitere Informationen.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="contact"></a>
<!-- CONTACT -->
## Kontakt
Mail: [mail@timokubera.it](mailto:mail@timokubera.it)

Project Link: [https://github.com/TimoKubera/IIRA](https://github.com/TimoKubera/IIRA)

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