"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammed Affan
Lane  :  AI
Date  :  02/11/2026

Run it:   py template.py
"""

over_limit_count = 0

while True:
    # ================================================================ INPUT
    dataset_name = input("Dataset name (or quit): ")
    if dataset_name == "quit":
        break
    rows_loaded = float(input("Rows loaded : "))
    rows_expected = float(input("Rows expected : "))

    # ============================================================== PROCESS
    rows_missing = rows_expected - rows_loaded
    percent_loaded = (rows_loaded / rows_expected) * 100

    if percent_loaded >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent_loaded >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)
    print(f"  Loaded      : {rows_loaded:>10.2f}")
    print(f"  Expected    : {rows_expected:>10.2f}")
    print(f"  Missing     : {rows_missing:>10.2f}")
    print(f"  Percent     : {percent_loaded:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print(f"Records over limit: {over_limit_count}")