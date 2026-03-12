import streamlit as st
#=================
#  DADOS
#=================

#Pode fazer uma lista igual a de baixo ou pode exportar de um excel

custo_setor = {
    "Solda": 59.15,
    "Prensa":30.08,
    "Frisadeira":57.03,
    "Serviço Manual":11.91,
    "Torno":13.69,
    "Usinagem":50.23,
    "Furadeira":21.34,
    "Lixadeira":40.04,
    "Pintura":27.14
}

#===================
# LAYOUT DA PAGINA
#===================
st.title("Calculadora de Retrabalho")
st.markdown("---")

col1, col2 = st.columns(2)

#seleciona o setor que deseja
with col1:
    setor = st.selectbox("Selecione o Setor: ", list(custo_setor.keys()))
#Coloca quanto tempo levou o retrabalho
with col2:
    temp_min = st.number_input("Tempo gasto(em minuttos): ", min_value=0, step=1)

# custo hora baseado no setor selecionado
custo_hora = custo_setor[setor]
#Faz a regra de 3 com o custo hora
custo_final = (temp_min * custo_hora)/60

#======================
# MOSTRA O RESULTADO
#======================
st.markdown("---")
if temp_min > 0:
    st.subheader(f"Resultado para {setor}:")
    st.metric(label="Custo Total do Retrabalho", value=f"R$ {custo_final:.2f}")
    st.info(f"Custo base do setor: R$ {custo_hora:.2f} / hora")
else:
    st.write("Aguardando a inserção do tempo para calcular...")


# Para você rodar o codigo abra o terminal e digite:
# streamlit run app.py
# Ou subtitua o "app.py" pelo nome do seu arquivo 

