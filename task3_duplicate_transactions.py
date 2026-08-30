transaction_ids = [
    "TXN1001", "TXN1002", "TXN1003", "TXN1001",
    "TXN1004", "TXN1002", "TXN1005", "TXN1005", "TXN1005",
]


def find_duplicates(ids_list):
    seen = set()
    duplicates = set()
    for txn_id in ids_list:
        if txn_id in seen:
            duplicates.add(txn_id)
        else:
            seen.add(txn_id)
    return duplicates


def get_unique_transactions(ids_list):
    return set(ids_list)


print("Original transaction count:", len(transaction_ids))

duplicates = find_duplicates(transaction_ids)
print("Duplicate transaction IDs:", duplicates)

unique_transactions = get_unique_transactions(transaction_ids)
print("Unique transactions:", unique_transactions)
print("Unique transaction count:", len(unique_transactions))
