def clean_email_list(emails):
    # Write your code below
    cleaned = list(map(lambda x: x.lower().strip(), emails))
       
    valid_emails = list(filter(lambda x: x.count("@") == 1 and x.index("@") > 0 and  x.index("@") < len(x)-1, cleaned))
    return list(valid_emails)