from collections import Counter

log_entries = [
    "INFO", "ERROR", "WARNING", "INFO", "ERROR", "INFO",
    "INFO", "WARNING", "ERROR", "INFO", "ERROR", "ERROR",
]


def analyze_logs(logs):
    counts = Counter(logs)
    log_types = list(counts.keys())
    most_common_type, most_common_count = counts.most_common(1)[0]
    return counts, log_types, (most_common_type, most_common_count)


counts, log_types, most_common = analyze_logs(log_entries)

print("Count per log type:")
for log_type, count in counts.items():
    print(f"  {log_type}: {count}")

print("\nLog types that appeared:", log_types)
print(f"Most frequent log type: {most_common[0]} ({most_common[1]} times)")
