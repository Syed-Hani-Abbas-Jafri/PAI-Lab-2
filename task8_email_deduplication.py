emails = [
    "ali@gmail.com", "sara@yahoo.com", "ali@gmail.com",
    "ahmed@gmail.com", "sara@yahoo.com", "zain@hotmail.com",
]


def unique_emails_set(email_list):
    return set(email_list)


def unique_emails_ordered(email_list):
    return list(dict.fromkeys(email_list))


print("Original emails (with duplicates):", emails)

print("\nUsing set() - unique but unordered:")
print(" ", unique_emails_set(emails))

print("\nUsing dict.fromkeys() - unique AND preserves original order:")
print(" ", unique_emails_ordered(emails))
