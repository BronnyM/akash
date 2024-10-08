# Python Basics Practice
# Focus: Variables, Operations, Printing, and If Statements

# PART 1: VARIABLES AND PRINTING
# Example 1: Basic variables and printing
country = "United States"
gdp = 21_400_000_000_000  # $21.4 trillion
population = 331000000
unemployment_rate = 3.7

# Simple printing
print("Country:", country)
print("GDP:", gdp)
print("Population:", population)
print("Unemployment Rate:", unemployment_rate)

# Formatted printing
print(f"{country} has a GDP of ${gdp/1000000000000} trillion")
print(f"The unemployment rate is {unemployment_rate}%")

# Practice 1: Create your own variables and print them
# TODO: Create variables for another country's economic data
# Example structure:
# country_name = "China"
# country_gdp = ...
# country_population = ...


# PART 2: BASIC OPERATIONS
# Example 2: Mathematical operations
gdp_per_capita = gdp / population
total_unemployed = (unemployment_rate / 100) * population

print(f"GDP per capita: ${gdp_per_capita:.2f}")
print(f"Estimated unemployed people: {total_unemployed:.0f}")

# Percentage change
old_gdp = 19000000000000
gdp_growth = ((gdp - old_gdp) / old_gdp) * 100

print(f"GDP growth: {gdp_growth:.1f}%")

# Practice 2: Perform your own calculations
# TODO: Calculate percentage changes, per capita values, or totals
# Hint: Try calculating:
# 1. Percentage of population employed
# 2. Year-over-year growth rates
# 3. Share of global GDP


# PART 3: IF STATEMENTS
# Example 3: Basic if statements
recession_threshold = -0.5

if gdp_growth < recession_threshold:
    print("The economy is in recession")
elif gdp_growth < 1.0:
    print("The economy is growing slowly")
else:
    print("The economy is growing at a normal or fast rate")

# Nested if statements
high_unemployment = 5.0
if unemployment_rate >= high_unemployment:
    print("High unemployment")
    if gdp_growth < 1.0:
        print("Stagflation risk!")
else:
    print("Normal or low unemployment")

# Practice 3: Write your own if statements
# TODO: Create conditions for:
# 1. Determining if a country is "developed" based on GDP per capita
# 2. Classifying inflation rates
# 3. Determining trade surplus/deficit


# PART 4: COMBINING CONCEPTS
# Example 4: A simple economic analyzer

def analyze_economy(gdp_growth, unemployment, inflation):
    print(f"\nEconomic Analysis:")
    print(f"GDP Growth: {gdp_growth}%")
    print(f"Unemployment: {unemployment}%")
    print(f"Inflation: {inflation}%")
    
    # Analyzing GDP Growth
    if gdp_growth < 0:
        print("WARNING: Economy is shrinking!")
    elif gdp_growth < 2:
        print("Slow growth")
    elif gdp_growth < 4:
        print("Moderate growth")
    else:
        print("High growth")
    
    # Analyzing unemployment
    if unemployment > 5:
        print("High unemployment")
    elif unemployment < 3:
        print("Very low unemployment - might cause wage inflation")
    
    # Analyzing inflation
    if inflation > 3:
        print("High inflation")
    elif inflation < 1:
        print("Low inflation - deflation risk")
    
    # Combined analysis
    if gdp_growth > 3 and unemployment < 4:
        print("Economy might be overheating")
    if inflation > 4 and unemployment > 6:
        print("Stagflation warning!")

    return gdp_growth, unemployment, inflation

# Using the analyzer
outputs = analyze_economy(2.5, 3.7, 2.1)

# Practice 4: Create your own economic analysis function
# TODO: Write a function that takes different economic indicators
# and provides an analysis. Consider using:
# 1. Trade balance
# 2. Government debt as % of GDP
# 3. Consumer confidence index

# PRACTICE EXERCISES

# 1. Variable Practice
# Create variables for:
# - Monthly revenue
# - Monthly expenses
# - Number of employees
# Calculate and print:
# - Monthly profit
# - Revenue per employee
# - Profit margin as a percentage

# 2. If Statement Practice
# Write a program that:
# - Determines tax brackets based on income
# - Classifies a company as small, medium, or large based on employees
# - Determines if a student loan should be approved based on income and credit score

# 3. Combined Practice
def business_analyzer():
    # TODO: Write a function that:
    # 1. Takes revenue, expenses, and number of employees as input
    # 2. Calculates key metrics
    # 3. Prints analysis and recommendations based on the metrics
    pass

# BONUS CHALLENGE
def economic_game():
    """
    Create a simple game where the player makes economic decisions.
    Use variables to track economic indicators and if statements to
    determine outcomes.
    """
    # TODO: Implement the game
    pass

# Example solution for Variable Practice
monthly_revenue = 100000
monthly_expenses = 75000
num_employees = 10

monthly_profit = monthly_revenue - monthly_expenses
revenue_per_employee = monthly_revenue / num_employees
profit_margin = (monthly_profit / monthly_revenue) * 100

print(f"\nBusiness Metrics:")
print(f"Monthly Profit: ${monthly_profit}")
print(f"Revenue per Employee: ${revenue_per_employee:.2f}")
print(f"Profit Margin: {profit_margin:.1f}%")