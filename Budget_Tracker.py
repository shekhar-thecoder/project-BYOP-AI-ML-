from datetime import datetime

# -------------------------------
# DATA STORAGE (LISTS)
# -------------------------------
transactions = []
investments = []

# -------------------------------
# WANTS vs NEEDS CLASSIFIER
# -------------------------------
def classify_want_need(category, description=""):
    
    needs_keywords = [
        "food", "rent", "electricity", "water", "medicine",
        "groceries", "transport", "fees", "education", "bill"
    ]
    
    wants_keywords = [
        "shopping", "movie", "netflix", "gaming",
        "party", "travel", "zomato", "swiggy", "luxury"
    ]
    
    text = (category + " " + description).lower()
    
    for word in needs_keywords:
        if word in text:
            return "NEED"
    
    for word in wants_keywords:
        if word in text:
            return "WANT"
    
    return "UNCATEGORIZED"

# -------------------------------
# ADD TRANSACTION
# -------------------------------
def add_transaction():
    try:
        amount = float(input("Enter amount: Rs "))
        category = input("Enter category: ")
        description = input("Enter description (optional): ")
        t_type = input("Type (Income/Expense): ").capitalize()
        
        tag = classify_want_need(category, description)
        date = datetime.now().strftime("%Y-%m-%d")
        
        transaction = {
            "Date": date,
            "Type": t_type,
            "Amount": amount,
            "Category": category,
            "Description": description,
            "Tag": tag
        }
        
        transactions.append(transaction)
        
        print("Transaction added successfully [" + tag + "]")
    
    except:
        print("Invalid input")

# -------------------------------
# ADD INVESTMENT
# -------------------------------
def add_investment():
    try:
        asset = input("Asset name: ")
        invested = float(input("Invested amount: Rs "))
        current = float(input("Current value: Rs "))
        
        date = datetime.now().strftime("%Y-%m-%d")
        
        investment = {
            "Date": date,
            "Asset": asset,
            "Invested": invested,
            "Current_Value": current
        }
        
        investments.append(investment)
        
        print("Investment added")
    
    except:
        print("Invalid input")

# -------------------------------
# FINANCIAL SUMMARY
# -------------------------------
def show_summary():
    income = 0
    expense = 0
    
    for t in transactions:
        if t["Type"] == "Income":
            income += t["Amount"]
        elif t["Type"] == "Expense":
            expense += t["Amount"]
    
    balance = income - expense
    
    total_invested = sum(i["Invested"] for i in investments)
    current_value = sum(i["Current_Value"] for i in investments)
    profit = current_value - total_invested
    
    net_worth = balance + current_value

    print("\n------ FINANCIAL SUMMARY ------")
    print("Total Income      : Rs", income)
    print("Total Expenses    : Rs", expense)
    print("Balance           : Rs", balance)
    print("Investment P/L    : Rs", profit)
    print("Net Worth         : Rs", net_worth)

# -------------------------------
# WANTS vs NEEDS ANALYSIS
# -------------------------------
def show_wants_vs_needs():
    needs = 0
    wants = 0
    
    for t in transactions:
        if t["Tag"] == "NEED":
            needs += t["Amount"]
        elif t["Tag"] == "WANT":
            wants += t["Amount"]
    
    print("\n------ WANTS vs NEEDS ------")
    print("Needs Spending : Rs", needs)
    print("Wants Spending : Rs", wants)
    
    total = needs + wants
    if total > 0:
        print("Needs % :", round((needs/total)*100, 2))
        print("Wants % :", round((wants/total)*100, 2))

# -------------------------------
# SIMPLE TEXT VISUALIZATION
# -------------------------------
def show_bar_chart():
    needs = 0
    wants = 0
    
    for t in transactions:
        if t["Tag"] == "NEED":
            needs += t["Amount"]
        elif t["Tag"] == "WANT":
            wants += t["Amount"]
    
    print("\n------ SIMPLE BAR GRAPH ------")
    print("Needs :", "*" * int(needs / 10))
    print("Wants :", "*" * int(wants / 10))

# -------------------------------
# SIMPLE PREDICTION (NO ML LIB)
# -------------------------------
def predict_expense():
    expenses = [t["Amount"] for t in transactions if t["Type"] == "Expense"]
    
    if len(expenses) < 2:
        print("Not enough data for prediction")
        return
    
    avg = sum(expenses) / len(expenses)
    print("Predicted next expense (based on average): Rs", round(avg, 2))

def predict_investment():
    if len(investments) < 2:
        print("Not enough data")
        return
    
    growth_rates = []
    
    for i in investments:
        if i["Invested"] > 0:
            growth = (i["Current_Value"] - i["Invested"]) / i["Invested"]
            growth_rates.append(growth)
    
    if len(growth_rates) == 0:
        print("No valid data")
        return
    
    avg_growth = sum(growth_rates) / len(growth_rates)
    total_current = sum(i["Current_Value"] for i in investments)
    
    predicted = total_current * (1 + avg_growth)
    
    print("Predicted portfolio value (next period): Rs", round(predicted, 2))

# -------------------------------
# MAIN MENU
# -------------------------------
while True:
    print("\n------ PERSONAL FINANCE TRACKER ------")
    print("1. Add Income/Expense")
    print("2. Add Investment")
    print("3. Financial Summary")
    print("4. Wants vs Needs Analysis")
    print("5. Simple Graph")
    print("6. Predict Expense")
    print("7. Predict Investment Growth")
    print("8. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        add_transaction()
    elif choice == "2":
        add_investment()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        show_wants_vs_needs()
    elif choice == "5":
        show_bar_chart()
    elif choice == "6":
        predict_expense()
    elif choice == "7":
        predict_investment()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice")