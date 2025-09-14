def currency_converter(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Please enter a valid currency"

    converted_money = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
    return converted_money


# Exchange rate dictionary
exchange_rates = {
    "USD": 1.0,      # United States Dollar
    "INR": 82.74,    # Indian Rupee
    "EUR": 0.92,     # Euro
    "JPY": 146.28,   # Japanese Yen
    "GBP": 0.78,     # British Pound
    "RUB": 96.15,    # Russian Ruble
    "CHF": 0.08,     # Swiss Franc
    "CNY": 7.28,     # Chinese Yuan
    "SAR": 3.75,     # Saudi Arabian Riyal
    "AED": 3.67      # Emirati Dirham
}

# Taking inputs
amount = float(input("Enter the amount: "))
from_currency = input("Enter from currency (eg. 'USD'): ").upper()
to_currency = input("Enter to currency (eg. 'INR'): ").upper()

# Convert money
converted_money = currency_converter(amount, from_currency, to_currency, exchange_rates)

# Print result
if isinstance(converted_money, str):
    print(converted_money)  # error message
else:
    print(f"{amount:.2f} {from_currency} is equivalent to {converted_money:.2f} {to_currency}")
