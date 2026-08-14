import streamlit as st

st.title("Sistema de Notas")

# session_state guarda dados que "sobrevivem" entre interações
if "notas" not in st.session_state:
    st.session_state.notas = {}

materias = ["Português", "Matematica", "Ciências", "Literatura", "Filosofia"]

nome_materia = st.selectbox("Selecione a matéria:", materias)

if nome_materia in st.session_state.notas:
    st.write(f"Você já tem uma nota salva em {nome_materia}: {st.session_state.notas[nome_materia]:.2f}")
    trocar = st.checkbox("Deseja trocar a nota?")
else:
    trocar = True   # se não existe, já pede as notas direto

if trocar:
    Nota1 = st.number_input("1ª nota", min_value=0.0, max_value=10.0, step=0.5)
    Nota2 = st.number_input("2ª nota", min_value=0.0, max_value=10.0, step=0.5)
    Nota3 = st.number_input("3ª nota", min_value=0.0, max_value=10.0, step=0.5)

    if st.button("Calcular e salvar"):
        media = (Nota1 + Nota2 + Nota3) / 3
        st.session_state.notas[nome_materia] = media

        st.write(f"Sua média em {nome_materia} foi: {media:.2f}")

        if media >= 6:
            st.success("Você foi Aprovado!")
        else:
            st.error("Você foi reprovado.")