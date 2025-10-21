# compliance_check.py
keywords = ["PII", "GDPR", "HIPAA", "password"]
violations = []

for file in ["app.py"]:
    with open(file) as f:
        content = f.read()
        for word in keywords:
            if word.lower() in content.lower():
                violations.append(f"{word} found in {file}")

if violations:
    print("Compliance Violations Found!")
    for v in violations:
        print(v)
    exit(1)
else:
    print("No compliance violations found!")
