"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammed Affan
Lane  :  AI
Date  :  03/11/2026

Run it:   python template.py

Reads servers from servers.txt (hostname,GB used,GB total), checks each one,
prints a report, and writes label,status for every record to results.txt.
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return difference, percent and status for one record."""
    if limit <= 0:
        return 0.0, 100.0, "OVER LIMIT"
        
    difference = limit - value
    percent = (value / limit) * 100
    
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
        
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one formatted report block for one record."""
    print(f"{label}")
    print(f"  used     : {value:>8.1f} GB")
    print(f"  total    : {limit:>8.1f} GB")
    print(f"  free     : {difference:>8.1f} GB")
    print(f"  percent  : {percent:>8.1f} %")
    print(f"  status   : {status}")
    print("-" * 30)


def print_summary(over_count, total):
    """Print the final 'N of M were over limit' line."""
    print(f"{over_count} of {total} were over limit")


# ====================================================================== STORE

def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:  # skip blank lines
                continue
            
            # Clean spaces around commas and validate structure
            parts = [item.strip() for item in line.split(",")]
            if len(parts) == 3:
                label, value, limit = parts
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
    return records


def write_results(path, results):
    """Write one 'label,status' line per result to a file."""
    with open(path, "w", encoding="utf-8") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


# =============================================================== PROCESS + OUTPUT

def main():
    try:
        records = load_records("servers.txt")
    except FileNotFoundError:
        print("servers.txt not found - starting with no records")
        records = []

    over_count = 0
    results = []

    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"],
                     difference, percent, status)
        results.append((record["label"], status))
        if status == "OVER LIMIT":
            over_count += 1

    print_summary(over_count, len(records))
    write_results("results.txt", results)


if __name__ == "__main__":
    main()


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers are correct by hand
#        srv-01: 87/120 = 72.5%  -> OK
#        srv-02: 45/120 = 37.5%  -> OK
#        srv-03: 120/120 = 100%  -> OVER LIMIT
#        srv-04: 115/120 = 95.8% -> WARNING
#        srv-05: 60/200 = 30%    -> OK
#    [x] Missing file: rename servers.txt and run - the try/except catches it
#        (Threshold/Typical version would crash with FileNotFoundError)
#    [x] Every function does one job