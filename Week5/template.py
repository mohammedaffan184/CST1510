"""
RECORD CHECK  -  my version
===========================

Name  :  Your Name
Lane  :  AI
Date  :  Week 5

Run it:  py template.py
"""

# ====================================================================== CLASS
class Record:
    def __init__(self, label, value, limit):
        """Store the label, value and limit on this record."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK for this record."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("datasets.txt")


# ==================================================================== OUTPUT
over_limit_count = 0

for record in records:
    status = record.status()
    percent = (record.value / record.limit) * 100

    if status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Loaded      : {record.value:>10.2f}")
    print(f"  Expected    : {record.limit:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")

    print("=" * 34)

print()
print(f"{over_limit_count} of {len(records)} records are OVER LIMIT")