import streamlit as st
import pandas as pd
import plotly.express as px
from generator import generate_synthetic_traffic
from engine import IDSEngine
from database import save_events_to_db, load_events_from_db

st.set_page_config(
    page_title="Network Intrusion Detection System (IDS) SOC",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .metric-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡 Enterprise Network Intrusion Detection System (IDS)")
st.markdown("### Simulated Security Operations Center (SOC) & Threat Analytics Dashboard")

st.sidebar.header("⚙️ Simulation Controls")
num_records = st.sidebar.slider("Synthetic Traffic Records", min_value=100, max_value=2000, value=500, step=100)

if st.sidebar.button("🚀 Generate & Analyze Traffic"):
    with st.spinner("Generating traffic and running IDS inspection..."):
        raw_df = generate_synthetic_traffic(num_records)
        ids_engine = IDSEngine()
        processed_df = ids_engine.process_dataset(raw_df)
        save_events_to_db(processed_df)
    st.sidebar.success("Analysis complete & stored in database!")

df = load_events_from_db()

if df.empty:
    st.warning("⚠️ No security events found. Click **'Generate & Analyze Traffic'** in the sidebar to begin.")
else:
    total_events = len(df)
    intrusions = len(df[df['classification'] == 'POTENTIAL INTRUSION'])
    suspicious = len(df[df['classification'] == 'SUSPICIOUS'])
    critical_alerts = len(df[df['severity'] == 'CRITICAL'])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Flows Analyzed", f"{total_events:,}")
    col2.metric("Potential Intrusions", f"{intrusions:,}", delta_color="inverse")
    col3.metric("Suspicious Flows", f"{suspicious:,}")
    col4.metric("Critical Alerts", f"{critical_alerts:,}", delta_color="inverse")

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Threat Analytics", "🚨 Active Alerts & Triage", "🔍 SOC Investigation", "📑 Incident Report"])

    with tab1:
        st.subheader("Traffic Classification & Severity Breakdown")
        c1, c2 = st.columns(2)
        with c1:
            fig_class = px.pie(df, names='classification', title="Flow Classification Distribution",
                               color_discrete_map={'NORMAL':'#238636', 'SUSPICIOUS':'#d29922', 'POTENTIAL INTRUSION':'#da3633'})
            st.plotly_chart(fig_class, use_container_width=True)
        with c2:
            fig_sev = px.bar(df, x='severity', title="Alert Severity Count",
                             color='severity', color_discrete_map={'INFO':'#8b949e', 'LOW':'#58a6ff', 'MEDIUM':'#d29922', 'HIGH':'#db6d28', 'CRITICAL':'#da3633'})
            st.plotly_chart(fig_sev, use_container_width=True)

        st.subheader("Protocol vs Risk Score Analysis")
        fig_box = px.box(df, x='protocol', y='risk_score', color='classification', title="Risk Score Distribution by Protocol")
        st.plotly_chart(fig_box, use_container_width=True)

    with tab2:
        st.subheader("🚨 Real-Time Security Alerts")
        alert_filter = st.selectbox("Filter by Classification", ["ALL", "POTENTIAL INTRUSION", "SUSPICIOUS", "NORMAL"])
        if alert_filter != "ALL":
            filtered_df = df[df['classification'] == alert_filter]
        else:
            filtered_df = df[df['classification'].isin(['POTENTIAL INTRUSION', 'SUSPICIOUS'])]

        st.dataframe(filtered_df[['timestamp', 'src_ip', 'dst_ip', 'protocol', 'dst_port', 'classification', 'severity', 'risk_score', 'triggered_rules']], use_container_width=True)

    with tab3:
        st.subheader("🔍 SOC Analyst Investigation Workbench")
        selected_ip = st.selectbox("Select Source IP to Investigate", df['src_ip'].unique())
        ip_df = df[df['src_ip'] == selected_ip]
        
        st.markdown(f"**Investigation Dossier for IP:** `{selected_ip}`")
        st.metric("Total Connections from IP", len(ip_df))
        st.metric("Highest Risk Score Observed", ip_df['risk_score'].max())
        
        st.markdown("### Connection Logs for Selected IP")
        st.dataframe(ip_df[['timestamp', 'dst_ip', 'protocol', 'dst_port', 'packet_count', 'byte_count', 'classification', 'triggered_rules']], use_container_width=True)

    with tab4:
        st.subheader("📑 Automated Incident Report Generator")
        st.markdown("Generate an executive-ready incident summary report based on current session alerts.")
        
        if st.button("Generate Executive Summary Report"):
            st.markdown("### 🛡️ SECURITY INCIDENT REPORT - EXECUTIVE SUMMARY")
            st.markdown(f"**Generated At:** {pd.Timestamp.now()}")
            st.markdown(f"**Total Analyzed Packets:** {total_events}")
            st.markdown(f"**Confirmed Intrusions:** {intrusions}")
            st.markdown(f"**Highest Severity Level:** {df['severity'].max()}")
            
            st.markdown("#### Recommended SOC Actions:")
            st.markdown("1. Isolate IP addresses associated with `CRITICAL` severity alerts.")
            st.markdown("2. Review firewall rules blocking ports `4444`, `31337`, and unauthorized SSH access.")
            st.markdown("3. Conduct deep-packet inspection on hosts flagged for data exfiltration patterns.")
            st.success("Incident report successfully compiled.")
