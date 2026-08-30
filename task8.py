emails = [
    "ali@gmail.com", "surayj@gmail.com", "adud@gmail.com",
    "ahmed@gmail.com", "sayyar@gmail.com", "zeeshan@gmail.com",
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
