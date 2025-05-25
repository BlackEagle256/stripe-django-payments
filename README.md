# 💳 Django Stripe Checkout Integration

A simple and clean Django application that demonstrates how to integrate **Stripe Checkout** for accepting online payments. Ideal for testing, learning, or building the foundation of a real payment system.

---

## 🚀 Features

- ✅ Stripe Checkout integration with Django
- ✅ Minimal HTML-based UI for payment flow
- ✅ Success and cancel pages after payment
- ✅ Clean project structure (modular and scalable)

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- Stripe Python SDK
- HTML5 + CSS3 (no frontend frameworks)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-stripe-checkout.git
cd django-stripe-checkout
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv env

# Windows
env\Scripts\activate

# macOS/Linux
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

. Set Stripe API Keys

Open stripe_project/settings.py and configure:

```python
STRIPE_SECRET_KEY = 'YOUR_SECRET_STRIPE_KEY'
STRIPE_PUBLISHABLE_KEY = 'YOUR_PUBLIC_STRIPE_KEY'
```

    For production apps, use environment variables instead of hardcoding keys.

5. Run Migrations

python manage.py migrate

6. Start the Development Server

python manage.py runserver

Go to http://127.0.0.1:8000 to test the checkout.

💳 Stripe Test Card

Use the following test card in Stripe Checkout:

Card Number: 4242 4242 4242 4242
Exp: Any future date
CVC: Any 3 digits
ZIP: Any 5 digits

More test cards: Stripe Testing Docs
📁 Project Structure
```
├── payments/
│   ├── templates/
│   │   ├── checkout.html
│   │   ├── success.html
│   │   └── cancel.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── stripe_project/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

📄 License

This project is licensed under the MIT License.
🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
🙋 FAQ

Q: Can I use this in production?
A: This is meant as a learning/demo project. For production, secure your API keys and use HTTPS.

Q: How do I add products dynamically?
A: You can modify the line_items in views.py to be generated from your database.
🌐 Useful Links

    🔗 Django Docs

    🔗 Stripe Docs

    🔗 Stripe Python SDK

    🔗 Stripe Checkout

👨‍💻 Author

Created by Mohammad Hosein Dadgostar
Feel free to connect or contribute!
