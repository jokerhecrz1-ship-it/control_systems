"""
app.py — نقطة دخول تطبيق Flask
منصة تدريب نظم التحكم · 6 أشهر
"""

from flask import Flask, render_template

# إنشاء تطبيق Flask
app = Flask(__name__)


@app.route('/')
def index():
    """الصفحة الرئيسية — تُرجع قالب index.html"""
    return render_template('index.html')


if __name__ == '__main__':
    # تشغيل على المنفذ 5000 مع وضع التطوير
    app.run(debug=True, port=5000)
