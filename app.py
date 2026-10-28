import streamlit as st

st.set_page_config(layout="wide", page_title="Dashboard - Atividade 06")

with st.sidebar:
    st.header("👤 Informações do Aluno")
    nome = st.text_input("Nome:", "Seu Nome Completo")
    chamada = st.text_input("Número da Chamada:", "00")
    turma = st.text_input("Turma:", "3º Ano X")
    st.markdown("---")
    st.caption("Recolha esta barra lateral para expandir a visão dos gráficos.")

st.title("📊 Dashboard Executivo - Atividade 06")
st.markdown("Visualização integrada e análise exploratória dos dados corporativos e demográficos.")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Regressão Linear")
    st.image("regressao.png", use_container_width=True)
    st.info(
        "**Análise:** Existe uma forte correlação linear positiva ($R^2 = 0.980$) entre a renda mensal e o gasto mensal. "
        "A cada real ganho a mais, o gasto tende a subir proporcionalmente à taxa de 0.57."
    )

with col2:
    st.subheader("2. Distribuição Salarial")
    st.image("boxplot.png", use_container_width=True)
    st.info(
        "**Análise:** Os departamentos de TI e Vendas possuem medianas salariais consideravelmente maiores que RH e Marketing. "
        "Nota-se também a presença de outliers com salários muito acima do padrão de mercado em TI e Vendas."
    )

with col3:
    st.subheader("3. Faturamento por Canal")
    st.image("pizza.png", use_container_width=True)
    st.info(
        "**Análise:** O canal digital (**Site**) domina o faturamento da empresa com 37.5%, "
        "seguido pela **Loja Física** com 26.7%. Juntos, os canais representam quase 2/3 da receita."
    )

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("4. Evolução Diária de Vendas")
    st.image("linhas.png", use_container_width=True)
    st.info(
        "**Análise:** Ambas as lojas (A e B) apresentam uma clara tendência de crescimento no volume diário de vendas ao longo "
        "do primeiro trimestre, validada pela linha de média móvel de 7 dias."
    )

with col5:
    st.subheader("5. Movimento de Clientes")
    st.image("heatmap.png", use_container_width=True)
    st.info(
        "**Análise:** O mapa de calor destaca o **fim de semana (Sábado e Domingo)** como os períodos de pico de tráfego, "
        "principalmente nos horários das 12:00, 14:00 e 18:00 no Domingo."
    )

with col6:
    st.subheader("6. Frequência de Chamados")
    st.image("frequencia.png", use_container_width=True)
    st.info(
        "**Análise:** O principal gargalo operacional de atendimento está concentrado na resolução de **Dúvidas** (116) e "
        "**Reclamações** (73), superando significativamente os cancelamentos."
    )

st.markdown("---")

col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("7. Vendas por Categoria/Região")
    st.image("barras.png", use_container_width=True) 
    st.info(
        "**Análise:** A **Região Oeste** destaca-se fortemente na venda de Brinquedos e Livros. "
        "Já a **Região Leste** possui seu melhor desempenho na venda de Eletrônicos."
    )

with col8:
    st.subheader("8. Relação Altura x Peso")
    st.image("dispersao.png", use_container_width=True)
    st.info(
        "**Análise:** O gráfico de dispersão mostra uma correlação positiva esperada entre altura e peso. "
        "A distribuição entre os sexos masculino e feminino apresenta uma sobreposição natural na faixa central."
    )

with col9:
    st.subheader("9. Distribuição de Idade")
    st.image("distribuicao.png", use_container_width=True)
    st.info(
        "**Análise:** A base de clientes é majoritariamente **jovem**, apresentando assimetria à direita. "
        "A mediana está em 29 anos, embora a média suba para 33.6 anos devido ao público de maior idade."
    )