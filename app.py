import streamlit as st

# Configuração da página em modo escuro com um design moderno
st.set_page_config(page_title="Processador de Frases", layout="wide")

# CSS para customização
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stTextInput>div>div>input {
            background-color: #1e1e1e;
            color: white;
            border-radius: 20px;
            padding: 15px;
            font-size: 18px;
            border: 1px solid #444;
            width: 100%;
            text-align: center;
        }
        .stButton>button {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            color: white;
            border-radius: 20px;
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #2575fc, #6a11cb);
            transform: scale(1.05);
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 60vh;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Título centralizado
st.markdown("<div class='title'>📝 Processador de Frases com IA</div>", unsafe_allow_html=True)

# Caixa de entrada centralizada
st.markdown("<div class='container'>", unsafe_allow_html=True)
frase = st.text_input("", placeholder="Digite uma frase para análise...", key="frase")
st.markdown("</div>", unsafe_allow_html=True)

# Botões de ação centralizados
col1, col2, col3 = st.columns([1,2,1])
with col2:
    buscar = st.button("🔍 Analisar")

# Exibição de resultados estilizada
if buscar and frase:
    st.markdown("---")
    st.subheader("📌 Entrada")
    st.write(f"**Frase original:** {frase}")
    
    with st.expander("🔹 Tokenização e Pré-processamento"):
        st.write("(Aqui aparecerá o resultado do módulo de tokenização do Paulo)")
    
    with st.expander("🔹 Análise Sintática"):
        st.write("(Aqui aparecerá a classificação gramatical e estrutura sintática do Mizael)")
    
    with st.expander("🔹 Armazenamento e Recuperação"):
        st.write("(Aqui aparecerá o status do armazenamento do Lancelot)")
