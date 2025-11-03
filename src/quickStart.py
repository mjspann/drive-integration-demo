# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:33:53 2025

@author: mspann
"""
from drive_integration import DriveAnalyzer

# Create analyzer instance
analyzer = DriveAnalyzer()

# Generate sample data
data = analyzer.generate_sample_data(duration=10, points=100)

# Analyze data
results = analyzer.analyze_data()

# Create plots
analyzer.plot_velocity()
analyzer.plot_comprehensive()