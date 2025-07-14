from django.shortcuts import render
import mysql.connector as sql

def signaction(request):
    if request.method == "POST":
        # Connect to the database
        db = sql.connect(
            host="localhost",
            user="root",
            port=3307,
            passwd="root",
            database="register",
            charset='utf8mb4',
            collation='utf8mb4_general_ci',
            use_unicode=True
        )
        cursor = db.cursor()

        # Extract POST data
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        sex = request.POST.get("sex", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # Insert into DB using parameterized query
        query = "INSERT INTO users (firstname, lastname, sex, email, password) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, sex, email, password)

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()

    return render(request, 'signup_page.html')