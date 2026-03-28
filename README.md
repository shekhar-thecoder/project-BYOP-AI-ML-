# project-BYOP-AI-ML-
# AI/ML Project

## Personal Finance and Investment Tracker

---

## Student Details

**Name:** Shekhar Tomar
**Registration Number:** 25BAI11013
**Course Code:** CSA2001

---

## About the Project

This project is a simple yet practical **Personal Finance and Investment Tracker** built using Python. The main idea behind this project was to create something that can actually be useful in day-to-day life while also applying basic concepts of programming and logic.

Instead of using heavy libraries or complex frameworks, the entire project is built using **core Python**, which makes it lightweight and easy to run on any system. The program helps in tracking income, expenses, and investments, and also gives insights into spending habits.

One of the key features of this project is the classification of expenses into **“Wants” and “Needs”**, which helps in understanding where money is actually going.

---

## Why This Project?

While working on this project, the goal was not just to complete an assignment, but to build something meaningful. Many people (especially students) don’t keep track of their finances properly.

This project helps in:

* Understanding spending patterns
* Managing money more effectively
* Differentiating between essential and non-essential expenses
* Getting a basic idea of financial health

---

## Features

* Add income and expense entries
* Track different categories of spending
* Manage investments (invested amount and current value)
* Automatic classification:

  * NEED (essential spending)
  * WANT (non-essential spending)
* Financial summary:

  * Total income
  * Total expenses
  * Balance
  * Net worth
* Wants vs Needs analysis
* Simple text-based visualization
* Basic prediction:

  * Future expenses (based on average)
  * Investment growth (based on growth rate)

---

## How It Works

The program runs in a **menu-driven format**.

When you run the file, you’ll see options like:

1. Add Income/Expense
2. Add Investment
3. View Financial Summary
4. Wants vs Needs Analysis
5. Simple Graph
6. Predict Expense
7. Predict Investment Growth
8. Exit

You just enter the option number and follow the instructions.

---

## Project Structure

This project is kept simple and organized:

* **Transactions** → Stored as a list of dictionaries
* **Investments** → Stored separately
* **Functions** → Used for each feature like:

  * Adding data
  * Calculating summary
  * Classification
  * Prediction

Everything is handled in a single Python file to keep it easy to understand.

---

## Logic Used

### Wants vs Needs Classification

The program uses a simple keyword-based approach.

For example:

* “food”, “rent”, “fees” → NEED
* “shopping”, “movie”, “zomato” → WANT

If nothing matches, it is marked as **UNCATEGORIZED**.

---

### Financial Calculations

* **Balance = Income – Expenses**
* **Profit/Loss = Current Value – Invested Amount**
* **Net Worth = Balance + Investment Value**

---

### Prediction Logic

Instead of using complex ML models, simple logic is used:

* Expense prediction → average of past expenses
* Investment prediction → average growth rate

This keeps the system simple and understandable.

---

## Technologies Used

* Python (Core)
* Built-in libraries only:

  * datetime

No external libraries like pandas, numpy, or sklearn are used.

---

## Advantages

* Works on any system (no setup required)
* Easy to understand and modify
* Useful for beginners
* Practical real-life application
* Clean and simple logic

---

## Limitations

* No graphical interface (CLI-based)
* Data is not saved permanently
* Predictions are basic
* Not suitable for large-scale use

---

## Future Improvements

If this project is extended further, the following can be added:

* File storage (CSV or database)
* GUI using Tkinter or web app
* Integration with real stock market data
* Advanced machine learning models
* Smart suggestions and alerts

---

## Conclusion

This project shows how basic Python can be used to build something practical and useful. It not only helps in understanding programming concepts but also gives insight into personal financial management.

Overall, it is a simple but meaningful project that can be further expanded into a full-scale application.

---

## How to Run

1. Install Python (if not already installed)
2. Copy the code into a `.py` file
3. Run using:

```
python filename.py
```

("ye readme material haii!!)
## Final Note

This project was built with the intention of keeping things simple, clear, and useful. It focuses more on logic and understanding rather than complexity.

---
