# 🌾 Samarth: Agri-Climate Q&A System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://samarth-agri-climate-q-a-system.streamlit.app/)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ashutosh8021/Samarth-Agri-Climate-Q-A-System.svg)](https://github.com/ashutosh8021/Samarth-Agri-Climate-Q-A-System/stargazers)

An interactive Streamlit web application for comprehensive agricultural data analysis in India. This system provides insights into crop production, trends, and agricultural patterns using data sourced from Data.gov.in.

## 🌐 Live Demo

**🚀 [Try the Live Application](https://samarth-agri-climate-q-a-system.streamlit.app/)**

Experience the full functionality of the agricultural data analysis system directly in your browser. No installation required!

## ✨ Features

- **📊 Interactive Dashboard**: Modern, responsive UI with enhanced visualizations
- **🗺️ State-wise Analysis**: Comprehensive crop production data by state and year
- **📈 Production Trends**: Time-series analysis of crop production patterns
- **🌱 Top Crops Analysis**: Identify leading crops by production volume
- **🔍 Advanced Filtering**: Season-based and multi-criteria filtering options
- **📱 Mobile-Friendly**: Responsive design that works on all devices
- **🎨 Enhanced UX**: Improved color scheme and accessibility
- **⚡ Real-time Analytics**: Instant data processing and visualization updates

## 🎯 Use Cases

- **🌾 Farmers & Agricultural Scientists**: Analyze crop performance and make data-driven decisions
- **📊 Policy Makers**: Understand agricultural trends for better policy formulation
- **🎓 Students & Researchers**: Access comprehensive agricultural data for academic research
- **💼 Agricultural Businesses**: Market analysis and crop selection strategies
- **📰 Journalists & Analysts**: Create data-driven agricultural reports

## 🚀 Quick Start

### 🌐 Option 1: Use Online (Recommended)
Simply visit the **[Live Demo](https://samarth-agri-climate-q-a-system.streamlit.app/)** - no setup required!

### 💻 Option 2: Local Installation

#### Prerequisites
- Python 3.7 or higher
- pip package manager

#### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ashutosh8021/Samarth-Agri-Climate-Q-A-System.git
   cd "Samarth Agri Q&A system"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Access the app**
   - Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
Samarth Agri Q&A system/
├── data/
│   └── cleaned_agri_production.csv    # Agricultural production dataset
├── src/
│   ├── qa_logic.py                    # Core analytics functions
│   └── __pycache__/                   # Python cache files
├── streamlit_app.py                   # Main Streamlit application
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

## 🛠️ Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **plotly**: Interactive visualization library

## 📊 Data Source

The agricultural production data is sourced from [Data.gov.in](https://data.gov.in/), India's open data platform. The dataset includes:

- **Coverage**: All Indian states and union territories
- **Time Period**: Multiple years of agricultural data
- **Crops**: Wide variety of crops including cereals, pulses, oilseeds, and more
- **Metrics**: Area, production, and yield data

## 📸 Screenshots & Demo

### 🖥️ Main Dashboard
The application features a clean, intuitive interface with:
- **Sidebar Controls**: Easy navigation and filtering options
- **Interactive Charts**: Dynamic visualizations that update in real-time
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### 📱 Mobile Experience
- Optimized sidebar that collapses on smaller screens
- Touch-friendly controls and visualizations
- Fast loading and smooth interactions

> **💡 Tip**: Visit the [Live Demo](https://samarth-agri-climate-q-a-system.streamlit.app/) to explore all features interactively!

## 🚀 Deployment

### Streamlit Cloud Deployment
This application is deployed on **Streamlit Cloud** for easy access:

- **Live URL**: https://samarth-agri-climate-q-a-system.streamlit.app/
- **Auto-deployment**: Automatically updates when code is pushed to the main branch
- **Free hosting**: No server maintenance required
- **Global CDN**: Fast loading worldwide

### Deploy Your Own Instance

1. **Fork this repository** on GitHub
2. **Sign up** for [Streamlit Cloud](https://streamlit.io/cloud)
3. **Connect your GitHub account** and select the forked repository
4. **Deploy** with one click - Streamlit Cloud will handle the rest!

## 🎯 Usage Guide

### Navigation
1. **Analysis Controls Panel**: Use the sidebar to select state, year, and crop parameters
2. **Location Selection**: Choose from Indian states and union territories
3. **Year Selection**: Select from available years for the chosen state
4. **Crop Analysis**: Pick specific crops for detailed trend analysis
5. **Advanced Filters**: Use season filters and other criteria for refined analysis

### Key Features
- **Top Crops Visualization**: Interactive bar charts showing leading crops
- **Production Trends**: Time-series line charts for production patterns
- **Comparative Analysis**: Side-by-side comparison of different crops and states
- **Data Export**: Download filtered data for further analysis

## 🔧 Configuration

### Environment Variables
No additional environment variables required for basic setup.

### Customization
- Modify color schemes in the CSS section of `streamlit_app.py`
- Update data source in the `load_data()` function
- Extend analytics functions in `src/qa_logic.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) section
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

## 🎉 Acknowledgments

- **[Data.gov.in](https://data.gov.in/)** for providing the comprehensive agricultural dataset
- **[Streamlit](https://streamlit.io/)** community for the excellent web framework
- **[Plotly](https://plotly.com/)** for interactive visualization capabilities
- **Agricultural scientists and researchers** who make data-driven farming possible

## 📊 Project Stats

- **Dataset Size**: 340,000+ agricultural records
- **Coverage**: All Indian states and union territories
- **Time Span**: Multi-year agricultural production data
- **Deployment**: Streamlit Cloud with global CDN
- **Performance**: Sub-second query response times

## 📈 Future Enhancements

- [ ] **🌦️ Weather Data Integration**: Correlate production with weather patterns
- [ ] **🤖 Machine Learning Predictions**: Forecast crop yields and trends
- [ ] **📋 Export Functionality**: Download reports in PDF/Excel formats
- [ ] **🌍 Multi-language Support**: Hindi and regional language options
- [ ] **🔌 API Integration**: Real-time data feeds and updates
- [ ] **📱 Mobile App Version**: Native mobile application
- [ ] **🗺️ GIS Integration**: Interactive maps with geospatial analysis
- [ ] **📈 Advanced Analytics**: Statistical modeling and forecasting

## ⭐ Show Your Support

If this project helped you, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** for your own modifications
- 🐛 **Reporting issues** to help improve the application
- 💡 **Suggesting features** for future development

---

<div align="center">

**🌾 Made with ❤️ for agricultural data analysis in India 🇮🇳**

*Empowering farmers, researchers, and policymakers with data-driven insights*

[![GitHub](https://img.shields.io/badge/GitHub-ashutosh8021-black?style=flat-square&logo=github)](https://github.com/ashutosh8021)
[![Streamlit](https://img.shields.io/badge/Deployed%20on-Streamlit%20Cloud-red?style=flat-square&logo=streamlit)](https://samarth-agri-climate-q-a-system.streamlit.app/)

</div>
