"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammed Affan
Lane  :  AI
Date  :  02/11/2026

Run it:   python template.py
"""

# ==================================================================== INPUT
dataset_name = input("Dataset name : ")
rows_loaded = float(input("Rows loaded : "))
rows_expected = float(input("Rows expected : "))


# ================================================================== PROCESS
difference = rows_loaded - rows_expected
percent_loaded = (rows_loaded / rows_expected) * 100

# Excellent: share of the data that is missing. In data science this tells you
# at a glance whether the dataset is complete enough to trust.
percent_missing = 100 - percent_loaded


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)

print(f"  Loaded      : {rows_loaded:>10.2f}")
print(f"  Expected    : {rows_expected:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent_loaded:>10.2f} %")
print(f"  Missing     : {percent_missing:>10.2f} %")

print("=" * 34)