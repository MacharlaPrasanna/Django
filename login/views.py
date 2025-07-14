from django.shortcuts import render
import mysql.connector as sql

def loginaction(request):
    if request.method == "POST":
        # Get form values safely
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # Connect to the MySQL database
        db = sql.connect(
            host="localhost",
            port=3307,
            user="root",
            passwd="root",
            database="register",
            charset='utf8mb4',
            collation='utf8mb4_general_ci',
            use_unicode=True
        )
        cursor = db.cursor()

        # Use parameterized query to prevent SQL injection
        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        cursor.close()
        db.close()

        # Check if login is valid
        if result:
            return render(request, 'welcome.html')
        else:
            return render(request, 'error.html')

    return render(request, 'login_page.html')