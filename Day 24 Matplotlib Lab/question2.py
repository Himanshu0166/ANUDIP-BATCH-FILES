import matplotlib.pyplot as plt

# Given data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create pie chart
plt.figure(figsize=(7, 7))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'orange', 'green', 'red', 'purple'])
plt.title(" Distribution of Monthly Income by Source")
plt.show()
