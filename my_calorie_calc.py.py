# from calories import Calculator

# def calorie_counter():
# calc = Calculator(age='', weight='', height='', gender='', activity='')
# print(calc.bmr()) 
# print(calc.tdee())

import tkinter as tk
from tkinter import ttk, messagebox
from my_calorie_calc import Calculator

def calculate():
    try:
        # Get values
        age = int(age_var.get())
        weight = float(weight_var.get())
        height = float(height_var.get())
        gender = gender_var.get()
        activity = activity_var.get()
        goal = goal_var.get()

        # Init Calculator
        calc = Calculator(age=age, weight=weight, height=height, gender=gender, activity=activity)

        bmr = calc.bmr()
        tdee = calc.tdee()

        # Adjust based on goal
        if goal == "cut":
            adjusted = tdee - 500
        elif goal == "bulk":
            adjusted = tdee + 500
        else:
            adjusted = tdee

        # Output
        messagebox.showinfo("Calorie Breakdown", 
            f"BMR: {bmr:.2f} kcal/day\n"
            f"TDEE: {tdee:.2f} kcal/day\n"
            f"Calories to {goal}: {adjusted:.2f} kcal/day")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for age, weight, and height.")

# GUI Setup
root = tk.Tk()
root.title("Calorie Counter 🧠🔥")

# Vars
age_var = tk.StringVar()
weight_var = tk.StringVar()
height_var = tk.StringVar()
gender_var = tk.StringVar(value="male")
activity_var = tk.StringVar(value="moderate")
goal_var = tk.StringVar(value="maintain")

# Layout
ttk.Label(root, text="Age (years):").grid(row=0, column=0, sticky="w")
ttk.Entry(root, textvariable=age_var).grid(row=0, column=1)

ttk.Label(root, text="Weight (kg):").grid(row=1, column=0, sticky="w")
ttk.Entry(root, textvariable=weight_var).grid(row=1, column=1)

ttk.Label(root, text="Height (cm):").grid(row=2, column=0, sticky="w")
ttk.Entry(root, textvariable=height_var).grid(row=2, column=1)

ttk.Label(root, text="Gender:").grid(row=3, column=0, sticky="w")
ttk.Combobox(root, textvariable=gender_var, values=["male", "female"], state="readonly").grid(row=3, column=1)

ttk.Label(root, text="Activity Level:").grid(row=4, column=0, sticky="w")
ttk.Combobox(root, textvariable=activity_var, values=["sedentary", "light", "moderate", "active", "very active"], state="readonly").grid(row=4, column=1)

ttk.Label(root, text="Goal:").grid(row=5, column=0, sticky="w")
ttk.Combobox(root, textvariable=goal_var, values=["cut", "maintain", "bulk"], state="readonly").grid(row=5, column=1)

ttk.Button(root, text="Calculate", command=calculate).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()