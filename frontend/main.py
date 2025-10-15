import os
import streamlit as st
import requests

# 📌 Получаем URL бэкенда из переменных окружения (или localhost по умолчанию)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("Авторизация")

is_signup = st.toggle("Регистрация")

# ============================ 📩 РЕГИСТРАЦИЯ ============================
if is_signup:
    with st.form("signup_form"):
        st.subheader("Регистрация")
        email = st.text_input("Email")
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        password_confirm = st.text_input("Подтвердите пароль", type="password")
        submit = st.form_submit_button("Зарегистрироваться")

        if submit:
            if password != password_confirm:
                st.error("Пароли не совпадают")
            elif not username or not password:
                st.warning("Введите имя пользователя и пароль")
            else:
                payload = {"username": username, "password": password, "email": email}
                try:
                    response = requests.post(f"{BACKEND_URL}/user/register", params=payload)
                    if response.status_code == 200:
                        st.success("Регистрация успешна!")
                        st.session_state["username"] = username
                        st.switch_page("pages/profile.py")  # ✅ без "pages/"
                    else:
                        st.error(f"Ошибка: {response.json().get('detail', 'Неизвестная ошибка')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Не удалось подключиться к серверу: {e}")

# ============================ 🔐 ВХОД ============================
else:
    with st.form("login_form"):
        st.subheader("Вход")
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        submit = st.form_submit_button("Войти")

        if submit:
            if not username or not password:
                st.warning("Введите имя пользователя и пароль")
            else:
                payload = {"username": username, "password": password}
                try:
                    response = requests.post(f"{BACKEND_URL}/user/login", params=payload)
                    if response.status_code == 200:
                        st.success("Вход выполнен!")
                        st.session_state["username"] = username
                        st.switch_page("pages/profile.py")  # ✅ переход на страницу
                    else:
                        st.error(f"Ошибка: {response.json().get('detail', 'Неверные данные')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Не удалось подключиться к серверу: {e}")
