"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammed Affan
Lane  :  AI
Date  :  02/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return "OVER LIMIT", "WARNING" or "OK" for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of the expected rows loaded."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered report. Nothing is worked out here, only shown."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Loaded      : {value:>10.2f}")
    print(f"  Expected    : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Percent     : {percent:>8.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()


# ============================================================ INPUT / PROCESS / OUTPUT
# Type "quit" as the dataset name to stop.

over_count = 0

while True:
    # --- 2. INPUT
    label = input("Dataset name (or 'quit') : ")
    if label == "quit":
        break
    value = float(input("Rows loaded             : "))
    limit = float(input("Rows expected           : "))

    # --- 3. PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_count += 1

    # --- 4. OUTPUT
    print_report(label, value, limit, difference, percent, status)

print(f"Records over limit: {over_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and note the error:
#            ZeroDivisionError: float division by zero
#    [x] Every function does one job:
#            status_of    -> decides
#            check        -> calculates
#            print_report -> shows