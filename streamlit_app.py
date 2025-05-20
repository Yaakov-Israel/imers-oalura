import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import google.generativeai as genai # Para o Google Gemini

# --- Configuração da Página Principal ---
st.set_page_config(
    page_title="Olhos da Lei - Super Agente IA",
    page_icon="👁️‍🗨️",
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
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model_pro = genai.GenerativeModel('gemini-1.5-flash-latest')
    gemini_api_configurada = True
except (KeyError, Exception) as e:
    gemini_api_configurada = False
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
    key="nav_funcoes_radio"
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
    **Olhos da Lei v0.4.2**\n
    Demonstração do ciclo operacional.
    (Verificação de sintaxe)
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

    cameras_disponiveis = {
        "Câmera Centro SP (Exemplo Teórico 1)": "LINK_INVALIDO_EXEMPLO_SP_1",
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
            url_camera_selecionada = ""

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
                prompt_analise = f"Você é o Super Agente Olhos da Lei. Analise um feed de câmera hipotético de '{camera_escolhida_nome}'. Descreva brevemente uma situação de risco potencial (1-2 frases) e classifique o Nível de Risco (1-Baixo, 2-Médio, 3-Alto)."
                try:
                    response = model_pro.generate_content(prompt_analise)
                    st.session_state.ultimo_alerta_ia = response.text
                    st.success("Análise da IA Concluída!")
                    st.markdown("**Resultado da Análise (Simulada pela IA):**")
                    st.info(response.text)
                    if "Nível de Risco: 2" in response.text or "Nível de Risco: 3" in response.text or "risco: 2" in response.text or "risco: 3" in response.text :
                        nova_ocorrencia = {
                            "id": len(st.session_state.ocorrencias_simuladas) + 1,
                            "descricao": response.text.splitlines()[0] if response.text.splitlines() else "Risco detectado pela IA",
                            "nivel": 3 if ("Nível de Risco: 3" in response.text or "risco: 3" in response.text) else 2,
                            "camera": camera_escolhida_nome,
                            "horario": datetime.now().strftime("%H:%M:%S"),
                            "lat": -23.5505 + (np.random.rand() - 0.5) * 0.1,
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
            if prompt_usuario:  # ESTA É A LINHA CRÍTICA - Verifique se o ':' está aqui!
                with st.spinner("Super Agente processando..."):
                    try:
                        response = model_pro.generate_content(prompt_usuario)
                        st.subheader("Resposta do Super Agente:")
                        st.markdown(response.text)
                        st.session_state.ultimo_alerta_ia = f"Interação: {prompt_usuario[:50]}... -> Resposta IA recebida."
                    except Exception as e:
                        st.error(f"Erro na comunicação com a IA: {e}")
            else:
                st.warning("Por favor, digite um comando ou pergunta.")
        st.markdown("---")
        st.caption("Nota: Esta é uma simulação. O Super Agente usa modelos de linguagem para responder.")


elif pagina_selecionada == "Mapa de Ocorrências":
    st.header("🗺️ Mapa de Ocorrências em Tempo Real")
    st.markdown("Visualização geográfica de alertas e incidentes detectados.")

    if not st.session_state.ocorrencias_simuladas:
        st.info("Nenhuma ocorrência simulada registrada ainda. Analise um feed de câmera para gerar alertas.")
    else:
        df_ocorrencias = pd.DataFrame(st.session_state.ocorrencias_simuladas)
        st.subheader("Mapa dos Incidentes")
        if not df_ocorrencias.empty and 'lat' in df_ocorrencias.columns and 'lon' in df_ocorrencias.columns:
            st.map(df_ocorrencias[['lat', 'lon']].dropna(), zoom=10)
        else:
            st.warning("Dados de localização ausentes ou inválidos para exibir o mapa.")

        st.subheader("Lista de Ocorrências")
        st.dataframe(df_ocorrencias[['id', 'descricao', 'nivel', 'camera', 'horario', 'status_acao']], use_container_width=True)

        ocorrencia_ids = [o["id"] for o in st.session_state.ocorrencias_simuladas if o["status_acao"] == "Pendente"]
        if ocorrencia_ids:
            ocorrencia_para_acao = st.selectbox("Selecionar Ocorrência para Ação:", ocorrencia_ids, key="map_select_ocorrencia")
            acao_tomada = st.selectbox("Ação a ser tomada (Simulação):", ["Despachar Cão-Robô", "Notificar Polícia Local", "Monitorar", "Resolver Incidente"], key="map_acao_ocorrencia")
            if st.button("Registrar Ação", key="map_registrar_acao_btn"):
                for i, oc in enumerate(st.session_state.ocorrencias_simuladas):
                    if oc["id"] == ocorrencia_para_acao:
                        st.session_state.ocorrencias_simuladas[i]["status_acao"] = f"Ação: {acao_tomada}"
                        st.success(f"Ação '{acao_tomada}' registrada para ocorrência {ocorrencia_para_acao}.")
                        if acao_tomada == "Despachar Cão-Robô":
                            robo_enviado = False
                            for nome_robo, status_info in st.session_state.status_robos.items():
                                if status_info["status"] == "Disponível" or status_info["status"] == "Em Patrulha":
                                    st.session_state.status_robos[nome_robo]["status"] = "Em Missão (Ocorr. " + str(ocorrencia_para_acao) + ")"
                                    st.session_state.status_robos[nome_robo]["local"] = f"Ocorrência {ocorrencia_para_acao}"
                                    st.toast(f"{nome_robo} despachado para ocorrência {ocorrencia_para_acao}!", icon="🐕‍🦺")
                                    robo_enviado = True
                                    break
                            if not robo_enviado:
                                st.warning("Nenhum cão-robô disponível no momento para despachar.")
                        st.rerun() 
                
    if st.button("Limpar Ocorrências Simuladas", key="limpar_ocorrencias_btn"):
        st.session_state.ocorrencias_simuladas = []
        st.session_state.ultimo_alerta_ia = None
        st.success("Ocorrências simuladas foram limpas.")
        st.rerun()

elif pagina_selecionada == "Relatórios Detalhados":
    st.header("📊 Relatórios e Estatísticas")
    st.markdown("Análises sobre detecções, respostas e desempenho do sistema (Simulação).")

    if not st.session_state.ocorrencias_simuladas:
        st.info("Nenhuma ocorrência registrada para gerar relatórios.")
    else:
        df_relatorio = pd.DataFrame(st.session_state.ocorrencias_simuladas)
        st.subheader("Resumo das Ocorrências")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total de Ocorrências Registradas", len(df_relatorio))
        with col2:
            if not df_relatorio.empty and 'nivel' in df_relatorio.columns:
                ocorrencias_alto_risco = len(df_relatorio[df_relatorio['nivel'] == 3])
                st.metric("Ocorrências de Alto Risco (Nível 3)", ocorrencias_alto_risco)
            else:
                st.metric("Ocorrências de Alto Risco (Nível 3)", 0)

        if not df_relatorio.empty and 'nivel' in df_relatorio.columns:
            st.subheader("Distribuição de Ocorrências por Nível de Risco")
            st.bar_chart(df_relatorio['nivel'].value_counts())

            st.subheader("Ocorrências por Câmera (Simulado)")
            if 'camera' in df_relatorio.columns:
                st.bar_chart(df_relatorio['camera'].value_counts())
            else:
                st.write("Dados de câmera não disponíveis para este gráfico.")
        else:
            st.write("Dados insuficientes para os gráficos.")

    st.markdown("---")
    st.info("⚠️ Implementação em andamento: Filtros avançados e mais opções de relatório.")


elif pagina_selecionada == "Configurações de Alerta":
    st.header("⚙️ Configurações de Alerta e Notificação")
    st.markdown("Personalize como e quando os alertas são enviados (Simulação).")

    st.subheader("Regras de Notificação por Nível de Risco")
    email_n1 = st.checkbox("Nível 1 (Baixo): Notificar por e-mail (Monitoramento)", value=True, key="conf_email_n1")
    sms_n2 = st.checkbox("Nível 2 (Médio): Notificar por E-mail e SMS (Atenção Requerida)", value=True, key="conf_sms_n2")
    auto_cao_n3 = st.checkbox("Nível 3 (Alto): Acionamento automático de Cão-Robô + Todas as Notificações", value=True, key="conf_cao_n3")

    st.subheader("Contatos para Notificações")
    emails_notificacao = st.text_area(
        "E-mails (um por linha):",
        "equipe.seguranca@exemplo.com\nsupervisor.turno@exemplo.com",
        key="conf_emails_lista"
    )
    telefones_sms_notificacao = st.text_area(
        "Telefones para SMS (um por linha, formato +55DDDXXXXXXXXX):",
        "+5511987654321\n+5521912345678",
        key="conf_telefones_lista"
    )

    if st.button("💾 Salvar Configurações", key="conf_salvar_btn_alerta"):
        st.success("Simulação: Configurações de alerta salvas com sucesso!")
        st.info("Em um sistema real, estas configurações seriam persistidas.")

elif pagina_selecionada == "Integração com Cães-Robôs":
    st.header("🐕‍🦺 Painel de Controle: Cães-Robôs")
    st.markdown("Monitore e comande as unidades de resposta rápida.")

    lista_nomes_robos = list(st.session_state.status_robos.keys())
    robo_selecionado_nome = st.selectbox(
        "Selecione uma Unidade Robótica:",
        lista_nomes_robos,
        key="robo_select_painel"
    )

    if robo_selecionado_nome:
        status_atual_robo = st.session_state.status_robos[robo_selecionado_nome]
        st.subheader(f"Status Detalhado: {robo_selecionado_nome}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Nível da Bateria", status_atual_robo["bateria"])
        with col2:
            st.metric("Status Operacional", status_atual_robo["status"])
        with col3:
            st.metric("Localização/Missão", status_atual_robo["local"])

        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6mZy3S2D930EK3P2TEG2afG24092qC3qyOw&s",
                 caption=f"Interface de telemetria e vídeo (simulada) para {robo_selecionado_nome}", width=400)

        st.subheader("Comandos Manuais (Simulação)")
        comando_col1, comando_col2 = st.columns(2)
        with comando_col1:
            if st.button(f"🚁 Enviar {robo_selecionado_nome} para Patrulha", key=f"cmd_patrulha_{robo_selecionado_nome.replace(' ', '_')}"): # Adicionando replace para key
                st.session_state.status_robos[robo_selecionado_nome]["status"] = "Em Patrulha"
                st.session_state.status_robos[robo_selecionado_nome]["local"] = "Setor Designado"
                st.success(f"{robo_selecionado_nome} enviado para patrulha.")
                st.rerun()
        with comando_col2:
            if st.button(f"🏠 Retornar {robo_selecionado_nome} à Base", key=f"cmd_base_{robo_selecionado_nome.replace(' ', '_')}"): # Adicionando replace para key
                st.session_state.status_robos[robo_selecionado_nome]["status"] = "Retornando à Base"
                st.session_state.status_robos[robo_selecionado_nome]["local"] = "Base"
                st.success(f"{robo_selecionado_nome} retornando à base.")
                st.rerun()
else:
    st.error("Página não encontrada! Selecione uma função válida no menu lateral.")
    st.image("https://placehold.co/600x300/red/white?text=Erro+404", caption="Página não existe")
