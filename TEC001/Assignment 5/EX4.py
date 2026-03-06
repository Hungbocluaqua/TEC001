import re
def redact_phone(text):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    return re.sub(pattern, "[REDACTED]", text)