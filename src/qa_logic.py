import pandas as pd

def top_crops(df, state, year, n=5):
    filtered = df[(df['State'] == state) & (df['Year_clean'] == year)]
    return filtered.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(n)

def production_trend(df, crop, state):
    filtered = df[(df['Crop'] == crop) & (df['State'] == state)]
    return filtered.sort_values('Year_clean')[['Year_clean', 'Production']]

def available_years(df, state):
    return sorted(df[df['State'] == state]['Year_clean'].dropna().unique())

def available_crops(df, state):
    return sorted(df[df['State'] == state]['Crop'].dropna().unique())
