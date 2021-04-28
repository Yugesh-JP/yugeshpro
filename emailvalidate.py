from email_validator import validate_email, EmailNotValidError
import csv

#email = "yugesh.ragavan@yugest.com"

with open('email.csv', 'r') as file:
  reader = csv.reader(file)
  next(reader)
  for col in reader:
    print(col[0])
    email = col[0]
    with open('output.csv', 'a+', newline="", encoding='utf-8') as wf:
      writer = csv.DictWriter(wf, fieldnames=['email', 'comments'])
      try:
        # Validate.
        valid = validate_email(email)

        # Update with the normalized form.
        email = valid.email
        print(f"{email} is valid")
        writer.writerow({'email': email,
                         'comments':'valid'})

      except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        writer.writerow({'email': email,
                         'comments': str(e)})
