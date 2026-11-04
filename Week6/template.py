"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammed Affan
Lane  :  AI
Date  :  04/11/2026

Run it:   py template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("datasets.csv")


# ================================================================= PROCESS
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
print("ALL RECORDS")
print(df)

print()
print("NOT OK")
print(df[df["status"] != "OK"])

print()
print("COUNT PER STATUS")
print(df.groupby("status").size())

df.to_csv("datasets_report.csv", index=False)

df["status"].value_counts().plot(kind="bar", title="Records by status")
plt.tight_layout()
plt.savefig("status_counts.png")