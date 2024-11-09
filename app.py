from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Dummy user data (replace with real user data from a database)
users = {
    'test@example.com': {'name': 'John Doe', 'username': 'johndoe123', 'email': 'johndoe@example.com'}
}

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))  # Redirect to login if not authenticated

    # Fetch user data based on session user email
    user = users.get(session['user'])
    
    if not user:
        return "User not found.", 404
    
    return render_template('profile.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login code here (for example purposes, just directly set session['user'])
    session['user'] = 'test@example.com'  # Dummy login for testing
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
