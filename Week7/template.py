"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammed Affan
Lane  :  AI
Date  :  20/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one raw line and return a dict of its fields."""
    name_part, rest = raw_line.strip().lower().split(",", 1)
    record = {"dataset": name_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
    return record


def status_of(record):
    """Return FLAGGED for a low rating or an under-18 respondent, otherwise OK."""
    if record["rating"] <= 2 or record["age"] < 18:
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT
# Raw, messy lines are kept in raw_records.txt and loaded from there.

raw_records = []
with open("raw_records.txt") as f:
    for line in f:
        raw_records.append(line)


# =============================================================== PROCESS + OUTPUT

flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, status)
    if status == "FLAGGED":
        flagged += 1

print(f"{len(raw_records)} records, {flagged} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] A value that will not convert to a number, e.g. rating=unknown:
#            ValueError: could not convert string to float: 'unknown'
#    [x] Every function does one job, with a docstring:
#            parse_line -> cleans and converts
#            status_of  -> decides