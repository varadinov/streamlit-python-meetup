import streamlit as st
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import tempfile

# Streamlit app title
st.title("Infrastructure Diagram as Code")

# Sidebar inputs
st.sidebar.header("Diagram Configuration")
diagram_name = st.sidebar.text_input("Diagram Name", "My Infrastructure Diagram")
with_lb = st.sidebar.checkbox("Include Load Balancer", value=True)
num_ec2_instances = st.sidebar.slider("Number of EC2 Instances", 1, 5, 3)
with_db = st.sidebar.checkbox("Include Database", value=True)

# Button to generate the diagram
if st.button("Generate Diagram"):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
        with Diagram(diagram_name, show=False, outformat="png", filename=tmpfile.name[:-4]):
            lb = ELB("Load Balancer") if with_lb else None
            ec2_instances = [EC2(f"EC2-{i+1}") for i in range(num_ec2_instances)]
            database = RDS("Database") if with_db else None

            if lb:
                lb >> ec2_instances
            if database:
                ec2_instances >> database

        st.image(tmpfile.name)

st.write("Adjust the configuration in the sidebar and click 'Generate Diagram' to create your custom diagram.")
