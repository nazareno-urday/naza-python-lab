<div align="center">

# ❓ Quiz Game — OOP Edition

**Twelve questions. Two possible answers. One stateful quiz engine.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-222222?style=flat-square)
![Paradigm](https://img.shields.io/badge/Paradigm-OOP-6f42c1?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=flat-square)

</div>

---

## ⚙️ The experiment

Answer a sequence of true-or-false questions while the program tracks your position and score throughout the complete quiz.

Question dictionaries are converted into `Question` objects and passed to a `QuizBrain` object, which controls the question flow, checks each answer, updates the score, and determines when the quiz is complete.

## 🧩 Project design

| Component   | Responsibility                                       |
| ----------- | ---------------------------------------------------- |
| `Question`  | Models the text and correct answer of one question   |
| `QuizBrain` | Controls quiz progress, answer checking, and scoring |
| `data.py`   | Stores the raw question dictionaries                 |
| `main.py`   | Builds the question bank and runs the quiz           |

## 📁 Required project files

All Python files must remain together in the same directory because `main.py` imports the other project modules.

```text
12-Quiz-Game-OOP/
├── data.py
├── main.py
├── question_model.py
├── quiz_brain.py
└── README.md
```

The four `.py` files are required to run the application. `README.md` contains the project documentation and is not used by the program itself.

## 🧠 Practiced here

`Object-oriented programming` · `Classes` · `Objects` · `Constructors` · `Methods` · `Lists of objects` · `Dictionary transformation` · `Object collaboration` · `State tracking` · `Modular design`

## 🎮 How to play

For every question, enter exactly one of the following answers:

```text
True
False
```

The program immediately checks your answer, displays your current score, and continues until every question has been answered.

## ▶️ Run it

Clone the complete repository:

```powershell
git clone https://github.com/nazareno-urday/naza-python-lab.git
```

Enter the project directory:

```powershell
cd naza-python-lab/12-Quiz-Game-OOP
```

Run the application:

```powershell
py main.py
```

### Requirements

* Python 3.x
* All included Python modules kept in the same directory
* No third-party packages required

## 🧪 Lab note

This experiment explores how raw dictionary data can be transformed into objects and managed by a separate quiz engine.

The program keeps question data, question modeling, quiz behavior, and application flow in independent modules with clearly defined responsibilities.

> Next mutation: accept case-insensitive answers, randomize the questions, and load new questions from an external API.

---

*Built during a guided Python challenge. Written, tested, and debugged by me.*
