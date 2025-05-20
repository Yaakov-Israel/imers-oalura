import streamlit as st
import pandas as pd # Para o mapa de exemplo
import numpy as np  # Para o mapa de exemplo

# --- Configuração da Página ---
st.set_page_config(
    page_title="Olhos da Lei - IA",
    page_icon="👁️",
    layout="wide"
)

# --- Barra Lateral para Navegação ---
st.sidebar.title("🔭 Navegação Principal")
pagina_selecionada = st.sidebar.radio(
    "Escolha uma seção:",
    (
        "Página Inicial",
        "Visualização de Câmeras Ao Vivo",
        "Mapa de Ocorrências",
        "Relatórios Detalhados",
        "Configurações de Alerta",
        "Integração com Cães-Robôs"
    ),
    key="nav_radio" # Adicionando uma chave para garantir o estado
)
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Olhos da Lei v0.2**\n
    Projeto em desenvolvimento.
    """
)
st.sidebar.caption("Imersão Alura + Google Gemini")


# --- Conteúdo da Página (varia conforme a seleção na barra lateral) ---

if pagina_selecionada == "Página Inicial":
    st.title("👁️ Olhos da Lei: Super-Agente de IA")
    st.subheader("Garantindo a segurança da população com Inteligência Artificial")

    st.markdown("""
    Bem-vindo ao painel de controle do **Olhos da Lei**!

    Este sistema utiliza Inteligência Artificial para monitorar espaços públicos através de câmeras,
    detectando potenciais ameaças em tempo real para uma resposta rápida e eficaz.

    Use o menu na barra lateral à esquerda para navegar pelas diferentes funcionalidades.
    """)
    st.info("Esta é a página inicial. Selecione uma funcionalidade na barra lateral para começar.", icon="👈")


elif pagina_selecionada == "Visualização de Câmeras Ao Vivo":
    st.header("📹 Visualização de Câmeras Ao Vivo")
    st.markdown("Acompanhe feeds de câmeras em tempo real.")

    # Exemplo de URLs de câmeras públicas (MJPEG são mais fáceis de embutir)
    # Estas URLs são exemplos e podem não estar sempre online ou podem mudar.
    # É importante encontrar URLs de streams MJPEG ou que possam ser embutidas em um <iframe>.
    cameras_publicas = {
        "Praia de Copacabana (Exemplo 1 - Pode não funcionar sempre)": "http://200.20.203.134/mjpg/video.mjpg?timestamp=1605659000", # Exemplo, pode estar offline
        "Tráfego em Cidade Aleatória (Exemplo 2 - Procurar por 'inurl:axis-cgi/mjpg/video.mjpg')": "http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg", # Exemplo da Univ. Heidelberg
        "Outra Câmera (Exemplo 3)": "http://webcampub.multivision.ru:8090/mjpg/video.mjpg", # Outro exemplo
        "Placeholder - Adicione sua URL": ""
    }

    camera_escolhida_nome = st.selectbox(
        "Selecione uma Câmera Pública (Exemplo):",
        list(cameras_publicas.keys())
    )
    url_camera_selecionada = cameras_publicas[camera_escolhida_nome]

    if url_camera_selecionada:
        st.markdown(f"**Visualizando:** {camera_escolhida_nome}")
        st.markdown(f"<small>URL: {url_camera_selecionada}</small>", unsafe_allow_html=True)
        try:
            # Para streams MJPEG, st.image funciona. Outros podem precisar de HTML/iframe.
            st.image(url_camera_selecionada, caption=f"Feed da {camera_escolhida_nome}", width=720)
            st.success("Feed da câmera carregado.")
        except Exception as e:
            st.error(f"Não foi possível carregar o feed da câmera selecionada.")
            st.warning(f"Detalhes do erro: {e}")
            st.info("Dica: Streams MJPEG são mais compatíveis. Verifique se a URL está correta e acessível.")
            st.markdown("Você pode tentar abrir a URL diretamente no seu navegador para testar.")
    elif camera_escolhida_nome == "Placeholder - Adicione sua URL":
        st.info("Adicione uma URL de stream MJPEG válida no código para testar esta funcionalidade.")
    else:
        st.info("Selecione uma câmera da lista para visualizar.")

    st.markdown("---")
    st.subheader("Detecção de Ameaças Nesta Câmera")
    if st.button("Analisar feed da câmera selecionada"):
        st.info("⚠️ Implementação em andamento: Análise de IA para esta câmera.")


elif pagina_selecionada == "Mapa de Ocorrências":
    st.header("🗺️ Mapa de Ocorrências")
    st.markdown("Visualize geograficamente as ocorrências e alertas detectados.")

    # Gerando dados de exemplo para o mapa
    # No Brasil, use coordenadas negativas para latitude e longitude (aproximadamente)
    # Exemplo: São Paulo: lat ~-23.55, lon ~-46.63
    # Exemplo: Rio de Janeiro: lat ~-22.90, lon ~-43.17
    map_data = pd.DataFrame(
        np.random.randn(20, 2) / [10, 10] + [-23.5505, -46.6333], # Coordenadas próximas a SP
        columns=['lat', 'lon']
    )
    st.map(map_data, zoom=10)

    st.subheader("Detalhes da Ocorrência Selecionada (Simulação)")
    ocorrencia_id = st.text_input("ID da Ocorrência (Ex: 12345):", "")
    if st.button("Buscar Detalhes da Ocorrência"):
        if ocorrencia_id:
            st.info(f"⚠️ Implementação em andamento: Busca de detalhes para ocorrência {ocorrencia_id}.")
        else:
            st.warning("Por favor, insira um ID de ocorrência.")


elif pagina_selecionada == "Relatórios Detalhados":
    st.header("📊 Relatórios Detalhados")
    st.markdown("Acesse análises e estatísticas sobre as detecções e o desempenho do sistema.")

    col1, col2 = st.columns(2)
    with col1:
        tipo_relatorio = st.selectbox(
            "Tipo de Relatório:",
            ("Detecções por Período", "Eficiência de Resposta", "Tipos de Ameaças Comuns", "Performance por Câmera")
        )
    with col2:
        # Definindo datas padrão para evitar erro se o usuário não selecionar
        from datetime import datetime, timedelta
        data_hoje = datetime.now()
        data_inicio_padrao = data_hoje - timedelta(days=7)
        periodo = st.date_input(
            "Selecione o Período:",
            [data_inicio_padrao, data_hoje] # [inicio, fim]
        )

    if st.button("Gerar Relatório"):
        if len(periodo) == 2:
            st.info(f"⚠️ Implementação em andamento: Geração do relatório '{tipo_relatorio}' para o período de {periodo[0].strftime('%d/%m/%Y')} a {periodo[1].strftime('%d/%m/%Y')}.")
        else:
            st.warning("Por favor, selecione um período válido (data de início e fim).")

    st.markdown("---")
    st.subheader("Visualização do Relatório (Exemplo)")
    st.image("https://placehold.co/700x300/EFEFEF/AAAAAA/png?text=Gráfico+do+Relatório+Aqui", caption="Exemplo de visualização de dados do relatório")


elif pagina_selecionada == "Configurações de Alerta":
    st.header("⚙️ Configurações de Alerta")
    st.markdown("Personalize como e quando os alertas são enviados e para quem.")

    st.subheader("Níveis de Risco e Ações Imediatas")
    alerta_email_n1 = st.checkbox("Ativar alertas por e-mail para Nível 1 (Atividade Suspeita)", value=True)
    alerta_sms_n2 = st.checkbox("Ativar alertas por SMS para Nível 2 (Ameaça Potencial)", value=True)
    acionar_caes_n3 = st.checkbox("Acionar Cães-Robôs automaticamente para Nível 3
