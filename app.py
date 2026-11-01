import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="BizIntel AI | Business Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# BizIntel AI - Professional Theme
st.markdown("""
<style>
/* Chart headings */
.stMainBlockContainer h3 {
    color: #1e293b !important;
    font-weight: 700 !important;
    margin-bottom: 0.75rem !important;
}

/* Spacing around charts */
div[data-testid="stVegaLiteChart"],
div[data-testid="stArrowVegaLiteChart"],
div[data-testid="stPyplotChart"] {
    margin-top: 8px !important;
    margin-bottom: 20px !important;
}
/* Professional chart containers */
div[data-testid="stVegaLiteChart"],
div[data-testid="stArrowVegaLiteChart"],
div[data-testid="stPyplotChart"] {
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 12px !important;
    padding: 12px !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04) !important;
}

/* Chart section spacing */
.stMainBlockContainer h2 {
    margin-top: 1.5rem !important;
    margin-bottom: 0.8rem !important;
}
/* Main dashboard background */
.stApp {
    background-color: #f5f7fb !important;
}

/* Keep the sidebar clean */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}

/* Keep KPI cards blue */
div[data-testid="stMetric"] > div {
    background-color: #eaf2ff !important;
}
/* Main content spacing */
.stMainBlockContainer {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Stronger heading hierarchy */
.stMainBlockContainer h1 {
    font-size: 2.35rem !important;
    font-weight: 800 !important;
    line-height: 1.25 !important;
    margin-bottom: 0.5rem !important;
}

.stMainBlockContainer h2 {
    font-size: 1.65rem !important;
    font-weight: 750 !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.8rem !important;
}

.stMainBlockContainer h3 {
    font-size: 1.25rem !important;
    font-weight: 700 !important;
}

/* Enhanced metric cards */
div[data-testid="stMetric"] {
    background: #eaf2ff !important;
    background-color: #eaf2ff  !important;
    border: 1px solid rgba(79, 139, 249, 0.55) !important;
    border-radius: 14px !important;
    padding: 20px 22px !important;
    min-height: 115px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
}

div[data-testid="stMetricLabel"] {
    font-size: 14px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricValue"] {
    font-size: 28px !important;
    font-weight: 800 !important;
}

div[data-testid="stMetricDelta"] {
    font-size: 13px !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton button,
.stDownloadButton button {
    border-radius: 9px !important;
    font-weight: 650 !important;
    min-height: 40px;
}

/* Tables */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 10px;
}

/* Sidebar spacing */
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
    font-size: 1.6rem !important;
}

[data-testid="stSidebar"] hr {
    margin: 1rem 0 !important;
}

/* Consistent section spacing */
.stMainBlockContainer div[data-testid="stVerticalBlock"] {
    gap: 1rem;
}
</style>
""", unsafe_allow_html=True)
# Professional sidebar navigation
with st.sidebar:
    st.markdown("# 📊 BizIntel AI")
    st.caption("Business Intelligence Platform")
    st.divider()

    st.subheader("🧭 Dashboard Guide")

    st.markdown("""
    - 📈 Business Overview
    - 🔎 Business Insights
    - 🔮 Revenue Forecasting
    - 🚨 Anomaly Detection
    - 🎯 Business Recommendations
    - 📥 Reports & Downloads
    """)

    st.divider()

    st.subheader("🛠️ Project Features")

    st.markdown("""
    - CSV data upload
    - Interactive data filters
    - Machine learning forecasting
    - Unusual-value detection
    - Excel and CSV exports
    """)

    st.divider()

    st.caption("Built with Python, Streamlit, Pandas and Scikit-learn")
# Professional dashboard header
st.markdown("""
    <div style="padding: 10px 0 20px 0;">
        <h1 style="margin-bottom: 0;">📊 BizIntel AI</h1>
        <p style="font-size: 17px; color: #808495;">
            AI-Powered Business Intelligence & Analytics Dashboard
        </p>
    </div>
    <hr>
""", unsafe_allow_html=True)

st.title("📊 BizIntel AI")
st.subheader("AI-Powered Business Intelligence Dashboard")
st.write("Analyze company revenue and growth using your business data.")

# Sidebar CSV upload
st.sidebar.title("⚙️ Dashboard Settings")
st.sidebar.header("📂 Upload Your Data")

uploaded_file = st.sidebar.file_uploader(
    "Upload business CSV",
    type=["csv"]
)

# Sample data
sample_data = pd.DataFrame({
    "Company": ["TechNova", "DataSphere", "CloudMatrix",
                "InnovateX", "FutureSoft"],
    "Revenue": [125000, 98000, 156000, 87000, 142000],
    "Growth": [12.5, 8.2, 18.4, 6.5, 15.1]
})

# Read uploaded data or use sample data
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("CSV uploaded successfully!")
    except Exception as e:
        st.error(f"Unable to read CSV: {e}")
        st.stop()
else:
    df = sample_data.copy()
    st.info("Showing sample data. Upload a CSV from the sidebar.")

# Validate columns
df.columns = df.columns.str.strip()
required = ["Company", "Revenue", "Growth"]

missing = [col for col in required if col not in df.columns]

if missing:
    st.error(
        f"Missing columns: {', '.join(missing)}. "
        "Required columns: Company, Revenue, Growth."
    )
    st.stop()

# Clean data
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
df["Growth"] = pd.to_numeric(df["Growth"], errors="coerce")
df = df.dropna(subset=required)

if df.empty:
    st.warning("No valid data found in the CSV.")
    st.stop()

st.divider()

# Dashboard metrics
total_revenue = df["Revenue"].sum()
average_growth = df["Growth"].mean()
company_count = df["Company"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("📈 Average Growth", f"{average_growth:.2f}%")
col3.metric("🏢 Companies", f"{company_count}")

st.divider()

# Company data table
st.subheader("🏢 Company Performance")
st.dataframe(df, use_container_width=True)

# Revenue chart
st.subheader("💰 Revenue by Company")
revenue_chart = df.set_index("Company")[["Revenue"]]
st.bar_chart(revenue_chart)

# Growth chart
st.subheader("📈 Company Growth")
growth_chart = df.set_index("Company")[["Growth"]]
st.bar_chart(growth_chart)

# --------------------------------------------------
# BUSINESS INTELLIGENCE AND AUTOMATED INSIGHTS
# --------------------------------------------------

st.divider()
st.header("🧠 Business Intelligence Insights")

# Find the company with the highest revenue
top_revenue_row = df.loc[df["Revenue"].idxmax()]
top_growth_row = df.loc[df["Growth"].idxmax()]

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Revenue Leader")
    st.metric(
        label=str(top_revenue_row["Company"]),
        value=f"₹{top_revenue_row['Revenue']:,.0f}",
        help="Company with the highest revenue in the dataset"
    )

with col2:
    st.subheader("🚀 Growth Leader")
    st.metric(
        label=str(top_growth_row["Company"]),
        value=f"{top_growth_row['Growth']:.2f}%",
        help="Company with the highest growth rate"
    )

# Classify companies by growth
def classify_growth(growth):
    if growth >= 15:
        return "High Growth"
    elif growth >= 8:
        return "Moderate Growth"
    else:
        return "Low Growth"

insights_df = df.copy()
insights_df["Performance"] = insights_df["Growth"].apply(
    classify_growth
)

st.subheader("📋 Company Performance Analysis")

st.dataframe(
    insights_df[
        ["Company", "Revenue", "Growth", "Performance"]
    ].sort_values("Revenue", ascending=False),
    use_container_width=True
)

# Automatically generate observations
st.subheader("💡 Automated Business Insights")

high_growth_count = (
    insights_df["Performance"] == "High Growth"
).sum()

low_growth_count = (
    insights_df["Performance"] == "Low Growth"
).sum()

st.write(
    f"📊 **{top_revenue_row['Company']}** has the highest "
    f"revenue at ₹{top_revenue_row['Revenue']:,.0f}."
)

st.write(
    f"📈 **{top_growth_row['Company']}** leads in growth "
    f"at {top_growth_row['Growth']:.2f}%."
)

st.write(
    f"🚀 {high_growth_count} companies are classified as "
    "high growth (15% or more)."
)

st.write(
    f"⚠️ {low_growth_count} companies are classified as "
    "low growth (below 8%). Consider reviewing their "
    "business performance."
)

st.caption(
    "Growth categories use predefined rules. These insights "
    "are generated from the uploaded data, not an external AI model."
)

# --------------------------------------------------
# STAGE 3 - MACHINE LEARNING REVENUE FORECASTING
# --------------------------------------------------

from sklearn.linear_model import LinearRegression
import numpy as np

st.divider()
st.header("🔮 Machine Learning Revenue Forecasting")

st.write(
    "Upload historical monthly revenue data to train a "
    "Linear Regression model and estimate future revenue."
)

history_file = st.file_uploader(
    "Upload historical revenue CSV",
    type=["csv"],
    key="historical_revenue_upload",
    help="Required columns: Company, Period, Revenue"
)

st.info(
    "Your historical CSV must contain Company, Period, and Revenue. "
    "Period should contain dates such as 2026-01 or 2026-02."
)

if history_file is not None:
    try:
        history_df = pd.read_csv(history_file)
        history_df.columns = history_df.columns.str.strip()

        required_history = ["Company", "Period", "Revenue"]
        missing_history = [
            col for col in required_history
            if col not in history_df.columns
        ]

        if missing_history:
            st.error(
                "Missing columns: "
                + ", ".join(missing_history)
            )
        else:
            history_df = history_df[required_history].copy()

            history_df["Company"] = (
                history_df["Company"].astype("string").str.strip()
            )
            history_df["Period"] = pd.to_datetime(
                history_df["Period"], errors="coerce"
            )
            history_df["Revenue"] = pd.to_numeric(
                history_df["Revenue"], errors="coerce"
            )

            history_df = history_df.dropna(
                subset=required_history
            )

            history_df = history_df[
                (history_df["Company"].str.len() > 0)
                & (history_df["Revenue"] >= 0)
            ].copy()

            # Convert dates to monthly periods
            history_df["Period"] = (
                history_df["Period"]
                .dt.to_period("M")
                .dt.to_timestamp()
            )

            # Combine duplicate company-month records
            history_df = (
                history_df.groupby(
                    ["Company", "Period"], as_index=False
                )["Revenue"].sum()
            )

            if history_df.empty:
                st.warning(
                    "No valid historical records were found."
                )
            else:
                companies = sorted(
                    history_df["Company"].unique().tolist()
                )

                selected_company = st.selectbox(
                    "Select company to forecast",
                    companies,
                    key="forecast_company"
                )

                forecast_months = st.slider(
                    "Forecast horizon (months)",
                    min_value=1,
                    max_value=12,
                    value=3
                )

                company_history = (
                    history_df[
                        history_df["Company"] == selected_company
                    ]
                    .sort_values("Period")
                    .copy()
                )

                st.subheader("📈 Historical Revenue")
                st.line_chart(
                    company_history.set_index("Period")[["Revenue"]]
                )

                if len(company_history) < 3:
                    st.warning(
                        "At least 3 distinct months of historical "
                        "revenue are required for this demo. "
                        "More historical data generally improves "
                        "the reliability of a forecast."
                    )
                elif st.button(
                    "🚀 Generate Revenue Forecast",
                    key="generate_revenue_forecast"
                ):
                    # Encode months as sequential numeric values
                    month_numbers = (
                        company_history["Period"].dt.year * 12
                        + company_history["Period"].dt.month
                    )

                    X = month_numbers.to_numpy().reshape(-1, 1)
                    y = company_history["Revenue"].to_numpy()

                    model = LinearRegression()
                    model.fit(X, y)

                    last_period = company_history["Period"].max()

                    future_dates = pd.date_range(
                        start=last_period + pd.offsets.MonthBegin(1),
                        periods=forecast_months,
                        freq="MS"
                    )

                    future_month_numbers = (
                        future_dates.year * 12
                        + future_dates.month
                    ).to_numpy().reshape(-1, 1)

                    predictions = model.predict(
                        future_month_numbers
                    )

                    # Revenue cannot be negative
                    predictions = np.maximum(predictions, 0)

                    forecast_df = pd.DataFrame({
                        "Period": future_dates,
                        "Forecast Revenue": predictions.round(2)
                    })

                    st.subheader("🔮 Forecast Results")

                    st.dataframe(
                        forecast_df,
                        use_container_width=True,
                        hide_index=True
                    )

                    st.metric(
                        "Next Month Estimated Revenue",
                        f"₹{predictions[0]:,.2f}"
                    )

                    # Display historical and forecast values
                    historical_plot = company_history[
                        ["Period", "Revenue"]
                    ].rename(columns={
                        "Revenue": "Historical Revenue"
                    })

                    historical_plot["Forecast Revenue"] = np.nan

                    future_plot = forecast_df.rename(columns={
                        "Forecast Revenue": "Forecast Revenue"
                    })
                    future_plot["Historical Revenue"] = np.nan

                    combined_plot = pd.concat(
                        [
                            historical_plot[
                                ["Period", "Historical Revenue",
                                 "Forecast Revenue"]
                            ],
                            future_plot[
                                ["Period", "Historical Revenue",
                                 "Forecast Revenue"]
                            ]
                        ],
                        ignore_index=True
                    ).set_index("Period")

                    st.line_chart(combined_plot)

                    st.caption(
                        "This is a Linear Regression baseline, not a "
                        "guaranteed prediction. It extrapolates the "
                        "historical trend and does not account for "
                        "seasonality or unexpected business changes."
                    )

    except Exception as e:
        st.error(f"Unable to process historical data: {e}")

        # --------------------------------------------------
# STAGE 4 - BUSINESS ANOMALY DETECTION
# --------------------------------------------------

from sklearn.ensemble import IsolationForest

st.divider()
st.header("🔍 Business Anomaly Detection")

st.write(
    "Identify potentially unusual company revenue and growth "
    "patterns using a machine learning algorithm."
)

if len(df) < 5:
    st.info(
        "Upload at least 5 valid company records to run "
        "the anomaly detection demonstration."
    )
else:
    anomaly_df = df.copy()

    features = anomaly_df[["Revenue", "Growth"]].copy()

    detector = IsolationForest(
        n_estimators=100,
        contamination="auto",
        random_state=42
    )

    predictions = detector.fit_predict(features)

    anomaly_df["Anomaly Status"] = [
        "⚠️ Review Recommended" if value == -1
        else "✅ Within Detected Pattern"
        for value in predictions
    ]

    anomaly_count = int((predictions == -1).sum())
    normal_count = int((predictions == 1).sum())

    col1, col2 = st.columns(2)

    col1.metric(
        "⚠️ Records Flagged",
        anomaly_count
    )

    col2.metric(
        "✅ Other Records",
        normal_count
    )

    st.subheader("📋 Anomaly Detection Results")

    st.dataframe(
        anomaly_df[
            ["Company", "Revenue", "Growth", "Anomaly Status"]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="⬇️ Download Anomaly Report",
        data=anomaly_df.to_csv(index=False).encode("utf-8"),
        file_name="bizintel_anomaly_report.csv",
        mime="text/csv",
        key="download_anomaly_report"
    )

    st.caption(
        "An anomaly is an unusual pattern relative to the "
        "uploaded dataset. A flagged record is not necessarily "
        "an error or fraud. Review the underlying business data "
        "before taking action."
    )

    # --------------------------------------------------
# STAGE 5 - INTERACTIVE FILTERS
# AND EXCEL BUSINESS REPORT
# --------------------------------------------------

from io import BytesIO

st.divider()
st.header("🎛️ Interactive Business Analysis")

st.write(
    "Filter your business data and generate a downloadable "
    "Excel report containing company performance and summary metrics."
)

# Work on a separate copy so existing features remain unchanged
filter_df = df.copy()

# Company filter
company_options = sorted(
    filter_df["Company"].dropna().unique().tolist()
)

selected_companies = st.multiselect(
    "Select companies",
    options=company_options,
    default=company_options,
    key="stage5_companies"
)

# Revenue range filter
revenue_min = float(filter_df["Revenue"].min())
revenue_max = float(filter_df["Revenue"].max())

if revenue_min == revenue_max:
    revenue_min -= 1
    revenue_max += 1

selected_revenue = st.slider(
    "Filter by revenue",
    min_value=revenue_min,
    max_value=revenue_max,
    value=(revenue_min, revenue_max),
    key="stage5_revenue"
)

# Growth range filter
growth_min = float(filter_df["Growth"].min())
growth_max = float(filter_df["Growth"].max())

if growth_min == growth_max:
    growth_min -= 1
    growth_max += 1

selected_growth = st.slider(
    "Filter by growth (%)",
    min_value=growth_min,
    max_value=growth_max,
    value=(growth_min, growth_max),
    key="stage5_growth"
)

# Apply filters
filtered_df = filter_df[
    filter_df["Company"].isin(selected_companies)
    & filter_df["Revenue"].between(
        selected_revenue[0], selected_revenue[1]
    )
    & filter_df["Growth"].between(
        selected_growth[0], selected_growth[1]
    )
].copy()

st.subheader("📊 Filtered Business Results")

result_col1, result_col2, result_col3 = st.columns(3)

result_col1.metric(
    "Matching Companies",
    filtered_df["Company"].nunique()
)

result_col2.metric(
    "Filtered Revenue",
    f"₹{filtered_df['Revenue'].sum():,.0f}"
)

if filtered_df.empty:
    result_col3.metric("Average Growth", "N/A")
else:
    result_col3.metric(
        "Average Growth",
        f"{filtered_df['Growth'].mean():.2f}%"
    )

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# EXCEL BUSINESS REPORT
# --------------------------------------------------

st.divider()
st.header("📑 Download Excel Business Report")

st.write(
    "Export the currently filtered records into an Excel workbook "
    "with company rankings and a business summary."
)

if filtered_df.empty:
    st.warning(
        "No records match your filters. Adjust the filters "
        "to generate an Excel report."
    )
else:
    report_df = filtered_df.copy()

    # Classify growth performance
    report_df["Performance"] = report_df["Growth"].apply(
        lambda growth:
        "High Growth" if growth >= 15
        else "Moderate Growth" if growth >= 8
        else "Low Growth"
    )

    # Rank companies by revenue
    report_df["Revenue Rank"] = (
        report_df["Revenue"]
        .rank(method="dense", ascending=False)
        .astype(int)
    )

    report_df = report_df.sort_values(
        "Revenue", ascending=False
    )

    # Build summary metrics
    summary_df = pd.DataFrame({
        "Metric": [
            "Number of Companies",
            "Total Revenue",
            "Average Revenue",
            "Average Growth (%)",
            "Highest Revenue Company",
            "Highest Revenue"
        ],
        "Value": [
            int(report_df["Company"].nunique()),
            float(report_df["Revenue"].sum()),
            float(report_df["Revenue"].mean()),
            float(report_df["Growth"].mean()),
            str(
                report_df.loc[
                    report_df["Revenue"].idxmax(), "Company"
                ]
            ),
            float(report_df["Revenue"].max())
        ]
    })

    # Create Excel workbook in memory
    excel_buffer = BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl"
    ) as writer:
        report_df.to_excel(
            writer,
            sheet_name="Company Analysis",
            index=False
        )

        summary_df.to_excel(
            writer,
            sheet_name="Business Summary",
            index=False
        )

    excel_buffer.seek(0)

    st.download_button(
        label="⬇️ Download Excel Business Report",
        data=excel_buffer.getvalue(),
        file_name="BizIntel_AI_Business_Report.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        key="stage5_excel_download"
    )

    st.success(
        "Your Excel report is ready to download!"
    )

# Download cleaned data
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Business Data",
    data=csv_data,
    file_name="bizintel_business_data.csv",
    mime="text/csv"
)

st.divider()
st.caption("BizIntel AI | Business Intelligence Dashboard")

# --------------------------------------------------
# STAGE 6 - AI-POWERED BUSINESS RECOMMENDATIONS
# --------------------------------------------------

st.divider()
st.header("🤖 AI-Powered Business Recommendations")

st.write(
    "Get data-driven recommendations based on company revenue "
    "and growth performance."
)

# Analyze the full uploaded business dataset
recommendation_df = df.copy()

if recommendation_df.empty:
    st.warning("Upload valid business data to generate recommendations.")

else:
    total_revenue = recommendation_df["Revenue"].sum()
    average_revenue = recommendation_df["Revenue"].mean()
    average_growth = recommendation_df["Growth"].mean()

    st.subheader("📊 Business Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    col2.metric("Average Revenue", f"₹{average_revenue:,.0f}")
    col3.metric("Average Growth", f"{average_growth:.2f}%")

    st.subheader("💡 Recommended Actions")

    recommendations = []

    # Revenue leader
    top_company = recommendation_df.loc[
        recommendation_df["Revenue"].idxmax()
    ]

    recommendations.append({
        "Priority": "Information",
        "Company": str(top_company["Company"]),
        "Finding": "Highest revenue in the dataset",
        "Recommendation": (
            "Review the factors contributing to this company's "
            "revenue and identify practices worth replicating."
        )
    })

    # Low-growth companies
    low_growth = recommendation_df[
        recommendation_df["Growth"] < 8
    ]

    for _, company in low_growth.iterrows():
        recommendations.append({
            "Priority": "High",
            "Company": str(company["Company"]),
            "Finding": f"Low growth: {company['Growth']:.2f}%",
            "Recommendation": (
                "Review sales trends, customer retention, pricing, "
                "and marketing performance to identify opportunities."
            )
        })

    # High-growth companies
    high_growth = recommendation_df[
        recommendation_df["Growth"] >= 15
    ]

    for _, company in high_growth.iterrows():
        recommendations.append({
            "Priority": "Positive",
            "Company": str(company["Company"]),
            "Finding": f"High growth: {company['Growth']:.2f}%",
            "Recommendation": (
                "Investigate the drivers of growth and assess "
                "whether the strategy can be scaled sustainably."
            )
        })

    # Revenue below dataset average
    below_average = recommendation_df[
        recommendation_df["Revenue"] < average_revenue
    ]

    for _, company in below_average.iterrows():
        recommendations.append({
            "Priority": "Review",
            "Company": str(company["Company"]),
            "Finding": "Revenue below dataset average",
            "Recommendation": (
                "Compare revenue trends and business conditions "
                "before deciding whether corrective action is needed."
            )
        })

    # General growth insight
    if average_growth < 8:
        recommendations.append({
            "Priority": "High",
            "Company": "Overall Business",
            "Finding": "Average growth is below 8%",
            "Recommendation": (
                "Review the overall growth strategy, customer demand, "
                "and revenue opportunities."
            )
        })
    elif average_growth >= 15:
        recommendations.append({
            "Priority": "Positive",
            "Company": "Overall Business",
            "Finding": "Strong average growth",
            "Recommendation": (
                "Evaluate whether current growth can be maintained "
                "without increasing business risks."
            )
        })
    else:
        recommendations.append({
            "Priority": "Review",
            "Company": "Overall Business",
            "Finding": "Moderate average growth",
            "Recommendation": (
                "Identify opportunities to improve growth while "
                "monitoring profitability and costs."
            )
        })

    recommendations_df = pd.DataFrame(recommendations)

    # Display recommendation cards
    for _, item in recommendations_df.iterrows():
        with st.container(border=True):
            st.markdown(
                f"**{item['Company']}** — {item['Priority']}"
            )
            st.write(f"**Finding:** {item['Finding']}")
            st.write(
                f"**Recommended action:** "
                f"{item['Recommendation']}"
            )

    # Download recommendations
    st.download_button(
        label="⬇️ Download Business Recommendations",
        data=recommendations_df.to_csv(
            index=False
        ).encode("utf-8"),
        file_name="BizIntel_AI_Recommendations.csv",
        mime="text/csv",
        key="stage6_recommendations_download"
    )

    st.caption(
        "Recommendations are generated using predefined rules "
        "applied to the uploaded dataset. They are decision-support "
        "suggestions, not guaranteed business outcomes."
    )
# ==============================
# BizIntel AI - Professional Footer
# ==============================
st.divider()
st.markdown(
    """
    <div style="text-align: center; padding: 15px 0 5px 0;">
        <h4 style="margin-bottom: 5px; color: #64748b;">
            📊 BizIntel AI
        </h4>
        <p style="font-size: 13px; color: #64748b; margin-bottom: 5px;">
            AI-Powered Business Intelligence & Analytics
        </p>
        <p style="font-size: 12px; color: #94a3b8;">
            Built with Python, Streamlit, Pandas and Scikit-learn
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
