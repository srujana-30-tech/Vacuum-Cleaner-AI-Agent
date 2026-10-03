# Vacuum Cleaner AI Agent

## 📌 Description

This project implements a simple **AI Vacuum Cleaner Agent** using Python. The vacuum cleaner operates in two rooms, **Room A and Room B**, and automatically cleans the rooms based on their current condition.

The program demonstrates the basic concept of an **intelligent agent** that observes the environment and performs actions accordingly.

## 🎯 Objective

The main objective is to simulate a vacuum cleaner that:

* Detects whether a room is Clean or Dirty.
* Cleans the room if it is Dirty.
* Moves to the other room if the current room is already Clean.
* Stops when both rooms are clean.

## 🧠 How It Works

1. The program randomly assigns **Clean** or **Dirty** status to Room A and Room B.
2. The vacuum cleaner randomly starts in either Room A or Room B.
3. The vacuum checks the status of its current room.
4. If the room is Dirty, it performs the **Suck** action and cleans it.
5. If the room is Clean, it moves to the other room.
6. The process continues until both rooms become Clean.
7. The program then displays the final status.

## 🛠️ Technologies Used

* **Python**
* `random` module
* Basic AI Agent concepts
* Conditional statements
* Loops
* Dictionaries
* Functions

## 📂 File Structure

```text
Vacuum 1.py
README.md
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python "Vacuum 1.py"
```

## 💡 Example Output

```text
Initial States: {'A': 'Dirty', 'B': 'Clean'}
Vacuum cleaner starting at Room A
----Cleaning Process----

Vacuum is in Room A | Status: Dirty
Action: Suck the dirt in room A

Vacuum is in Room A | Status: Clean
Action: Move right to room B

Vacuum is in Room B | Status: Clean
Action: Move left to room A

Both the rooms are clean!
Final Status: {'A': 'Clean', 'B': 'Clean'}
```

## 🤖 AI Concept Used

This program represents a **Simple Reflex Agent**.

The vacuum cleaner makes decisions based on the current state of the environment:

```text
If Room is Dirty → Suck
If Room is Clean → Move
If Both Rooms are Clean → Stop
```

## ✨ Features

* Random room conditions
* Random starting location
* Automatic cleaning
* Automatic movement
* Stops when all rooms are clean
* Demonstrates basic Artificial Intelligence agent behavior

## 📚 Learning Outcome

By completing this program, we understand how an AI agent can:

* Perceive the environment
* Make decisions based on the current state
* Perform appropriate actions
* Continue acting until the goal is achieved

## 👩‍💻 Author

**Srujana Pujar**

## 📄 License

This project is created for educational and learning purposes.
