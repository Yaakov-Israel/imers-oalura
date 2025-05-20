import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Olhos da Lei - IA",
    page_icon="👁️",
    layout="wide"
)

# --- Barra Lateral para Navegação ---
st.sidebar.title("Navegação Principal")
pagina_selecionada = st.sidebar.radio(
    "Escolha uma seção:",
    (
        "Página Inicial",
        "Visualização de Câmeras Ao Vivo",
        "Mapa de Ocorrências",
        "Relatórios Detalhados",
        "Configurações de Alerta",
        "Integração com Cães-Robôs"
    )
)
st.sidebar.markdown("---") # Linha divisória
st.sidebar.caption("Projeto em desenvolvimento - Imersão Alura + Google Gemini")


# --- Conteúdo da Página (varia conforme a seleção na barra lateral) ---

if pagina_selecionada == "Página Inicial":
    st.title("👁️ Olhos da Lei: Super-Agente de IA")
    st.subheader("Garantindo a segurança da população com Inteligência Artificial")

    st.markdown("""
    Bem-vindo ao painel de controle do **Olhos da Lei**!

    Este sistema utiliza Inteligência Artificial para monitorar espaços públicos através de câmeras,
    detectando potenciais ameaças em tempo real para uma resposta rápida e eficaz.

    Use o menu na barra lateral para navegar pelas diferentes funcionalidades.
    """)

    st.header("🚦 Status da Detecção Simulado")
    threat_level = st.selectbox(
        "Simular Nível de Ameaça Detectada:",
        ("Nenhuma Ameaça", "Nível 1: Atividade Suspeita", "Nível 2: Ameaça Potencial", "Nível 3: Ameaça Iminente!"),
        key="selectbox_inicial" # Chave única para este selectbox
    )

    if threat_level == "Nenhuma Ameaça":
        st.success("✅ Tudo tranquilo! Nenhuma ameaça detectada no momento.")
    elif threat_level == "Nível 1: Atividade Suspeita":
        st.info("👀 Nível 1: Atividade suspeita detectada. Monitoramento intensificado.")
    elif threat_level == "Nível 2: Ameaça Potencial":
        st.warning("⚠️ Nível 2: Ameaça potencial identificada! Alerta enviado para as autoridades locais.")
    else:  # Nível 3
        st.error("🚨 NÍVEL 3: AMEAÇA IMINENTE! Ação imediata requerida! Autoridades e cães-robôs acionados!")

elif pagina_selecionada == "Visualização de Câmeras Ao Vivo":
    st.header("📹 Visualização de Câmeras Ao Vivo")
    st.markdown("Aqui você poderá visualizar o feed de diferentes câmeras em tempo real.")

    # Placeholder para seleção de câmera
    num_cameras = 5 # Simular 5 câmeras
    camera_selecionada = st.selectbox(
        "Selecione uma Câmera:",
        [f"Câmera {i+1} - Localização Exemplo {i+1}" for i in range(num_cameras)]
    )
    st.success(f"Exibindo feed da {camera_selecionada}...")

    # Placeholder para o vídeo
    st.image("https://placehold.co/600x400/000000/FFFFFF/png?text=Feed+da+Câmera+Aqui", caption=f"Simulação do feed da {camera_selecionada}")
    st.info("Nota: Esta é uma simulação. A integração com feeds reais de câmeras será implementada.")

elif pagina_selecionada == "Mapa de Ocorrências":
    st.header("🗺️ Mapa de Ocorrências")
    st.markdown("Visualize geograficamente as ocorrências e alertas detectados.")

    # Placeholder para o mapa (poderia usar st.map futuramente com dados reais)
    st.image("https://placehold.co/600x400/EFEFEF/AAAAAA/png?text=Mapa+de+Ocorrências+Aqui", caption="Simulação do mapa de ocorrências")
    st.markdown("""
    **Funcionalidades planejadas:**
    - Filtros por tipo de ocorrência, data e severidade.
    - Heatmaps de áreas de maior risco.
    - Detalhes da ocorrência ao clicar em um ponto.
    """)
    # Exemplo de como você poderia adicionar um mapa real (requer dados de latitude/longitude)
    # import pandas as pd
    # import numpy as np
    # map_data = pd.DataFrame(
    #    np.random.randn(10, 2) / [20, 20] + [-23.5505, -46.6333], # Coordenadas próximas a SP como exemplo
    #    columns=['lat', 'lon'])
    # st.map(map_data)


elif pagina_selecionada == "Relatórios Detalhados":
    st.header("📊 Relatórios Detalhados")
    st.markdown("Acesse análises e estatísticas sobre as detecções e o desempenho do sistema.")

    # Placeholders para filtros de relatório
    col1, col2 = st.columns(2)
    with col1:
        tipo_relatorio = st.selectbox("Tipo de Relatório:", ("Detecções por Período", "Eficiência de Resposta", "Tipos de Ameaças Comuns"))
    with col2:
        periodo = st.date_input("Selecione o Período:", []) # Deixa o usuário selecionar um intervalo

    st.button("Gerar Relatório")
    st.info(f"Simulação: Gerando relatório de '{tipo_relatorio}' para o período selecionado...")
    # Placeholder para o gráfico/tabela do relatório
    st.image("https://placehold.co/600x300/CCCCCC/FFFFFF/png?text=Gráfico+do+Relatório+Aqui", caption="Exemplo de visualização de relatório")


elif pagina_selecionada == "Configurações de Alerta":
    st.header("⚙️ Configurações de Alerta")
    st.markdown("Personalize como e quando os alertas são enviados.")

    st.subheader("Níveis de Risco e Ações")
    st.checkbox("Ativar alertas por e-mail para Nível 1", value=True)
    st.checkbox("Ativar alertas por SMS para Nível 2", value=True)
    st.checkbox("Acionar Cães-Robôs automaticamente para Nível 3")

    st.text_input("E-mails para notificação (separados por vírgula):", "alerta@policia.gov.br, supervisor@seguranca.com")
    st.text_input("Números de SMS para notificação (separados por vírgula):", "+5511999998888, +5521988887777")

    st.button("Salvar Configurações de Alerta")
    st.success("Simulação: Configurações de alerta salvas!")

elif pagina_selecionada == "Integração com Cães-Robôs":
    st.header("🐕‍🦺 Integração com Cães-Robôs")
    st.markdown("Monitore e controle as unidades de cães-robôs.")

    num_robos = 3
    robo_selecionado = st.selectbox(
        "Selecione um Cão-Robô:",
        [f"Robô Guardião {i+1}" for i in range(num_robos)]
    )

    st.subheader
