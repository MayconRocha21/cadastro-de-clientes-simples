import streamlit as st


st.title("Cadastro de clientes")


nome = st.text_input("Nome do cliente", key="nome")

endereco = st.text_input("Endereço: ", key="endereco")

data_nasc = st.date_input("Data Nascimento: ", key="dt_nasc")

tipo = st.selectbox("Tipo de cliente", ["Pessoa física", "Pessoa jurídica"], key="tipo")


cadastro = st.button("Cadastrar")


print(type(data_nasc))


if cadastro:

    with open("clientes.csv", "a") as arquivo:

        arquivo.write(f"{nome};{endereco};{data_nasc}\n")


    st.success("Cliente cadastrado com sucesso!", icon=" ")