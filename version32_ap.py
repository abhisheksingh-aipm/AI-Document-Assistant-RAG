import streamlit as st
import time

from RAGversion32 import (
    process_pdf,
    chunk_text,
    create_embeddings,
    store_embeddings,
    ask_question,
    generate_document_hash,
    document_exists,
    get_uploaded_documents
)

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# Session State
# =====================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =====================================
# Title
# =====================================

st.title("🤖 AI Document Assistant")

st.write("Welcome to your first AI Product!")

st.write("Upload one or more PDFs and ask questions.")

# =====================================
# Sidebar
# =====================================

st.sidebar.title("📚 Knowledge Base")

documents = get_uploaded_documents()

st.sidebar.write(f"Total PDFs: {len(documents)}")

for doc in documents.values():

    st.sidebar.write(f"📄 {doc['name']}")

    st.sidebar.caption(f"{doc['chunks']} Chunks")

# =====================================
# Upload PDFs
# =====================================

uploaded_files = st.file_uploader(
    "Upload your PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        st.divider()

        st.subheader(f"📄 {uploaded_file.name}")

        document_hash = generate_document_hash(
            uploaded_file
        )

        if document_exists(document_hash):

            st.success("✅ Already Exists")

        else:

            st.info("📄 New PDF")

            full_text = process_pdf(uploaded_file)

            chunks = chunk_text(full_text)

            embeddings = create_embeddings(chunks)

            store_embeddings(
                document_hash,
                uploaded_file.name,
                chunks,
                embeddings
            )

            st.success("✅ Stored Successfully")

    st.divider()

    question = st.text_input(
        "Ask a Question"
    )

    if question:

        with st.spinner("🤖 Gemini is thinking..."):

            answer, sources = ask_question(question)

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        st.success("✅ Answer Generated")

        st.write("## Answer")

        placeholder = st.empty()

        stream_text = ""

        for word in answer.split():

            stream_text += word + " "

            placeholder.markdown(stream_text)

            time.sleep(0.02)

        # =====================================
        # Sources
        # =====================================

        st.divider()

        st.subheader("📚 Sources Used")

        for i, (score, document, metadata) in enumerate(sources):

            with st.expander(
                f"Source {i+1} | Score: {score:.3f}"
            ):

                st.write(
                    f"📄 Document: {metadata['document_name']}"
                )

                st.write(
                    f"📑 Chunk: {metadata['chunk_number']}"
                )

                st.write(document)

        # =====================================
        # Chat History
        # =====================================

        st.divider()

        st.subheader("💬 Chat History")

        for chat in st.session_state.chat_history:

            st.chat_message("user").write(
                chat["question"]
            )

            st.chat_message("assistant").write(
                chat["answer"]
            )

else:

    st.info("👆 Please upload one or more PDFs.")