# Python Learning Journey with Kako 🚀

Welcome to my Python learning guide! This collection of lessons dives into core concepts in Python, all through fun, themed examples inspired by Andalusian scholars, gladiators, warriors, and the beauty of math and time. Let’s explore the magic behind Python’s power! 🐍✨

## Table of Contents 📜
1. [Lesson 08: Modules and Functions 🛠️](#lesson-08-modules-and-functions)
2. [Lesson 09: Exception Handling ⚠️](#lesson-09-exception-handling)
3. [Lesson 10: File Handling 🗂️](#lesson-10-file-handling)
4. [Lesson 11: The Math & DateTime Calendar 🧮📅](#lesson-11-the-math--datetime-calendar)

---

## Lesson 08: Modules and Functions 🛠️

### Concepts:
- **Modules**: External libraries in Python that provide functionality (e.g., `math`, `random`).
- **Functions**: Blocks of code designed to perform specific tasks, improving code reusability.

### Code Types:
- **Basic Functions**: Creating functions to check a number’s status, greet, and calculate the square of a number.
- **Loops**: Repeating tasks like countdowns and displaying items from a list.
- **Function Calls**: Using functions to execute various tasks, like greeting and calculation.

### Example:
```python
def check_status(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
```

---

## Lesson 09: Exception Handling ⚠️

### Concepts:
- **Exception Handling**: Mechanism to handle errors gracefully without crashing the program.
- **Custom Exceptions**: Creating exceptions that are specific to your program's needs.

### Code Types:
- **Try/Except Block**: Handle errors by trying a block of code and catching exceptions if they occur.
- **Raising Exceptions**: Triggering errors when something goes wrong (e.g., broken armour or no sword).

### Example:
```python
class ArmourError(Exception):
    pass

class Gladiator:
    def __init__(self, armour):
        self.armour = armour

    def wear_armour(self):
        try:
            if self.armour == "broken":
                raise ArmourError("The armour is broken! Cannot wear it.")
            elif self.armour == "no_armour":
                raise ArmourError("No armour to wear!")
            else:
                print("The gladiator is wearing the armour!")
        except ArmourError as e:
            print(f"Error: {e}")
```

---

## Lesson 10: File Handling 🗂️

### Concepts:
- **File Operations**: Reading from and writing to files in various formats like text, CSV, and JSON.
- **Data Preservation**: Storing knowledge and data in files for future use.

### Code Types:
- **Text Files**: Reading and writing simple text.
- **CSV Files**: Storing data in a structured format (rows and columns).
- **JSON Files**: Storing data in a flexible, readable format for structured storage.

### Example:
```python
# Writing to a text file
with open("andalusian_scroll.txt", "w") as file:
    file.write("Scholars like Ibn Rushd and Al-Zahrawi changed the world with their wisdom.\n")

# Reading from a text file
with open("andalusian_scroll.txt", "r") as file:
    print(file.read())
```

---

## Lesson 11: The Math & DateTime Calendar 🧮📅

### Concepts:
- **Time Handling**: Using Python’s `time`, `datetime`, and `calendar` modules to manage and manipulate dates and times.
- **Math Operations**: Performing basic mathematical operations like calculating square roots, exponents, and working with constants like π.
- **NaN Handling**: Understanding and working with “Not a Number” (NaN) in Python.

### Code Types:
- **Time Manipulation**: Getting the current time, formatting it, and converting epoch time.
- **Calendar Functions**: Displaying a calendar for specific months.
- **Math Functions**: Performing standard operations like logarithms and square roots.
- **NaN Check**: Checking if a value is `NaN`.

### Example:
```python
import math
import datetime

# Current time
now = datetime.datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("🕒 Current DateTime:", formatted_now)

# Math operations
print("π (pi):", math.pi)
print("√16:", math.sqrt(16))
```

---

## Summary of Code Types 📝

### 1. **Lesson 08: Modules and Functions**
- **Function Definitions**: Creating reusable code blocks.
- **Loops and Iterations**: Performing repetitive tasks (e.g., countdown).
- **Function Calls**: Executing specific tasks with parameters.

### 2. **Lesson 09: Exception Handling**
- **Try/Except Blocks**: Safely handling errors.
- **Raising Custom Exceptions**: Defining unique error messages when specific conditions occur.

### 3. **Lesson 10: File Handling**
- **Reading/Writing Files**: Working with text, CSV, and JSON files.
- **Appends and Modifications**: Modifying existing files or appending new data.

### 4. **Lesson 11: The Math & DateTime Calendar**
- **Time Operations**: Using Python’s `time`, `datetime`, and `calendar` libraries to work with dates and times.
- **Mathematical Operations**: Using Python’s `math` module for calculations.
- **NaN Handling**: Identifying and working with `NaN` values using `math.isnan()` and `numpy.isnan()`.

---

## Conclusion 🎉

These lessons lay the foundation for effective coding with Python, helping you handle **functions**, **exceptions**, **files**, and **math/time operations** in an engaging way. Whether you're a gladiator, a scholar, or a time wizard, Python is your trusty tool to explore the world of code! ⚔️🧙‍♂️🐍

---

**Happy Coding!** 👩‍💻👨‍💻 - **Kako** ✨
