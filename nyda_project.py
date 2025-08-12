from datetime import datetime
import math
import random

# Branding
lot_name = "Parking of Eden"
slogan = "Where your car rests in paradise — for a price."

print(f"=== {lot_name} ===")
print(slogan)
print("\nRates: First 15 sec free | R20/min (up to 6 min) | R300 flat if > 6 min")
print("No overnight parking allowed.\n")

# Record entry time
input("Press ENTER to simulate entering the parking lot...")
entry_time = datetime.now()
print(f"✅ Entry recorded at {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
print("You are now parked...\n")

# Wait for exit
input("Press ENTER when you are ready to leave...")
exit_time = datetime.now()

# Current date/time for receipt
today = exit_time.strftime("%Y-%m-%d")
receipt_time = exit_time.strftime("%H:%M:%S")

# Generate ticket number & cashier ID
ticket_no = f"POE-{random.randint(10000, 99999)}"
cashier_id = f"CASH-{random.randint(1, 20):02d}"

# Calculate duration in minutes
duration_minutes = (exit_time - entry_time).total_seconds() / 60

# Validation (overnight check in minutes)
if duration_minutes > 24 * 60:
    print("\n❌ No overnight parking allowed!")
else:
    # Fee calculation
    if duration_minutes <= (15 / 60):  # 15 seconds grace
        fee = 0
        billable_minutes = 0
    elif duration_minutes > 6:  # More than 6 minutes
        fee = 300
        billable_minutes = math.ceil(duration_minutes)
    else:
        billable_minutes = math.ceil(duration_minutes)
        fee = billable_minutes * 20

    # Receipt formatting
    width = 40
    print("\n" + "*" * width)
    print(lot_name.center(width))
    print(slogan.center(width))
    print("-" * width)
    print(f"Ticket No:  {ticket_no}".ljust(width))
    print(f"Cashier ID: {cashier_id}".ljust(width))
    print(f"Date:       {today}".ljust(width))
    print(f"Time:       {receipt_time}".ljust(width))
    print("-" * width)
    print(f"Entry Time: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}".ljust(width))
    print(f"Exit Time:  {exit_time.strftime('%Y-%m-%d %H:%M:%S')}".ljust(width))
    print(f"Duration:   {duration_minutes:.2f} min".ljust(width))
    print(f"Billed:     {billable_minutes} min".ljust(width))
    print(f"Amount Due: R{fee:.2f}".ljust(width))
    print("-" * width)
    print("Thank you for parking with us!".center(width))
    print("*" * width)
