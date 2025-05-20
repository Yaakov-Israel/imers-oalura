import streamlit as st

st.sidebar.title("Teste de Navegação")
pagina = st.sidebar.radio(
    "Selecione:",
    ("Início", "Página 2", "Página 3"),
    key="nav_teste"
)

if pagina == "Início":
    st.header("Você está no Início")
    st.write("Conteúdo da página inicial de teste.")
elif pagina == "Página 2":
    st.header("Você está na Página 2")
    st.write("Conteúdo da página 2 de teste.")
elif pagina == "Página 3":
    st.header("Você está na Página 3")
    st.write("Conteúdo da página 3 de teste.")
else:
    st.write("Página desconhecida")

st.write(f"Página selecionada: {pagina}") # Para depuração
