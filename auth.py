from flask import Blueprint, render_template, request, redirect, session, flash
import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Username and password are required.', 'error')
            return render_template('register.html')

        if username.lower() == 'admin':
            flash('You cannot register as admin.', 'error')
            return render_template('register.html')

        conn = db.get_connection()
        try:
            conn.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, 'user')",
                (username, password)
            )
            conn.commit()
            flash('Registered successfully.', 'success')
            return redirect('/login')
        except Exception as e:
            if 'UNIQUE constraint failed: users.username' in str(e):
                flash('Username already exists.', 'error')
            else:
                flash(f'Registration error: {e}', 'error')
        finally:
            conn.close()

    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        conn = db.get_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session['user'] = user['id']
            session['role'] = user['role']
            return redirect('/')
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
