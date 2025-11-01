import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.qa_logic import top_crops, production_trend, available_years, available_crops

# Page configuration
st.set_page_config(
    page_title="Samarth Agri-Climate Q&A", 
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #2E8B57 0%, #228B22 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .metric-container {
        background-color: #f0f8f0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #2E8B57;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #f8fff8 !important;
        padding: 1rem !important;
    }
    
    /* Sidebar styling improvements */
    section[data-testid="stSidebar"] {
        background-color: #f8fff8 !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #f8fff8 !important;
        padding-top: 1rem !important;
    }
    .stSelectbox > div > div > div {
        background-color: white !important;
        border: 2px solid #e8f5e8 !important;
        border-radius: 5px !important;
    }
    
    /* Fix dropdown options visibility */
    .stSelectbox > div > div > div > div {
        background-color: white !important;
        color: #333333 !important;
    }
    
    /* Dropdown menu styling */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        border: 2px solid #2E8B57 !important;
    }
    
    /* Dropdown options */
    div[data-baseweb="menu"] {
        background-color: white !important;
        border: 1px solid #2E8B57 !important;
        border-radius: 5px !important;
    }
    
    div[data-baseweb="menu"] > ul > li {
        background-color: white !important;
        color: #333333 !important;
        padding: 8px 12px !important;
    }
    
    div[data-baseweb="menu"] > ul > li:hover {
        background-color: #f0f8f0 !important;
        color: #2E8B57 !important;
    }
    
    /* Sidebar text styling */
    section[data-testid="stSidebar"] label {
        color: #2E8B57 !important;
        font-weight: 600 !important;
    }
    
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #2E8B57 !important;
    }
    
    /* Select box text styling */
    .stSelectbox label {
        color: #2E8B57 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    .stSlider > div > div > div > div {
        background-color: #2E8B57;
    }
    div[data-testid="metric-container"] {
        background-color: #f0f8f0;
        border: 1px solid #d4edda;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Main header
st.markdown("""
    <div class="main-header">
        <h1>🌾 Samarth: Agri-Climate Q&A System</h1>
        <p style="margin: 0; font-size: 1.1em; opacity: 0.9;">
            Comprehensive agricultural data analysis powered by Data.gov.in
        </p>
    </div>
    """, unsafe_allow_html=True)

# Load data with caching for better performance
@st.cache_data
def load_data():
    try:
        return pd.read_csv('data/cleaned_agri_production.csv')
    except FileNotFoundError:
        st.error("❌ Data file not found. Please ensure 'data/cleaned_agri_production.csv' exists.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()

# Add loading spinner
with st.spinner('🔄 Loading agricultural data...'):
    df = load_data()

# Data validation
if df.empty:
    st.error("❌ No data available in the dataset.")
    st.stop()

# Add a success message for data loading
st.success(f"✅ Successfully loaded {len(df):,} agricultural records!")

# Sidebar for controls
with st.sidebar:
    st.header("🔧 Analysis Controls")
    st.markdown("---")
    
    # State selection
    st.subheader("📍 Location")
    state = st.selectbox(
        'Select State:', 
        sorted(df['State'].unique()),
        help="Choose a state to analyze agricultural data"
    )
    
    # Year selection
    years = available_years(df, state)
    year = st.selectbox(
        'Select Year:', 
        years,
        help="Select the year for crop production analysis"
    )
    
    st.markdown("---")
    st.subheader("🌱 Crop Analysis")
    
    # Crop selection
    crops = available_crops(df, state)
    crop = st.selectbox(
        'Select Crop:', 
        crops,
        help="Choose a specific crop for trend analysis"
    )
    
    # Number of top crops
    n = st.slider(
        'Top N Crops:', 
        min_value=1, 
        max_value=15, 
        value=5,
        help="Number of top-producing crops to display"
    )
    
    # Add a collapsible section for advanced filters
    with st.expander("🔧 Advanced Filters", expanded=False):
        # Season filter
        available_seasons = sorted(df['Season'].dropna().unique())
        selected_seasons = st.multiselect(
            "Filter by Season:",
            available_seasons,
            default=available_seasons,
            help="Select specific seasons to analyze"
        )
        
        # Production range filter
        min_production = st.number_input(
            "Minimum Production (Tonnes):",
            min_value=0,
            value=0,
            help="Filter crops with production above this threshold"
        )
    
    st.markdown("---")
    st.markdown("**💡 Tip:** All data is sourced from Data.gov.in and updated regularly for accuracy.")

# Main content area
col1, col2 = st.columns([2, 1])

# Main content area
col1, col2 = st.columns([2, 1])

with col2:
    # Summary statistics
    st.subheader("📊 Quick Stats")
    
    # Apply advanced filters to current data
    current_data = df[
        (df['State'] == state) & 
        (df['Year_clean'] == year) &
        (df['Season'].isin(selected_seasons)) &
        (df['Production'] >= min_production)
    ]
    
    if not current_data.empty:
        total_production = current_data['Production'].sum()
        total_area = current_data['Area'].sum()
        unique_crops = current_data['Crop'].nunique()
        unique_districts = current_data['District'].nunique()
        
        st.metric(
            label="Total Production",
            value=f"{total_production:,.0f} Tonnes",
            help="Total crop production in the selected state and year"
        )
        
        st.metric(
            label="Total Area",
            value=f"{total_area:,.0f} Hectares",
            help="Total cultivated area in the selected state and year"
        )
        
        st.metric(
            label="Crop Varieties",
            value=f"{unique_crops}",
            help="Number of different crops grown"
        )
        
        st.metric(
            label="Districts",
            value=f"{unique_districts}",
            help="Number of districts with agricultural data"
        )
    
    # Additional insights
    st.markdown("---")
    st.subheader("🔍 Quick Insights")
    
    # Top producing district
    if not current_data.empty:
        top_district = current_data.groupby('District')['Production'].sum().idxmax()
        top_district_production = current_data.groupby('District')['Production'].sum().max()
        
        st.info(f"**Top District:** {top_district}\n\n**Production:** {top_district_production:,.0f} tonnes")
        
        # Most cultivated crop
        top_crop_by_area = current_data.groupby('Crop')['Area'].sum().idxmax()
        top_crop_area = current_data.groupby('Crop')['Area'].sum().max()
        
        st.success(f"**Most Cultivated:** {top_crop_by_area}\n\n**Area:** {top_crop_area:,.0f} hectares")

with col1:
    st.header(f'🏆 Top {n} Crops by Production - {state} ({year})')
    
    # Apply filters to top crops data as well
    filtered_df = df[
        (df['Season'].isin(selected_seasons)) &
        (df['Production'] >= min_production)
    ]
    
    try:
        top_crops_data = top_crops(filtered_df, state, year, n)
        
        if not top_crops_data.empty:
            # Create a more attractive dataframe display
            display_df = top_crops_data.reset_index()
            display_df.columns = ['🌱 Crop', '📦 Production (Tonnes)']
            display_df['📦 Production (Tonnes)'] = display_df['📦 Production (Tonnes)'].apply(lambda x: f"{x:,.0f}")
            display_df.index = range(1, len(display_df) + 1)
            
            st.dataframe(
                display_df, 
                use_container_width=True,
                hide_index=False
            )
            
            # Add a bar chart for better visualization
            fig_bar = px.bar(
                x=top_crops_data.values,
                y=top_crops_data.index,
                orientation='h',
                title=f"Top {n} Crops Production Comparison",
                labels={'x': 'Production (Tonnes)', 'y': 'Crops'},
                color=top_crops_data.values,
                color_continuous_scale='Greens'
            )
            fig_bar.update_layout(
                showlegend=False,
                height=400,
                yaxis={'categoryorder': 'total ascending'}
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.warning("⚠️ No data available for the selected filters. Try adjusting your criteria.")
    except Exception as e:
        st.error(f"❌ Error processing crop data: {str(e)}")
        st.info("💡 Try selecting different parameters or check your data filters.")

# Production trend section
st.header(f'📈 Production Trend: {crop} in {state}')

trend_data = production_trend(df, crop, state)

if not trend_data.empty and len(trend_data) > 1:
    # Create an enhanced line chart with plotly
    fig_line = px.line(
        trend_data,
        x='Year_clean',
        y='Production',
        title=f'{crop} Production Trend in {state}',
        labels={'Year_clean': 'Year', 'Production': 'Production (Tonnes)'},
        markers=True
    )
    
    fig_line.update_traces(
        line=dict(color='#2E8B57', width=3),
        marker=dict(size=8, color='#228B22')
    )
    
    fig_line.update_layout(
        height=500,
        hovermode='x unified',
        xaxis_title="Year",
        yaxis_title="Production (Tonnes)"
    )
    
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Add trend analysis
    if len(trend_data) >= 2:
        latest_year = trend_data['Year_clean'].max()
        earliest_year = trend_data['Year_clean'].min()
        latest_production = trend_data[trend_data['Year_clean'] == latest_year]['Production'].iloc[0]
        earliest_production = trend_data[trend_data['Year_clean'] == earliest_year]['Production'].iloc[0]
        
        if latest_production > earliest_production:
            trend_direction = "📈 Increasing"
            trend_color = "green"
        elif latest_production < earliest_production:
            trend_direction = "📉 Decreasing"
            trend_color = "red"
        else:
            trend_direction = "➡️ Stable"
            trend_color = "blue"
        
        percentage_change = ((latest_production - earliest_production) / earliest_production) * 100
        
        col_trend1, col_trend2, col_trend3 = st.columns(3)
        
        with col_trend1:
            st.metric(
                "Trend Direction", 
                trend_direction,
                help="Overall production trend from first to last available year"
            )
        
        with col_trend2:
            st.metric(
                "Latest Production",
                f"{latest_production:,.0f} Tonnes",
                help=f"Production in {latest_year}"
            )
        
        with col_trend3:
            st.metric(
                "Overall Change",
                f"{percentage_change:+.1f}%",
                help=f"Percentage change from {earliest_year} to {latest_year}"
            )
else:
    st.warning(f"Insufficient data to show trend for {crop} in {state}. Please select a different crop or state.")

# Additional Analysis Section
st.markdown("---")
st.header("🔄 Comparative Analysis")

col_comp1, col_comp2 = st.columns(2)

with col_comp1:
    st.subheader("📊 District-wise Production")
    
    district_data = df[(df['State'] == state) & (df['Year_clean'] == year) & (df['Crop'] == crop)]
    
    if not district_data.empty:
        district_production = district_data.groupby('District')['Production'].sum().sort_values(ascending=False).head(10)
        
        if len(district_production) > 0:
            fig_district = px.bar(
                x=district_production.values,
                y=district_production.index,
                orientation='h',
                title=f"{crop} Production by District ({year})",
                labels={'x': 'Production (Tonnes)', 'y': 'District'},
                color=district_production.values,
                color_continuous_scale='Blues'
            )
            fig_district.update_layout(
                showlegend=False,
                height=400,
                yaxis={'categoryorder': 'total ascending'}
            )
            st.plotly_chart(fig_district, use_container_width=True)
        else:
            st.info("No district-level data available for the selected combination.")
    else:
        st.info("No data available for the selected crop, state, and year combination.")

with col_comp2:
    st.subheader("🗓️ Year-over-Year Comparison")
    
    # Get last 5 years of data for the state
    recent_years = sorted(df[df['State'] == state]['Year_clean'].unique())[-5:]
    yearly_data = []
    
    for yr in recent_years:
        year_production = df[(df['State'] == state) & (df['Year_clean'] == yr)]['Production'].sum()
        yearly_data.append({'Year': yr, 'Total Production': year_production})
    
    if yearly_data:
        yearly_df = pd.DataFrame(yearly_data)
        
        fig_yearly = px.line(
            yearly_df,
            x='Year',
            y='Total Production',
            title=f"Total Production Trend - {state}",
            markers=True
        )
        
        fig_yearly.update_traces(
            line=dict(color='#FF6B35', width=3),
            marker=dict(size=10, color='#FF6B35')
        )
        
        fig_yearly.update_layout(height=400)
        st.plotly_chart(fig_yearly, use_container_width=True)
    else:
        st.info("No yearly data available for comparison.")

# Data Export Section
st.markdown("---")
st.header("📥 Data Export & Insights")

col_export1, col_export2, col_export3 = st.columns(3)

with col_export1:
    # Export current selection data
    current_selection_data = df[(df['State'] == state) & (df['Year_clean'] == year)]
    if not current_selection_data.empty:
        csv_data = current_selection_data.to_csv(index=False)
        st.download_button(
            label="📊 Download Current Data (CSV)",
            data=csv_data,
            file_name=f"{state}_{year}_agricultural_data.csv",
            mime="text/csv",
            help="Download filtered data for the current selection"
        )

with col_export2:
    # Export top crops data
    if not top_crops_data.empty:
        top_crops_csv = top_crops_data.reset_index().to_csv(index=False)
        st.download_button(
            label="🏆 Download Top Crops (CSV)",
            data=top_crops_csv,
            file_name=f"top_{n}_crops_{state}_{year}.csv",
            mime="text/csv",
            help="Download top crops production data"
        )

with col_export3:
    # Export trend data
    if not trend_data.empty:
        trend_csv = trend_data.to_csv(index=False)
        st.download_button(
            label="📈 Download Trend Data (CSV)",
            data=trend_csv,
            file_name=f"{crop}_trend_{state}.csv",
            mime="text/csv",
            help="Download production trend data for selected crop"
        )

st.markdown('**📚 Source:** cleaned_agri_production.csv (Data.gov.in) | **🔄 Last Updated:** November 2025')
