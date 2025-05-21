import streamlit as st
import ollama  # Ganti dari google.generativeai ke ollama

# 🔧 Fungsi untuk load CSS dari styles/custom.css
def load_css():
    with open("styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🧠 Fungsi buat merangkum pakai Ollama
def generate_summary(email_text):
    response = ollama.chat(
        model='llama3',
        messages=[{
            "role": "user",
            "content": f"Summarize this email professionally and concisely:\n\n{email_text}"
        }]
    )
    return response['message']['content']


# 🚀 Streamlit UI
st.set_page_config(page_title="Smart Summary Dashboard", page_icon="🧾")

load_css()  # ⬅️ Panggil CSS di awal

st.title("🧾 Smart Summary Dashboard")
st.write("Masukkan isi email harian kamu di bawah, nanti diringkas otomatis pakai AI lokal.")

email_input = st.text_area("Isi Email:", height=300)

if st.button("🔍 Ringkas Sekarang"):
    if email_input.strip() == "":
        st.warning("Masukkan isi email terlebih dahulu.")
    else:
        with st.spinner("Merangkum email..."):
            try:
                summary = generate_summary(email_input)
                st.subheader("📄 Hasil Ringkasan:")
                st.success(summary)
            except Exception as e:
                st.error(f"Gagal ringkas: {e}")