import re
input_file = 'sample.txt'         
output_file = 'emails_found.txt'  

with open(input_file, 'r') as f:
    content = f.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

emails = list(set(emails))

# Save to output file
with open(output_file, 'w') as f:
    for email in emails:
        f.write(email + '\n')

print(f"✅ {len(emails)} email(s) found and saved to '{output_file}' 📁")
