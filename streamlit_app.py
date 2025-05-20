import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Olhos da Lei - IA",
    page_icon="👁️", # Pode ser um emoji ou o caminho para um arquivo de ícone
    layout="wide" # 'centered' ou 'wide'
)

# --- Cabeçalho e Descrição ---
st.title("👁️ Olhos da Lei: Super-Agente de IA")
st.subheader("Garantindo a segurança da população com Inteligência Artificial")

st.markdown("""
Bem-vindo ao painel de controle do **Olhos da Lei**!

Este sistema utiliza Inteligência Artificial para monitorar espaços públicos através de câmeras,
detectando potenciais ameaças em tempo real para uma resposta rápida e eficaz.
""")

# --- Seção de Demonstração/Status (Placeholder) ---
st.header("🚦 Status da Detecção")

# Adicionar um selectbox para simular diferentes tipos de ameaças (exemplo)
threat_level = st.selectbox(
    "Simular Nível de Ameaça Detectada:",
    ("Nenhuma Ameaça", "Nível 1: Atividade Suspeita", "Nível 2: Ameaça Potencial", "Nível 3: Ameaça Iminente!")
)

if threat_level == "Nenhuma Ameaça":
    st.success("✅ Tudo tranquilo! Nenhuma ameaça detectada no momento.")
elif threat_level == "Nível 1: Atividade Suspeita":
    st.info("👀 Nível 1: Atividade suspeita detectada. Monitoramento intensificado.")
elif threat_level == "Nível 2: Ameaça Potencial":
    st.warning("⚠️ Nível 2: Ameaça potencial identificada! Alerta enviado para as autoridades locais.")
else: # Nível 3
    st.error("🚨 NÍVEL 3: AMEAÇA IMINENTE! Ação imediata requerida! Autoridades e cães-robôs acionados!")

# --- Placeholder para futuras funcionalidades ---
st.sidebar.header("Funcionalidades Futuras")
st.sidebar.markdown("""
- Visualização de Câmeras Ao Vivo
- Mapa de Ocorrências
- Relatórios Detalhados
- Configurações de Alerta
- Integração com Cães-Robôs
""")

st.caption("Projeto em desenvolvimento - Imersão Alura + Google Gemini")
