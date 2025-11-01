# 🌾 Samarth: Agri-Climate Q&A System

An interactive Streamlit web application for comprehensive agricultural data analysis in India. This system provides insights into crop production, trends, and agricultural patterns using data sourced from Data.gov.in.

## ✨ Features

- **📊 Interactive Dashboard**: Modern, responsive UI with enhanced visualizations
- **🗺️ State-wise Analysis**: Comprehensive crop production data by state and year
- **📈 Production Trends**: Time-series analysis of crop production patterns
- **🌱 Top Crops Analysis**: Identify leading crops by production volume
- **🔍 Advanced Filtering**: Season-based and multi-criteria filtering options
- **📱 Mobile-Friendly**: Responsive design that works on all devices
- **🎨 Enhanced UX**: Improved color scheme and accessibility

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
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

- Data.gov.in for providing the agricultural dataset
- Streamlit community for the excellent web framework
- Plotly for interactive visualization capabilities

## 📈 Future Enhancements

- [ ] Weather data integration
- [ ] Machine learning predictions
- [ ] Export functionality for reports
- [ ] Multi-language support
- [ ] API integration for real-time data
- [ ] Mobile app version

---

**Made with ❤️ for agricultural data analysis in India**
