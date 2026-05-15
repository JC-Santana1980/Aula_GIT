import streamlit as st

#Titulo
st.title("Sistema de Biblioteca")

#Criar Lista de Livros
if "livros" not in st.session_state:
     st.session_state.livros = []

#Cadastrar Livros
st.subheader("Cadastrar Livro")
nome_livro = st.text_input("Nome do livro")
autor = st.text_input("Autor")

#Botao Cadastrar
if st.button("Cadastrar Livro"):
   if nome_livro != "" and autor != "":
     livro = {
        "nome": nome_livro,
         "autor": autor,
         "emprestado": False
     }
     st.session_state.livros.append(livro)
     st.success("Livro cadastrado com sucesso!")

#Listar Livros
st.subheader(" Livros Cadastrados")
if len(st.session_state.livros) == 0:
     st.warning("Nenhum livro cadastrado.")
else:
    for i, livro in enumerate(st.session_state.livros):
        st.write(f"### {livro['nome']}")
        st.write(f"Autor: {livro['autor']}")

#Status e Colunas.
        if livro["emprestado"] == False:
             st.success("Disponível")
        else:
             st.error("Emprestado")
        col1, col2 = st.columns(2)

        with col1:
            if st.button(" Emprestar",key=f"emp{i}"):
                st.session_state.livros[i]["emprestado"] = True
                st.rerun()

            #Devolucao    
            if st.button(" Devolver", key=f"dev{i}"):
                st.session_state.livros[i]["emprestado"] = False
                st.rerun()
        st.divider()    
 

