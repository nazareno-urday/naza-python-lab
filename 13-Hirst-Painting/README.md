<div align="center">



\# 🎨 Hirst-Inspired Dot Painting



\*\*One hundred colorful dots. A different composition every time.\*\*



!\[Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square\\\&logo=python\\\&logoColor=white)

!\[Graphics](https://img.shields.io/badge/Graphics-Turtle-2EA44F?style=flat-square)

!\[Status](https://img.shields.io/badge/Status-Complete-2EA44F?style=flat-square)



</div>



\---



\## 🖼️ The experiment



Generate a colorful 10 × 10 dot painting inspired by the visual style of Damien Hirst's spot paintings.



The RGB color palette was originally extracted from a reference painting using `colorgram.py`. The final palette is stored directly in the program, so each execution can randomly create a new composition.



\## 📸 Preview



!\[Generated Hirst-inspired dot painting](preview.png)



\## ⚙️ How it works



The turtle begins in the bottom-left corner and moves horizontally across the canvas.



For every position, the program:



1\. Randomly selects an RGB color from the extracted palette.

2\. Draws a colored dot.

3\. Moves to the next position.

4\. Repeats the process across ten rows.



Because the colors are selected randomly, every generated painting is unique.



\## 🧠 Practiced here



`Turtle graphics` · `RGB colors` · `Tuples` · `Nested loops` · `Random selection` · `Coordinates`



\## 📁 Project structure



```text

Hirst-Painting/

├── main.py

├── preview.png

└── README.md

```



\## 🚀 Run locally



Clone or download the project and run:



```bash

python main.py

```



No external dependencies are required. `turtle` and `random` are included with Python.



\## 📝 Note



This project was created for educational purposes while learning Python graphics and working with RGB color palettes.



It is an independent programming exercise and is not affiliated with the original artist.



