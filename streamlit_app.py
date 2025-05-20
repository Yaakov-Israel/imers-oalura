import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import google.generativeai as genai # Adicionado para o Gemini

# --- Configuração da Página ---
st.set_page_config(
    page_title="Olhos da Lei - IA",
    page_icon="👁️",
    layout="wide"
)

# --- Configuração da API Key do Google Gemini ---
# A API Key DEVE ser configurada nos Secrets do Streamlit
# Crie um arquivo chamado .streamlit/secrets.toml no seu repositório
# E adicione: GOOGLE_API_KEY = "SUA_API_KEY_AQUI"

try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro') # Ou outro modelo, como gemini-pro-vision para imagens
    gemini_api_configurada = True
except (KeyError, Exception) as e: # Captura KeyError se a chave não existir ou outra exceção na configuração
    gemini_api_configurada = False
    # Não vamos parar o app se a API não estiver configurada, apenas avisar e desabilitar funcionalidades
    pass # Continuar mesmo se a API não estiver configurada

# --- Barra Lateral para Navegação ---
st.sidebar.title("🔭 Navegação Principal")
pagina_selecionada = st.sidebar.radio(
    "Escolha uma seção:",
    (
        "Página Inicial",
        "Visualização de Câmeras Ao Vivo",
        "Análise com IA (Gemini)", # Nova seção para testar o Gemini
        "Mapa de Ocorrências",
        "Relatórios Detalhados",
        "Configurações de Alerta",
        "Integração com Cães-Robôs"
    ),
    key="nav_radio"
)
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Olhos da Lei v0.3**\n
    Projeto em desenvolvimento.
    """
)
if not gemini_api_configurada:
    st.sidebar.warning("API do Google Gemini não configurada. Funcionalidades de IA limitadas. Verifique os `secrets`.")
else:
    st.sidebar.success("API do Google Gemini conectada!")
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

    cameras_publicas = {
        "Praia (Exemplo Genérico - Pode não funcionar)": "http://200.20.203.134/mjpg/video.mjpg",
        "Tráfego (Univ. Heidelberg - Exemplo)": "http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg",
        "Webcam (Rússia - Exemplo)": "http://webcampub.multivision.ru:8090/mjpg/video.mjpg",
        "Placeholder - Adicione sua URL MJPEG": ""
    }

    camera_escolhida_nome = st.selectbox(
        "Selecione uma Câmera Pública (Exemplo):",
        list(cameras_publicas.keys()),
        key="cam_select"
    )
    url_camera_selecionada = cameras_publicas[camera_escolhida_nome]

    if url_camera_selecionada:
        st.markdown(f"**Visualizando:** {camera_escolhida_nome}")
        st.markdown(f"<small>URL: {url_camera_selecionada}</small>", unsafe_allow_html=True)
        try:
            st.image(url_camera_selecionada, caption=f"Feed da {camera_escolhida_nome}", width=720)
            st.success("Tentando carregar feed da câmera...")
        except Exception as e:
            st.error(f"Não foi possível carregar o feed da câmera selecionada.")
            st.warning(f"Detalhes do erro: {e}")
            st.info("Dica: Streams MJPEG são mais compatíveis. Verifique se a URL está correta e acessível.")
            st.markdown("Você pode tentar abrir a URL diretamente no seu navegador para testar.")
    elif camera_escolhida_nome == "Placeholder - Adicione sua URL MJPEG":
        st.info("Adicione uma URL de stream MJPEG válida no código para testar esta funcionalidade.")
    else:
        st.info("Selecione uma câmera da lista para visualizar.")

    st.markdown("---")
    st.subheader("Análise de IA desta Câmera (Simulação)")
    if st.button("Analisar feed da câmera com IA", key="analisar_feed_btn"):
        if gemini_api_configurada:
            st.info("🤖 Implementação em andamento: Análise de IA para esta câmera usando Gemini...")
            # Aqui você chamaria a função que captura um frame e envia para o Gemini Vision
        else:
            st.warning("API do Gemini não configurada. Não é possível analisar.")

elif pagina_selecionada == "Análise com IA (Gemini)":
    st.header("🧠 Análise com Inteligência Artificial (Gemini)")
    st.markdown("Use o poder do Google Gemini para análises.")

    if not gemini_api_configurada:
        st.error("API do Google Gemini não está configurada nos Secrets. Esta seção não pode funcionar.")
    else:
        st.info("API do Gemini conectada! Você pode usar modelos como 'gemini-pro' para texto ou 'gemini-pro-vision' para imagens.")

        prompt_usuario = st.text_area("Digite seu prompt para o Gemini (ex: descreva uma cena de segurança em uma praça pública):", height=100, key="gemini_prompt")
        if st.button("Enviar para Gemini", key="gemini_submit_btn"):
            if prompt_usuario:
                try:
                    with st.spinner("Aguardando resposta do Gemini..."):
                        response = model.generate_content(prompt_usuario)
                        st.subheader("Resposta do Gemini:")
                        st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao chamar a API do Gemini: {e}")
            else:
                st.warning("Por favor, digite um prompt.")

        st.markdown("---")
        st.subheader("Teste com Imagem (Funcionalidade Futura para Gemini Vision)")
        uploaded_file = st.file_uploader("Carregue uma imagem para análise (placeholder):", type=["jpg", "jpeg", "png"], key="img_upload_gemini")
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Imagem Carregada", use_column_width=True)
            if st.button("Analisar Imagem com Gemini Vision (Simulado)", key="gemini_vision_btn"):
                st.info("🤖 Implementação em andamento: Análise desta imagem com Gemini Vision.")
                # Em uma implementação real:
                # image_bytes = uploaded_file.getvalue()
                # image_parts = [{"mime_type": uploaded_file.type, "data": image_bytes}]
                # prompt_parts = [image_parts[0], "\nDescreva esta imagem em detalhes."]
                # response = model_vision.generate_content(prompt_parts) -> (usar o modelo gemini-pro-vision)
                # st.markdown(response.text)


elif pagina_selecionada == "Mapa de Ocorrências":
    st.header("🗺️ Mapa de Ocorrências")
    st.markdown("Visualize geograficamente as ocorrências e alertas detectados.")
    map_data = pd.DataFrame(
        np.random.randn(20, 2) / np.array([10, 10]) + np.array([-23.5505, -46.6333]), # Coordenadas próximas a SP
        columns=['lat', 'lon']
    )
    st.map(map_data, zoom=10)
    st.subheader("Detalhes da Ocorrência Selecionada (Simulação)")
    ocorrencia_id = st.text_input("ID da Ocorrência (Ex: 12345):", "", key="map_ocorrencia_id")
    if st.button("Buscar Detalhes da Ocorrência", key="map_buscar_btn"):
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
            ("Detecções por Período", "Eficiência de Resposta", "Tipos de Ameaças Comuns", "Performance por Câmera"),
            key="rel_tipo"
        )
    with col2:
        data_hoje = datetime.now().date() # Usar .date() para date_input
        data_inicio_padrao = data_hoje - timedelta(days=7)
        periodo = st.date_input(
            "Selecione o Período:",
            [data_inicio_padrao, data_hoje], # [inicio, fim]
            key="rel_periodo",
            max_date=data_hoje # Evitar datas futuras
        )
    if st.button("Gerar Relatório", key="rel_gerar_btn"):
        if periodo and len(periodo) == 2:
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
    alerta_email_n1 = st.checkbox("Ativar alertas por e-mail para Nível 1 (Atividade Suspeita)", value=True, key="conf_email_n1")
    alerta_sms_n2 = st.checkbox("Ativar alertas por SMS para Nível 2 (Ameaça Potencial)", value=True, key="conf_sms_n2")
    acionar_caes_n3 = st.checkbox("Acionar Cães-Robôs automaticamente para Nível 3 (Ameaça Iminente)", key="conf_caes_n3")
    st.subheader("Contatos para Notificação")
    emails_notificacao = st.text_area(
        "E-mails para notificação (um por linha):",
        "alerta.policia@exemplo.gov.br\nsupervisor.seguranca@exemplo.com\nresponsavel.area@exemplo.com.br",
        key="conf_emails"
    )
    telefones_sms = st.text_area(
        "Telefones para SMS (um por linha, formato +55DDDXXXXXXXXX):",
        "+5511999998888\n+5521988887777",
        key="conf_telefones"
    )
    if st.button("Salvar Configurações de Alerta", key="conf_salvar_btn"):
        st.info("⚠️ Implementação em andamento: Salvamento das configurações de alerta.")

elif pagina_selecionada == "Integração com Cães-Robôs":
    st.header("🐕‍🦺 Integração com Cães-Robôs")
    st.markdown("Monitore e controle as unidades de cães-robôs para resposta a ameaças.")
    num_robos_disponiveis = 3
    lista_robos = [f"Robô Guardião Alpha-{i+1}" for i in range(num_robos_disponiveis)]
    robo_selecionado = st.selectbox(
        "Selecione uma Unidade Robótica:",
        lista_robos,
        key="robo_select"
    )
    st.subheader(f"Status do {robo_selecionado}")
    col1, col2, col3 = st.columns(3)
    bateria_percent = np.random.randint(60, 101)
    status_robo = np.random.choice(["Em Patrulha", "Disponível", "Recarregando", "Em Missão"])
    local_robo = f"Setor {np.random.choice(['Alpha', 'Beta', 'Gamma'])}-{np.random.randint(1,10)}"
    with col1:
        st.metric("Nível da Bateria", f"{bateria_percent}%", f"{bateria_percent-np.random.randint(0,5)}%" if bateria_percent > 65 else f"-{np.random.randint(0,5)}%")
    with col2:
        st.metric("Status Operacional", status_robo)
    with col3:
        st.metric("Localização Atual", local_robo)
    st.subheader("Comandos Táticos")
    if st.button(f"Enviar {robo_selecionado} para Ponto de Alerta Imediato", key="robo_alerta_btn"):
        st.info(f"⚠️ Implementação em andamento: Comando para {robo_selecionado} ir ao ponto de alerta.")
    if st.button(f"Instruir {robo_selecionado} a Iniciar Protocolo de Contenção", key="robo_conter_btn"):
        st.info(f"⚠️ Implementação em andamento: Comando de contenção para {robo_selecionado}.")
    if st.button(f"Retornar {robo_selecionado} para Base de Recarga", key="robo_base_btn"):
        st.info(f"⚠️ Implementação em andamento: Comando para {robo_selecionado} retornar à base.")
    st.image("https://placehold.co/600x350/333333/FFFFFF/png?text=Interface+de+Controle+do+Robô", caption=f"Simulação da interface de vídeo e controle para o {robo_selecionado}")

else:
    st.error("Página não encontrada! Selecione uma opção no menu lateral.")
