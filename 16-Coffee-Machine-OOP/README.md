<div align="center">

# ☕ Coffee Machine — OOP Edition

**Four focused classes. Three drinks. One complete transaction flow.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-222222?style=flat-square)
![Paradigm](https://img.shields.io/badge/Paradigm-OOP-6f42c1?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=flat-square)

</div>

---

## ⚙️ The experiment

Order an espresso, latte, or cappuccino while a group of collaborating objects manages the complete transaction.

The machine verifies its available ingredients, processes the inserted coins, calculates change, tracks profit, and deducts resources after every successful purchase.

Administrative commands can display the current machine state or shut the program down.

## 🧩 Project design

| Component      | Responsibility                                        |
| -------------- | ----------------------------------------------------- |
| `MenuItem`     | Models a drink, its price, and required ingredients   |
| `Menu`         | Stores the available drinks and searches for an order |
| `CoffeeMaker`  | Tracks resources and prepares each drink              |
| `MoneyMachine` | Processes coins, payments, change, and profit         |
| `main.py`      | Coordinates the application flow                      |
| `art.py`       | Stores the Coffee Machine ASCII artwork               |

## 📁 Required project files

All Python files must remain together inside the same directory because `main.py` imports the other modules.

```text
16-Coffee-Machine-OOP/
├── art.py
├── coffee_maker.py
├── main.py
├── menu.py
├── money_machine.py
└── README.md
```

The five `.py` files are required to run the application. `README.md` contains the project documentation and is not used by the program itself.

## 🧠 Practiced here

`Object-oriented programming` · `Classes` · `Objects` · `Constructors` · `Methods` · `Attributes` · `Object collaboration` · `Modular design` · `State management`

## 🎛️ Available commands

| Command      | Action                                    |
| ------------ | ----------------------------------------- |
| `espresso`   | Orders an espresso                        |
| `latte`      | Orders a latte                            |
| `cappuccino` | Orders a cappuccino                       |
| `report`     | Displays resources and accumulated profit |
| `off`        | Shuts down the machine                    |

## ▶️ Run it

Clone the complete repository:

```powershell
git clone https://github.com/nazareno-urday/naza-python-lab.git
```

Enter the project directory:

```powershell
cd naza-python-lab/16-Coffee-Machine-OOP
```

Run the application:

```powershell
py main.py
```

### Requirements

* Python 3.x
* All included project modules kept in the same directory
* No third-party packages required

## 🧪 Lab note

This project is the object-oriented evolution of the original procedural Coffee Machine challenge.

Instead of keeping every responsibility inside one script, the application separates menu management, resource control, payment processing, and drink preparation into specialized classes.

> Next mutation: add stronger coin-input validation and automated tests for payments and resource consumption.

---

*Built during a guided Python challenge. Refactored, tested, and debugged by me.*
