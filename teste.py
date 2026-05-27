import streamlit as st

# CONFIG
st.set_page_config(page_title="Empresas Parceiras", layout="wide")

# TÍTULO
st.title("🌐 Empresas Parceiras")

# COLUNAS
col1, col2, col3 = st.columns(3)

# =========================
# TESLA
# =========================
with col1:
    st.image("tesla.png")
    st.subheader("⚡ Tesla")

    st.write("""
    Empresa referência em carros elétricos e inovação tecnológica.
    Atua também em energia sustentável e baterias.
    """)

    st.link_button("Acessar Site", "https://www.tesla.com/")

# =========================
# SAMSUNG
# =========================
with col2:
    st.image("samsung.png")
    st.subheader("📱 Samsung")

    st.write("""
    Multinacional sul-coreana conhecida por smartphones,
    televisores e diversos produtos eletrônicos.
    """)

    st.link_button("Acessar Site", "https://www.samsung.com/br/")

# =========================
# SPOTIFY
# =========================
with col3:
    st.image("spotify.png")
    st.subheader("🎵 Spotify")

    st.write("""
    Plataforma de streaming de músicas e podcasts
    utilizada por milhões de pessoas no mundo.
    """)

    st.link_button("Acessar Site", "https://www.spotify.com/br/")
