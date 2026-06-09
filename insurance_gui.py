import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("insurance_model.pkl", "rb"))

# Prediction Function
def predict_insurance():
    try:
        age = int(entry_age.get())
        bmi = float(entry_bmi.get())
        children = int(entry_children.get())

        gender = gender_var.get()
        smoker = smoker_var.get()
        region = region_var.get()

        # Convert categorical values
        sex_male = 1 if gender == "Male" else 0
        smoker_yes = 1 if smoker == "Yes" else 0

        region_northwest = 1 if region == "Northwest" else 0
        region_southeast = 1 if region == "Southeast" else 0
        region_southwest = 1 if region == "Southwest" else 0

        # Create DataFrame
        new_data = pd.DataFrame({
            "age": [age],
            "bmi": [bmi],
            "children": [children],
            "sex_male": [sex_male],
            "smoker_yes": [smoker_yes],
            "region_northwest": [region_northwest],
            "region_southeast": [region_southeast],
            "region_southwest": [region_southwest]
        })

        prediction = model.predict(new_data)

        result_label.config(
            text=f"Predicted Insurance Cost: ₹{prediction[0]:,.2f}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = tk.Tk()
root.title("Medical Insurance Cost Prediction")
root.geometry("600x700")
root.configure(bg="#f5f5f5")

# Title
title = tk.Label(
    root,
    text="🏥 Medical Insurance Cost Prediction",
    font=("Arial", 20, "bold"),
    bg="#f5f5f5",
    fg="darkblue"
)
title.pack(pady=20)

# Frame
frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both")

# Age
tk.Label(frame, text="Age", bg="white",
         font=("Arial", 12)).pack(pady=5)

entry_age = tk.Entry(frame, font=("Arial", 12))
entry_age.pack(pady=5)

# BMI
tk.Label(frame, text="BMI", bg="white",
         font=("Arial", 12)).pack(pady=5)

entry_bmi = tk.Entry(frame, font=("Arial", 12))
entry_bmi.pack(pady=5)

# Children
tk.Label(frame, text="Children", bg="white",
         font=("Arial", 12)).pack(pady=5)

entry_children = tk.Entry(frame, font=("Arial", 12))
entry_children.pack(pady=5)

# Gender Dropdown
tk.Label(frame, text="Gender", bg="white",
         font=("Arial", 12)).pack(pady=5)

gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(
    frame,
    textvariable=gender_var,
    values=["Male", "Female"],
    state="readonly"
)
gender_dropdown.pack(pady=5)
gender_dropdown.current(0)

# Smoker Dropdown
tk.Label(frame, text="Smoker", bg="white",
         font=("Arial", 12)).pack(pady=5)

smoker_var = tk.StringVar()
smoker_dropdown = ttk.Combobox(
    frame,
    textvariable=smoker_var,
    values=["Yes", "No"],
    state="readonly"
)
smoker_dropdown.pack(pady=5)
smoker_dropdown.current(1)

# Region Dropdown
tk.Label(frame, text="Region", bg="white",
         font=("Arial", 12)).pack(pady=5)

region_var = tk.StringVar()
region_dropdown = ttk.Combobox(
    frame,
    textvariable=region_var,
    values=[
        "Northeast",
        "Northwest",
        "Southeast",
        "Southwest"
    ],
    state="readonly"
)
region_dropdown.pack(pady=5)
region_dropdown.current(0)

# Predict Button
predict_btn = tk.Button(
    root,
    text="Predict Insurance Cost",
    command=predict_insurance,
    bg="green",
    fg="white",
    font=("Arial", 14, "bold"),
    width=22
)
predict_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#f5f5f5",
    fg="red"
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Developed by Santhosh kumar E",
    font=("Arial", 10),
    bg="#f5f5f5"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
