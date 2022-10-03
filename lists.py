from flask import Blueprint, render_template

lists_bp = Blueprint('lists', __name__)

@lists_bp.route('/')
def home_page():
    return render_template('home.html')