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
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_logo.png",
        width=200
    )

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
    st.image(
        "https://logos-world.net/wp-content/uploads/2020/04/Samsung-Logo.png",
        width=220
    )

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
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg",
        width=150
    )

    st.subheader("🎵 Spotify")

    st.write("""
    Plataforma de streaming de músicas e podcasts
    utilizada por milhões de pessoas no mundo.
    """)

    st.link_button("Acessar Site", "https://www.spotify.com/br/")
