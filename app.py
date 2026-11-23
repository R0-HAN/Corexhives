import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="COREXHIVES | Smart Beehive", page_icon="🐝", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
.stApp{background:#f5f7f2}.block-container{max-width:1200px;padding-top:1.2rem;padding-bottom:2rem}
.brand{background:#173d2b;color:white;padding:22px 26px;border-radius:18px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.brand-name{font-size:30px;font-weight:800;letter-spacing:.5px}.brand-name span{color:#f2bd4b}
.brand-sub{font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#d5e4d7;margin-top:6px}
.top-badge{border:1px solid #75947b;border-radius:30px;padding:8px 12px;font-size:11px;color:#eff7ef}
.hero-title{font-size:27px;font-weight:800;color:#20291f;margin:4px 0}.muted{color:#71806e;font-size:13px}
.demo{background:#fff2d4;color:#805d13;border:1px solid #efd89b;padding:9px 12px;border-radius:9px;font-size:11px;font-weight:800;display:inline-block;margin:8px 0 14px}
.metric-card{background:white;border:1px solid #e6ece2;border-radius:15px;padding:17px 18px;min-height:135px;box-shadow:0 4px 15px #1e37230a}
.metric-label{color:#71806e;font-size:12px;font-weight:700}.metric-value{color:#20291f;font-size:30px;font-weight:800;margin:9px 0 2px}
.metric-note{color:#71806e;font-size:11px}.metric-status{display:inline-block;background:#eaf4e9;color:#2d7040;border-radius:30px;padding:5px 9px;font-size:10px;font-weight:800;margin-top:9px}
.panel-title{font-size:16px;font-weight:800;color:#20291f;margin:4px 0 12px}
.status-row{display:flex;justify-content:space-between;gap:10px;padding:12px 0;border-bottom:1px solid #edf0ea;font-size:13px;color:#354334}
.status-row:last-child{border-bottom:0}.pill{background:#eaf4e9;color:#2d7040;padding:5px 9px;border-radius:30px;font-size:10px;font-weight:800;white-space:nowrap}
.pill-warn{background:#fff1dc;color:#93641a}.panel{background:white;border:1px solid #e6ece2;border-radius:15px;padding:18px;box-shadow:0 4px 15px #1e37230a}
.alert-box{background:white;border:1px solid #e6ece2;border-left:5px solid #efbd4b;border-radius:12px;padding:14px 16px;font-size:12px;line-height:1.55;color:#465044;margin-top:15px}
.footer{text-align:center;color:#879184;font-size:11px;padding:22px 0 5px}
@media(max-width:600px){.block-container{padding-left:.75rem;padding-right:.75rem}.brand-name{font-size:25px}.hero-title{font-size:23px}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="brand"><div><div class="brand-name">COREX<span>HIVES</span> 🐝</div>
<div class="brand-sub">Smart Beehive Health &amp; Swarm Monitoring System</div></div>
<div class="top-badge">● PROJECT DEMONSTRATION</div></div>
""", unsafe_allow_html=True)

left, right = st.columns([3, 1])
with left:
    st.markdown('<div class="hero-title">Hive Monitoring Dashboard</div><div class="muted">A single view of hive environment, weight and acoustic activity.</div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="demo">SAMPLE DATA · NOT LIVE SENSORS</div>', unsafe_allow_html=True)

cols = st.columns(4)
cards = [
    ("🌡️", "Temperature", "34.2", "°C", "Illustrative hive reading", "DEMO NORMAL"),
    ("💧", "Humidity", "62", "%", "Relative humidity", "DEMO NORMAL"),
    ("⚖️", "Hive weight", "28.6", "kg", "Illustrative weight value", "DEMO STABLE"),
    ("🐝", "Acoustic activity", "Active", "", "Illustrative sound status", "SAMPLE STATUS"),
]
for col, (icon, label, value, unit, note, status) in zip(cols, cards):
    with col:
        st.markdown(f'<div class="metric-card"><div class="metric-label">{icon} &nbsp; {label}</div><div class="metric-value">{value} <span style="font-size:14px;color:#71806e;font-weight:500">{unit}</span></div><div class="metric-note">{note}</div><div class="metric-status">{status}</div></div>', unsafe_allow_html=True)

st.write("")
chart_col, health_col = st.columns([1.55, 1], gap="medium")
with chart_col:
    st.markdown('<div class="panel-title">Environmental trend</div>', unsafe_allow_html=True)
    trend = pd.DataFrame({"Time":["08:00","09:00","10:00","11:00","12:00","13:00","14:00"],
                          "Temperature (°C)":[32.0,32.8,33.1,33.7,34.0,33.8,34.2],
                          "Humidity (%)":[59,60,58,61,60,63,62]})
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trend["Time"], y=trend["Temperature (°C)"], name="Temperature", mode="lines+markers", line=dict(color="#d99a2b",width=3)))
    fig.add_trace(go.Scatter(x=trend["Time"], y=trend["Humidity (%)"], name="Humidity", mode="lines+markers", line=dict(color="#4b8b68",width=3), yaxis="y2"))
    fig.update_layout(height=300, margin=dict(l=8,r=8,t=22,b=8), paper_bgcolor="white", plot_bgcolor="white",
                      legend=dict(orientation="h",y=1.12,x=0), font=dict(color="#53604f",size=11),
                      xaxis=dict(title="",showgrid=False), yaxis=dict(title="Temperature (°C)",gridcolor="#edf0ea",zeroline=False),
                      yaxis2=dict(title="Humidity (%)",overlaying="y",side="right",showgrid=False))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

with health_col:
    st.markdown('<div class="panel-title">Hive health indicators</div>', unsafe_allow_html=True)
    for label, value, warn in [("Temperature condition","NORMAL",False),("Humidity condition","NORMAL",False),
                               ("Weight variation","STABLE",False),("Acoustic activity","ACTIVE",False),
                               ("Swarm indication","NOT CONFIRMED",True)]:
        cls = "pill pill-warn" if warn else "pill"
        st.markdown(f'<div class="status-row"><span>{label}</span><span class="{cls}">{value}</span></div>', unsafe_allow_html=True)

st.write("")
a, b = st.columns(2, gap="medium")
with a:
    st.markdown('<div class="panel-title">System architecture</div><div class="panel">', unsafe_allow_html=True)
    for label, tag in [("1. Hive sensors & microphone","INPUT"),("2. ESP32 / controller","COLLECTION"),
                       ("3. Audio processing (FFT + features)","PROCESSING"),("4. ML classification & logic","ANALYSIS"),
                       ("5. Web dashboard","DISPLAY")]:
        st.markdown(f'<div class="status-row"><span>{label}</span><span class="pill">{tag}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with b:
    st.markdown('<div class="panel-title">Monitoring &amp; swarm alert</div><div class="panel" style="min-height:190px"><div style="font-size:30px">⚠️</div><b>No swarm event confirmed</b><p class="muted">This is a demonstration status. In the completed system, possible swarm indicators may be assessed using acoustic patterns together with hive-weight changes. Field validation is required before treating an alert as a reliable prediction.</p></div>', unsafe_allow_html=True)

st.markdown("""
<div class="alert-box"><b>Demonstration notice:</b> All displayed measurements, trends and statuses are sample values
for interface demonstration. They are not live sensor readings and do not represent a validated swarm prediction.
Connect actual sensor and model outputs before presenting this as a live monitoring system.</div>
""", unsafe_allow_html=True)
st.markdown(f'<div class="footer">COREXHIVES · Smart Beehive Health &amp; Swarm Monitoring · Updated {datetime.now().strftime("%d %b %Y, %H:%M")}</div>', unsafe_allow_html=True)
