import streamlit as st

# Title
st.title("Streamlit Demo: Displaying Information")

# Header
st.header("1. Markdown Display")

# Markdown
st.markdown("""
**Markdown Example**:
- **Bold Text**
- *Italic Text*
- Inline code: `print("Hello, Streamlit!")`
""")

# Subheader
st.subheader("2. Code Display")

# Code block
code_example = """
def greet(name):
    return f"Hello, {name}!"

print(greet("Streamlit"))
"""
st.code(code_example, language='python')

st.divider()

# Subheader
st.subheader("3. Display JSON Data")

# JSON example
json_example = {
    "name": "Streamlit",
    "version": "1.0",
    "features": ["Markdown", "Code", "JSON Display"]
}
st.json(json_example)

st.divider()

# Subheader
st.subheader("4. Write Method Example")

st.write("The `st.write()` method supports multiple formats:")
st.write("Here's a **string** example.")
st.write(["This is", "a list", "of strings"])
st.write({"This is": "a dictionary", "with keys": "and values"})

st.divider()

# Subheader
st.subheader("5. LaTeX and Math Equations")

# LaTeX display
st.latex(r"""
\int_a^b f(x)\,dx = F(b) - F(a)
""")

# Footer
st.info("Explore Streamlit's documentation for more amazing features!")
