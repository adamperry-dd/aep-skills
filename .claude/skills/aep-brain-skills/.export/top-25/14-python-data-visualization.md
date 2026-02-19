---
name: python-data-visualization
description: Create data visualizations in Python using matplotlib, seaborn, and plotly. Use when making charts, plots, heatmaps, statistical visualizations, or interactive dashboards. Covers static publication figures, statistical analysis plots, and interactive web visualizations.
---

# Python Data Visualization

Unified guide for Python visualization covering matplotlib (static/custom), seaborn (statistical), and plotly (interactive).

## Quick Decision: Which Library?

| Need | Library | Why |
|------|---------|-----|
| **Fine-grained control** | matplotlib | Full customization of every element |
| **Statistical plots** | seaborn | Built-in aggregation, CI, publication-ready |
| **Interactive/web** | plotly | Pan, zoom, hover, HTML export |
| **Quick EDA** | seaborn | One-liners for distributions, correlations |
| **Publication figures** | matplotlib + seaborn | Vector export (PDF/SVG), precise styling |
| **Dashboards** | plotly + Dash | Interactive web applications |
| **3D visualization** | matplotlib or plotly | Both support 3D; plotly is interactive |

## Matplotlib: Foundation & Control

**Use for:** Full customization, novel plot types, publication figures, integration with scientific workflows.

### Core Pattern (Object-Oriented - Recommended)

```python
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

# Plot data
x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2)

# Customize
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trigonometric Functions')
ax.legend()
ax.grid(True, alpha=0.3)

# Save
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf', bbox_inches='tight')  # Vector for publications
```

### Multiple Subplots

```python
# Regular grid
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data, bins=30)

# Flexible layout
fig, axes = plt.subplot_mosaic([['left', 'right_top'],
                                 ['left', 'right_bottom']])
```

### Key Plot Types

```python
ax.plot(x, y)                    # Line plot
ax.scatter(x, y, c=colors, s=sizes)  # Scatter
ax.bar(categories, values)       # Bar chart
ax.hist(data, bins=30)           # Histogram
ax.imshow(matrix, cmap='viridis')  # Heatmap
ax.contour(X, Y, Z)              # Contour
ax.boxplot([d1, d2, d3])         # Box plot
```

### Colormaps

- **Sequential:** viridis, plasma, inferno (ordered data)
- **Diverging:** coolwarm, RdBu (centered data)
- **Qualitative:** tab10, Set3 (categories)
- **Avoid:** jet (not perceptually uniform)

---

## Seaborn: Statistical Visualization

**Use for:** Statistical plots, distributions, correlations, publication figures with minimal code.

### Quick Start

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set theme
sns.set_theme(style='whitegrid', palette='colorblind')

# Load data
df = sns.load_dataset('tips')

# One-line visualization
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day', size='size')
plt.show()
```

### Key Plot Types by Purpose

**Relationships:**
```python
sns.scatterplot(data=df, x='x', y='y', hue='category')
sns.lineplot(data=df, x='time', y='value', errorbar='sd')
sns.regplot(data=df, x='x', y='y')  # With regression line
```

**Distributions:**
```python
sns.histplot(data=df, x='value', hue='group', stat='density')
sns.kdeplot(data=df, x='x', y='y', fill=True)
sns.boxplot(data=df, x='category', y='value')
sns.violinplot(data=df, x='group', y='measurement', split=True)
```

**Categorical:**
```python
sns.barplot(data=df, x='day', y='total_bill', errorbar='ci')
sns.swarmplot(data=df, x='day', y='total_bill')  # Show all points
sns.countplot(data=df, x='category')
```

**Matrix/Correlation:**
```python
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
sns.clustermap(data, cmap='viridis', standard_scale=1)
```

**Multi-panel:**
```python
sns.pairplot(data=df, hue='species', corner=True)
sns.jointplot(data=df, x='x', y='y', kind='scatter', hue='group')
```

### Faceting (Small Multiples)

```python
# Figure-level functions support col/row
sns.relplot(data=df, x='x', y='y', col='category', row='group', hue='type')
sns.catplot(data=df, x='day', y='total_bill', col='time', kind='box')
sns.displot(data=df, x='value', col='group', kind='kde')
```

### Axes-Level vs Figure-Level

| Axes-Level | Figure-Level |
|------------|--------------|
| scatterplot, histplot, boxplot | relplot, displot, catplot |
| Plot to single axes | Manage entire figure |
| Use `ax=` parameter | Use `col=`, `row=` for faceting |
| Return Axes | Return FacetGrid |

---

## Plotly: Interactive Visualization

**Use for:** Interactive charts, web dashboards, hover tooltips, animations.

### Quick Start (Plotly Express)

```python
import plotly.express as px

# Simple scatter
fig = px.scatter(df, x='x', y='y', color='category', size='value',
                 hover_data=['name'], title='Interactive Plot')
fig.show()

# Save
fig.write_html('chart.html')
fig.write_image('chart.png')  # Requires kaleido
```

### Key Plot Types

```python
# Basic charts
px.scatter(df, x='x', y='y', trendline='ols')
px.line(df, x='date', y='price')
px.bar(df, x='category', y='value', color='group')
px.histogram(df, x='value', marginal='box')

# Statistical
px.box(df, x='category', y='value', points='all')
px.violin(df, x='group', y='measurement', box=True)

# Heatmaps
px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='RdBu')

# 3D
px.scatter_3d(df, x='x', y='y', z='z', color='category')

# Geographic
px.scatter_geo(df, lat='latitude', lon='longitude', color='region')
px.choropleth(df, locations='country', color='value')

# Financial
import plotly.graph_objects as go
go.Candlestick(x=df['date'], open=df['open'], high=df['high'],
               low=df['low'], close=df['close'])
```

### Subplots

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=('A', 'B', 'C', 'D'))
fig.add_trace(go.Scatter(x=[1,2], y=[3,4]), row=1, col=1)
fig.add_trace(go.Bar(x=['A','B'], y=[1,2]), row=1, col=2)
```

### Interactivity

```python
# Custom hover
fig.update_traces(hovertemplate='<b>%{x}</b><br>Value: %{y:.2f}')

# Range slider for time series
fig.update_xaxes(rangeslider_visible=True)

# Animation
px.scatter(df, x='x', y='y', animation_frame='year')
```

### Templates

```python
# Built-in themes
fig = px.scatter(df, x='x', y='y', template='plotly_dark')
# Options: plotly_white, plotly_dark, ggplot2, seaborn, simple_white
```

---

## Best Practices

### 1. Data Preparation
- Use pandas DataFrames with meaningful column names
- Prefer long-form (tidy) data for seaborn

### 2. Publication Quality
```python
# Matplotlib
plt.savefig('fig.pdf', dpi=300, bbox_inches='tight')

# Seaborn
sns.set_theme(style='ticks', context='paper', font_scale=1.1)
sns.despine(trim=True)

# Plotly
fig.write_image('fig.pdf')  # Requires kaleido
```

### 3. Accessibility
- Use colorblind-safe palettes (viridis, colorblind)
- Add patterns/hatching for bar charts
- Include descriptive labels and legends

### 4. Performance
- For large datasets, use `rasterized=True` (matplotlib)
- Downsample before plotting if needed
- Use WebGL renderer for plotly with many points

### 5. Colormap Selection
- Sequential: Ordered data (viridis, plasma)
- Diverging: Centered data (coolwarm, RdBu)
- Qualitative: Categories (tab10, Set3)

---

## Common Patterns

### EDA Workflow
```python
# Quick overview
sns.pairplot(df, hue='target', corner=True)

# Distributions
sns.displot(df, x='variable', hue='group', kind='kde', fill=True)

# Correlations
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
```

### Publication Figure
```python
sns.set_theme(style='ticks', context='paper')
fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=df, x='x', y='y', hue='group', ax=ax)
ax.set_xlabel('X Label (units)')
ax.set_ylabel('Y Label (units)')
sns.despine()
plt.savefig('figure.pdf', bbox_inches='tight')
```

### Interactive Dashboard
```python
import plotly.express as px
from plotly.subplots import make_subplots

# Create multi-panel interactive figure
fig = make_subplots(rows=2, cols=2)
# Add traces...
fig.update_layout(height=800)
fig.write_html('dashboard.html')
```

---

## Installation

```bash
# Core
uv pip install matplotlib seaborn plotly pandas numpy

# For plotly static export
uv pip install kaleido

# For plotly dashboards
uv pip install dash
```

## Resources

- Matplotlib: https://matplotlib.org/stable/gallery/
- Seaborn: https://seaborn.pydata.org/examples/
- Plotly: https://plotly.com/python/
