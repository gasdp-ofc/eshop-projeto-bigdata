import streamlit as st
from pymongo import MongoClient
import pandas as pd

st.title("🛍️ E-Shop Brasil - Gestão de Dados com MongoDB")

client = MongoClient("mongodb://mongo:27017/")
db = client["eshop"]
collection = db["clientes"]

st.header("📥 Inserir novo cliente")
nome = st.text_input("Nome")
email = st.text_input("Email")

if st.button("Inserir"):
    if nome and email:
        collection.insert_one({"nome": nome, "email": email})
        st.success("✅ Cliente inserido com sucesso!")
    else:
        st.warning("⚠️ Preencha todos os campos!")

st.header("📄 Clientes cadastrados")
dados = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(dados)
st.dataframe(df)
