import streamlit as st
from database.vector_store import VectorStore


# Initialize VectorStore
vector_store = VectorStore()


# Streamlit app title
st.title("Vendor Search Application")

# Text input for user query
query = st.text_input("Enter your search query:")

if query:
    # Perform search
    results = vector_store.search(query_text=query, limit=5, distance_threshold=0.5)

    # Display results
    if not results.empty:
        st.subheader("Search Results:")
        for index, row in results.iterrows():
            st.write(f"**Vendor Company Name:** {row['vendor_company_name']}")
            st.write(f"**Content:** {row['content']}")
            st.write(f"**Email:** {row['email']}")
            st.write(f"**Distance:** {row['distance']:.4f}")
            st.write("---")
    else:
        st.write("No relevant results found.")
