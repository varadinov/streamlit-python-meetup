---
titleTemplate: '%s'
selectable: true
colorSchema: light
author: Borislav Varadinov
transition: slide-left
---

# Create Simple Web Apps
## With just few lines of code

---
layout: default
---
# Presentation Video Recording
<Youtube id="n1dOZyrWAbU" width="900" height="400"/>


---
layout: default
---
# About Me
* Names
  - Borislav Varadinov​s
* Company
  - Dell Technologies​
* Job Title​
  - Senior Principal Engineer​



---
layout: default
dragPos:
  multi-knife: 529,114,360,355
  tools: 86,119,335,364
---

# Web Frameworks and Libraries
<div style="display: flex; flex-direction: column; align-items: center;">
    <img  v-drag="'tools'" src="/images/tools.png" style="max-width:85%;"/>
</div>
<div v-click style="display: flex; flex-direction: column; align-items: center;">
    <img v-drag="'multi-knife'"  src="/images/multi-knife.png" style="max-width:85%;"/>
</div>

---
layout: default
---
# What is Streamlit?
* "A faster way to build and share data apps"
* Open-source Python library
* Build interactive web applications
* Designed for data scientists and machine learning engineers
* Quickly turn scripts into shareable web apps
* Can be used for various simple web apps
* 36k stars in GitHub


---
layout: default
---
# Brief History of Streamlit
* Founded by former Google engineers
* First Release in 2019
* 10k stars in 2020
* Acquired by Snowflake in 2022 ($800 million)


---
layout: default
---
# Use Cases
* Reporting Apps
* Interactive Dashboards Apps
* Business Intelligence Apps
* Proof of Concept and Demo Apps
* Simple Interactive Web Apps

---
layout: default
---
# Key Features
* Rapid Development 
* Interactive Widgets
* Data Visualization
* Zero Web Development Knowledge Required

---
layout: default
---
# Why Streamlit?
* Time-Saving
* User-Friendly
* Community 
* Extensibility

---
layout: default
dragPos:
  warning: 418,22,292,82
---

# Hello World
* Install
```bash
pip install streamlit
```

<div v-click>
    <div v-drag="'warning'" class="bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 rounded">
        <p>Always use venv!</p>
    </div>
    <v-drag-arrow pos="419,94,-198,53" color="#EAB308" />
</div>


<br />

* Code
```python
import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app!")
```

<br />

* Run app
```bash
streamlit run app.py
```


---
layout: center
---
# It's showtime!
Part 1

---
layout: default
dragPos:
  widget: 329,88,646,397
---

# Widgets and Elements
* Text
* Data
* Chart
* Input
* Media
* Chat
* Status
* Layout and Containers
* Navigation

<img v-drag="'widget'" src="/images/widgets.png">

---
layout: default
---
# Widgets and Elements Magic
* Backend (Python)
* Communication Layer (WebSockets)
* Frontend (React)


---
layout: default
dragPos:
  heading: 55,97,429,368
  text: 496,96,448,368
---

# Heading and Text
<img v-drag="'heading'" src="/images/heading_elements.png">
<img v-drag="'text'" src="/images/formatted_text_elements.png">

---
layout: default
dragPos:
  widget: 69,90,531,415
---

# Data
<img v-drag="'widget'" src="/images/data_elements.png">

---
layout: default
dragPos:
  widget: 76,82,505,452
---

# Chart
<img v-drag="'widget'" src="/images/chart_elements.png">

---
layout: default
dragPos:
  widget: 81,87,508,422
---

# Advanced Chart
<img v-drag="'widget'" src="/images/advanced_chart_elements.png">

---
layout: default
dragPos:
  widget: 67,86,467,415
---

# Button
<img v-drag="'widget'" src="/images/button_elements.png">

---
layout: default
dragPos:
  widget: 67,93,602,387
---

# Selection
<img v-drag="'widget'" src="/images/selection_elements.png">

---
layout: default
dragPos:
  widget: 60,106,388,249
---

# Numeric
<img v-drag="'widget'" src="/images/numeric_elements.png">

---
layout: default
dragPos:
  widget: 74,101,394,249
---

# Datetime
<img v-drag="'widget'" src="/images/datetime_elements.png">

---
layout: default
dragPos:
  widget: 75,91,349,242
---

# Text input
<img v-drag="'widget'" src="/images/text_input_elements.png">

---
layout: default
dragPos:
  widget: 73,97,527,375
---

# Media
<img v-drag="'widget'" src="/images/media_elements.png">

---
layout: default
dragPos:
  widget: 78,93,499,288
---

# Chat
<img v-drag="'widget'" src="/images/chat_elements.png">

---
layout: default
dragPos:
  widget: 79,83,495,413
---

# Status
<img v-drag="'widget'" src="/images/animated_status_elements.png">

---
layout: default
dragPos:
  widget: 80,82,499,422
---

# Status messages
<img v-drag="'widget'" src="/images/callout_messages_elements.png">

---
layout: default
dragPos:
  widget: 74,90,503,395
---

# Layout and Containers
<img v-drag="'widget'" src="/images/layouts_end_container_elements.png">

---
layout: default
dragPos:
  widget: 75,92,527,282
---

# Navigation
<img v-drag="'widget'" src="/images/navigation_elements.png">

---
layout: default
---
# Components gallery
* Collection of community-built components
* Wide Range of Components (400+)
* Open-Source Contributions
* Ease of Use and Install
* [https://streamlit.io/components](https://streamlit.io/components)

---
layout: default
---
# Script-Based Workflow
* Apps are Python scripts
* Script-as-a-state-machine paradigm
* Scripts execute from top to bottom
* UI elements are rendered in the order they appear
* Streamlit reruns the entire script on user action

---
layout: default
---
# Session Management
* Built in mechanism for session store
* Allows Streamlit to persist data across reruns
* Keeps variable values or user interactions
* Access session state with **st.session_state**


---
layout: default
---
# Caching
* Built in mechanism for caching
* Store the results of time-consuming functions or operations
* Two main caching decorators:
    - **@st.cache_data**: cache functions that load or process data
    - **@st.cache_resource**: cache objects that need to be created only once per session 


---
layout: default
---
# Multipage Applications
* Split content across multiple pages
* Useful for organizing "complex applications"
* Separating distinct sections (e.g., dashboards and reports).
* Each page is stored as separate Python file
* Pages are stored in **pages/** directory
* Main file (app.py) serves as the entry point

```python
my_app/
├── app.py         # Main entry point
└── pages/
    ├── page1.py   # First page
    └── page2.py   # Second page
```

---
layout: default
---
# Custom Components and Extensions
* Extend functionality by integrating custom UI elements
* Useful for embedding specialized widgets
* Provides a Component API
* Typically developed using React or Vue.js 
* Component Hub/Gallery

---
layout: default
---
# Authentication
* Local accounts
    - Implement your own login form
    - External components for login form
* OAuth2 & OpenID Connect
    - External components for OAuth 2 login


---
layout: default
---
# Deployment Options
* Streamlit Community Cloud
* Streamlit in Snowflake
* Docker
* VM or Physical Machine


---
layout: default
---
# Coming Soon
* Native support for writing cookies
* Session based on cookies
* Native authentication support
* Native authentication with OAuth2 & OpenID Connect
* Hooks to add identity information in st.user
* Native redirect 
* Support for custom http endpoints 

---
layout: default
---
# Streamlit vs ...
* Grafana
* PowerBI and Tableau
* Gradio
* Voila
* Panel
* NiceGUI
* More...


---
layout: center
---
# It's showtime 
Part 2


---
layout: default
---
# Why not streamlit?
* Cache and Session State are In-Memory
* Limited HTTP Control
* Performance Limitations for Large Applications
* Limited UI Customization and Layout Flexibility
* Restricted Customization for Mobile Responsiveness
* Limited Support for Real-Time Applications
* UI is not easily testable


---
layout: default
dragPos:
  qr_code: 346,219,246,247
---

# It's feedback time
* Feedback website
  * https://presentation-feedback.streamlit.app/

<img v-drag="'qr_code'" src="/images/qr_code_feedback.png">

---
layout: default
dragPos:
  qr_code: 727,122,212,216
---

# Presentation
* Presentation
  * https://varadinov.github.io/streamlit-python-meetup/
  
* Demos
  * https://github.com/varadinov/streamlit-python-meetup/tree/main/demos

* Feedback app source code
  * https://github.com/varadinov/streamlit-presentation-feedback


<img v-drag="'qr_code'" src="/images/qr_code_presentation.png">

---
layout: center
---
# Q/A and Discussion
