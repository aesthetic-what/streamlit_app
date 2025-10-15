import streamlit as st
import requests


label = st.title("Авторизация", anchor=False, width="content")

is_signup = st.toggle("Регистрация")

if is_signup:
    # Форма регистрации
    with st.form("signup_form"):
        st.subheader("Регистрация")
        email = st.text_input("Email")
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        password_confirm = st.text_input("Подтвердите пароль", type="password")
        submit = st.form_submit_button("Зарегистрироваться")
        
        # params = {"username": username, "password": password, "email": email}

        if submit:
            response = requests.post(f"http://localhost:8000/user/register?username={username}&password={password}&email={email}")
            # В дальнейшем лучше изменить способ регистрации на headers или другой похожий тип, для более безопасной регистрации
            # print(response.json()["status_code"])
            # result = response.json()
            if response.status_code == 200:
                st.success("Регистрация успешна!")
                st.switch_page("pages/streamlit_main.py")
            else:
                st.error("Ошибка, Такой пользователь уже есть")
else:
    # Форма входа
    with st.form("login_form"):
        st.subheader("Вход")
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        submit = st.form_submit_button("Войти")
        
        params = {"username": username, "password": password}

        if submit:
            response = requests.post(f"http://localhost:8000/user/login?username={username}&password={password}")

            if response.status_code == 200:
                st.success("Вход выполнен!")
                st.switch_page("pages/streamlit_main.py")
            else:
                st.error(f"Ошибка, {response.json()["detail"]}")
