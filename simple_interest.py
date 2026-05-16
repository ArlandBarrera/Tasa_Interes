from datetime import date

YEAR_LENGTH = 360
CHAR_LENGTH = 50

OPTION_PERIODS = {
    "1": "daily",
    "2": "weekly",
    "3": "semimonthly",
    "4": "monthly",
    "5": "bimonthly",
    "6": "quarterly",
    "7": "fourmonth",
    "8": "semiannual",
    "9": "annual",
}

PERIODS = {
    "daily": YEAR_LENGTH,
    "weekly": 52,
    "semimonthly": 24,
    "monthly": 12,
    "bimonthly": 6,
    "quarterly": 4,
    "fourmonth": 3,
    "semiannual": 2,
    "annual": 1,
}


def calculate_interest(
    principal: float,
    rate: float,
    rate_period: str,
    start_date: date,
    end_date: date,
):
    annual_rate = rate * PERIODS[rate_period]

    daily_rate = annual_rate / YEAR_LENGTH

    elapsed_days = (end_date - start_date).days

    interest = principal * daily_rate * elapsed_days

    total = principal + interest

    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "daily_rate": daily_rate,
        "elapsed_days": elapsed_days,
        "interest": round(interest, 2),
        "total": round(total, 2),
    }


def get_valid_float(prompt: str) -> float:
    while True:
        value = input(prompt)
        try:
            num = float(value)
            if num > 0:
                return num
            print("Error: Value must be positive.")
        except ValueError:
            print("Error: Please enter a numeric value.")


def get_valid_date(prompt: str) -> date:
    while True:
        value = input(prompt)
        try:
            return date.fromisoformat(value)
        except ValueError:
            print("Error: Invalid date. Use YYYY-MM-DD format.")


def get_period_choice() -> str:
    print("\nAvailable periods:")
    for key, val in OPTION_PERIODS.items():
        print(f"{key} - {val}")
    while True:
        choice = input("Enter number: ").strip().lower()
        if choice in OPTION_PERIODS.keys():
            return OPTION_PERIODS.get(choice)
        print("Error: Invalid period.")


def display_results(result: dict, rate_period: str, rate: float, start_date: date, end_date: date):
    print()
    print("=" * CHAR_LENGTH)
    print("SUMMARY")
    print("=" * CHAR_LENGTH)
    print(f"Principal:        ${result['principal']:,.2f}")
    print("-" * CHAR_LENGTH)
    print(f"Interest Rate:    {rate}% ({rate_period})")
    print("-" * CHAR_LENGTH)
    print(f"Annual Rate:      {result['annual_rate']:.4f}")
    print(f"Daily Rate:       {result['daily_rate']:.4f}")
    print("-" * CHAR_LENGTH)
    print(f"Start Date:       {start_date}")
    print(f"End Date:         {end_date}")
    print(f"Elapsed Days:     {result['elapsed_days']}")
    print("-" * CHAR_LENGTH)
    print(f"Interest:         ${result['interest']:,.2f}")
    print(f"Total:            ${result['total']:,.2f}")
    print("-" * CHAR_LENGTH)


if __name__ == "__main__":
    print("=" * CHAR_LENGTH)
    print("Simple Interest Calculator - ACT/360")
    print("=" * CHAR_LENGTH)

    principal = get_valid_float("Principal amount: ")
    rate_percentage = get_valid_float("Interest rate (%): ")
    rate = rate_percentage / 100
    rate_period = get_period_choice()
    start_date = get_valid_date("Start date (YYYY-MM-DD): ")
    end_date = get_valid_date("End date (YYYY-MM-DD): ")

    if end_date <= start_date:
        print("Error: End date must be after start date.")
    else:
        result = calculate_interest(principal, rate, rate_period, start_date, end_date)
        display_results(result, rate_period, rate_percentage, start_date, end_date)
