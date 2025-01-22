import streamlit as st
import psutil
from datetime import datetime

st.set_page_config(layout='wide')
def get_process_data():
    processes = []

    for process in psutil.process_iter(['pid', 'username', 'cpu_percent', 'memory_percent', 'name']):
        try:
            processes.append({
                'pid': process.info['pid'],
                'cpu_percent': round(process.info['cpu_percent'] / psutil.cpu_count(), 2) * 100,
                'memory_percent': round(process.info['memory_percent'], 2),
                'username': process.info['username'],
                'name': process.info['name'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle processes that might have ended or are inaccessible
            continue

    return processes

@st.fragment(run_every='5s')
def dynamic_data_display():
    data = get_process_data()
    st.write(f"Data refreshed at: {datetime.now().strftime('%H:%M:%S')}")
    st.dataframe(data, use_container_width=True, height=920)

st.title("Dynamic Process Statistics")
st.markdown("This dashboard refreshes its data every 5 seconds.")
dynamic_data_display()


