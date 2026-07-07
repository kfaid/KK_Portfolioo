import os
import re
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

# Basic server-side email validation regex
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

@app.route('/')
def index():
    """Renders the portfolio home page."""
    # We can pass dynamic content to the template if needed
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handles contact form submissions via AJAX."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No data received."}), 400

        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        subject = data.get("subject", "").strip()
        message = data.get("message", "").strip()

        # Input Validation
        if not name or not email or not subject or not message:
            return jsonify({"status": "error", "message": "All fields are required."}), 400

        if len(name) < 2:
            return jsonify({"status": "error", "message": "Name must be at least 2 characters long."}), 400

        if not EMAIL_REGEX.match(email):
            return jsonify({"status": "error", "message": "Please enter a valid email address."}), 400

        if len(message) < 10:
            return jsonify({"status": "error", "message": "Message must be at least 10 characters long."}), 400

        # Production log of the contact submission
        app.logger.info(f"New Contact Form Submission:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        # In a real environment, you might integrate with SendGrid, Mailgun, or save to a DB.
        # Since this is a portfolio on Vercel (serverless), we return a successful response immediately.
        return jsonify({
            "status": "success",
            "message": "Your message has been sent successfully! Krushil will get in touch with you soon."
        }), 200

    except Exception as e:
        app.logger.error(f"Error handling contact submission: {str(e)}")
        return jsonify({"status": "error", "message": "An internal server error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Local development server running on port 5001 to avoid conflicts
    app.run(host='0.0.0.0', port=5001, debug=True)
