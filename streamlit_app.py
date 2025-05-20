import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import google.generativeai as genai # Para o Google Gemini

# --- Configuração da Página Principal ---
st.set_page_config(
    page_title="Olhos da Lei - Super Agente IA",
    page_icon="👁️‍🗨️", # Um ícone um pouco diferente
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Gerenciamento de Estado da Sessão (para integração entre funções) ---
if 'ocorrencias_simuladas' not in st.session_state:
    st.session_state.ocorrencias_simuladas = []
if 'ultimo_alerta_ia' not in st.session_state:
    st.session_state.ultimo_alerta_ia = None
if 'status_robos' not in st.session_state:
    st.session_state.status_robos = {
        "Robô Guardião Alpha-1": {"bateria": "90%", "status": "Disponível", "local": "Base"},
        "Robô Guardião Bravo-2": {"bateria": "85%", "status": "Em Patrulha", "local": "Setor Delta"},
        "Robô Guardião Charlie-3": {"bateria": "70%", "status": "Recarregando", "local": "Base"}
    }

# --- Configuração da API Key do Google Gemini (AI Studio) ---
try:
    # Idealmente, configure GOOGLE_API_KEY nos Secrets do Streamlit Cloud
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model_pro = genai.GenerativeModel('gemini-1.5-flash-latest') # Usando um modelo mais recente e rápido
    # Para visão, seria: model_vision = genai.GenerativeModel('gemini-pro-vision')
    gemini_api_configurada = True
except (KeyError, Exception) as e:
    gemini_api_configurada = False
    # Não para o app, mas avisa e limita funcionalidades de IA
    pass

# --- Barra Lateral de Navegação ---
st.sidebar.title("⚙️ Funções do Super Agente")
st.sidebar.markdown("---")

lista_funcoes = [
    "Página Inicial",
    "Visualização de Câmeras Ao Vivo",
    "Análise com IA (Gemini)",
    "Mapa de Ocorrências",
    "Relatórios Detalhados",
    "Configurações de Alerta",
    "Integração com Cães-Robôs"
]
pagina_selecionada = st.sidebar.radio(
    "Selecione uma função:",
    lista_funcoes,
    key="nav_funcoes_radio" # Chave única para o widget
)

st.sidebar.markdown("---")
st.sidebar.subheader("Status do Sistema")
if gemini_api_configurada:
    st.sidebar.success("✅ API Gemini Conectada")
else:
    st.sidebar.warning("⚠️ API Gemini Não Configurada.\nVerifique os `secrets` para IA.")

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Olhos da Lei v0.4**\n
    Demonstração do ciclo operacional.
    """
)
st.sidebar.caption(f"Hoje é {datetime.now().strftime('%d/%m/%Y')}")


# --- Conteúdo Principal da Página (controlado pela navegação) ---

if pagina_selecionada == "Página Inicial":
    st.title("👁️‍🗨️ Olhos da Lei: Super Agente de IA")
    st.subheader("Vigilância Inteligente para um Brasil Mais Seguro")
    st.markdown("""
    Bem-vindo à interface de demonstração do **Olhos da Lei**. Este sistema foi concebido
    para operar autonomamente, utilizando Inteligência Artificial para:

    - **Monitorar** transmissões de câmeras em tempo real.
    - **Detectar** anomalias, ameaças e comportamentos de risco.
    - **Classificar** a severidade dos incidentes.
    - **Alertar** as autoridades competentes e unidades de resposta rápida (incluindo cães-robôs).
    - **Gerar** relatórios e insights para otimizar a segurança pública.

    Navegue pelas **Funções** na barra lateral para visualizar simulações de cada etapa do ciclo operacional.
    O objetivo é demonstrar como o Super Agente processaria informações e coordenaria respostas,
    reduzindo a necessidade de monitoramento humano constante e permitindo que os operadores humanos
    foquem em ensinar e aprimorar o sistema.
    """)
    if st.session_state.ultimo_alerta_ia:
        st.warning(f"**Último Alerta da IA:** {st.session_state.ultimo_alerta_ia}")


elif pagina_selecionada == "Visualização de Câmeras Ao Vivo":
    st.header("📹 Visualização de Câmeras Ao Vivo")
    st.markdown("Simulação de acesso a feeds de câmeras públicas.")

    # Tentar encontrar câmeras de SP é difícil, links mudam. Usaremos placeholders e exemplos.
    cameras_disponiveis = {
        "Câmera Centro SP (Exemplo Teórico 1)": "LINK_INVALIDO_EXEMPLO_SP_1", # Substituir por links reais se encontrados
        "Avenida Paulista (Exemplo Teórico 2)": "LINK_INVALIDO_EXEMPLO_SP_2",
        "Praia (Exemplo Genérico - Pode não funcionar)": "http://200.20.203.134/mjpg/video.mjpg",
        "Tráfego (Univ. Heidelberg - Exemplo)": "http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg",
        "Adicionar URL MJPEG Manualmente": "MANUAL"
    }
    camera_escolhida_nome = st.selectbox(
        "Selecione uma Câmera (Exemplos):",
        list(cameras_disponiveis.keys()),
        key="cam_select_vivo"
    )
    url_camera_selecionada = cameras_disponiveis[camera_escolhida_nome]

    if url_camera_selecionada == "MANUAL":
        url_manual = st.text_input("Digite a URL do stream MJPEG:", key="url_manual_cam")
        if url_manual:
            url_camera_selecionada = url_manual
        else:
            st.info("Por favor, insira uma URL para visualização manual.")
            url_camera_selecionada = "" # Evitar erro

    if url_camera_selecionada and "LINK_INVALIDO" not in url_camera_selecionada and url_camera_selecionada != "MANUAL":
        st.markdown(f"**Visualizando:** {camera_escolhida_nome}")
        st.markdown(f"<small>URL: {url_camera_selecionada}</small>", unsafe_allow_html=True)
        try:
            st.image(url_camera_selecionada, caption=f"Feed da {camera_escolhida_nome}", width=640)
            st.success("Tentando carregar feed da câmera...")
        except Exception as e:
            st.error(f"Não foi possível carregar o feed: {camera_escolhida_nome}.")
            st.caption(f"Detalhes: {e}")
            st.info("Dica: Apenas streams MJPEG diretos funcionam bem. Links de portais (Ex: CET) geralmente não são compatíveis aqui.")
    elif "LINK_INVALIDO" in url_camera_selecionada:
        st.warning(f"Link para '{camera_escolhida_nome}' é apenas um exemplo teórico. Precisamos de uma URL MJPEG real e funcional.")
        st.image("https://placehold.co/640x480/silver/black?text=Feed+Indisponível", caption=camera_escolhida_nome)

    st.markdown("---")
    st.subheader("Análise Automática pelo Super Agente")
    if st.button("👁️‍🗨️ Iniciar Análise de IA nesta Câmera", key="analisar_camera_btn"):
        if gemini_api_configurada:
            with st.spinner("Super Agente analisando o feed..."):
                # Simulação: Em um sistema real, capturaríamos um frame da câmera
                # Aqui, vamos usar um prompt genérico para o Gemini
                prompt_analise = f"Você é o Super Agente Olhos da Lei. Analise um feed de câmera hipotético de '{camera_escolhida_nome}'. Descreva brevemente uma situação de risco potencial (1-2 frases) e classifique o Nível de Risco (1-Baixo, 2-Médio, 3-Alto)."
                try:
                    response = model_pro.generate_content(prompt_analise)
                    st.session_state.ultimo_alerta_ia = response.text
                    st.success("Análise da IA Concluída!")
                    st.markdown("**Resultado da Análise (Simulada pela IA):**")
                    st.info(response.text)

                    # Simular adição de ocorrência se risco for médio/alto
                    if "Nível de Risco: 2" in response.text or "Nível de Risco: 3" in response.text or "risco: 2" in response.text or "risco: 3" in response.text :
                        nova_ocorrencia = {
                            "id": len(st.session_state.ocorrencias_simuladas) + 1,
                            "descricao": response.text.splitlines()[0] if response.text.splitlines() else "Risco detectado pela IA",
                            "nivel": 3 if ("Nível de Risco: 3" in response.text or "risco: 3" in response.text) else 2,
                            "camera": camera_escolhida_nome,
                            "horario": datetime.now().strftime("%H:%M:%S"),
                            "lat": -23.5505 + (np.random.rand() - 0.5) * 0.1, # Aleatório perto de SP
                            "lon": -46.6333 + (np.random.rand() - 0.5) * 0.1,
                            "status_acao": "Pendente"
                        }
                        st.session_state.ocorrencias_simuladas.append(nova_ocorrencia)
                        st.toast(f"Nova ocorrência (Nível {nova_ocorrencia['nivel']}) registrada no Mapa!", icon="🗺️")

                except Exception as e:
                    st.error(f"Erro ao contatar IA: {e}")
        else:
            st.warning("API do Gemini não configurada. Análise de IA indisponível.")

elif pagina_selecionada == "Análise com IA (Gemini)":
    st.header("🧠 Interagir com o Super Agente (Gemini)")
    st.markdown("Faça perguntas ou dê instruções ao Super Agente para simular análises.")

    if not gemini_api_configurada:
        st.error("API do Google Gemini não está configurada nos `secrets`. Esta função está desabilitada.")
    else:
        prompt_default = "Super Agente, quais são os procedimentos padrão ao detectar uma briga em uma praça pública?"
        prompt_usuario = st.text_area("Seu comando ou pergunta para o Super Agente:", value=prompt_default, height=150, key="gemini_prompt_interacao")
        if st.button("🧠 Enviar para Super Agente", key="gemini_submit_interacao_btn"):
            if prompt_usuario
