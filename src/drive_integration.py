"""
Drive Integration Demo Package
A simple demonstration of integrating drive data analysis using NumPy, Pandas, and Matplotlib.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DriveAnalyzer:
    """
    A class to analyze and visualize drive data.
    """
    
    def __init__(self):
        self.data = None
        self.results = {}
    
    def generate_sample_data(self, duration=10, points=100):
        """
        Generate sample drive data for demonstration.
        
        Parameters:
        duration (float): Time duration in seconds
        points (int): Number of data points
        
        Returns:
        pandas.DataFrame: Generated data
        """
        time = np.linspace(0, duration, points)
        velocity = np.sin(time) + 0.1 * np.random.randn(points)
        acceleration = np.cos(time) + 0.05 * np.random.randn(points)
        distance = np.cumsum(velocity) * (duration/points)
        
        self.data = pd.DataFrame({
            'Time (s)': time,
            'Velocity (m/s)': velocity,
            'Acceleration (m/s²)': acceleration,
            'Distance (m)': distance
        })
        
        return self.data
    
    def analyze_data(self):
        """
        Perform basic analysis on the drive data.
        
        Returns:
        dict: Analysis results
        """
        if self.data is None:
            raise ValueError("No data available. Please generate or load data first.")
        
        self.results = {
            'mean_velocity': self.data['Velocity (m/s)'].mean(),
            'max_velocity': self.data['Velocity (m/s)'].max(),
            'min_velocity': self.data['Velocity (m/s)'].min(),
            'total_distance': self.data['Distance (m)'].iloc[-1],
            'data_points': len(self.data)
        }
        
        return self.results
    
    def plot_velocity(self, save_path=None):
        """
        Plot velocity over time.
        
        Parameters:
        save_path (str): Path to save the plot (optional)
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Time (s)'], self.data['Velocity (m/s)'], 
                label='Velocity', color='blue', linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.title('Drive Velocity Analysis')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def plot_comprehensive(self, save_path=None):
        """
        Create a comprehensive plot of all metrics.
        
        Parameters:
        save_path (str): Path to save the plot (optional)
        """
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
        
        # Velocity plot
        ax1.plot(self.data['Time (s)'], self.data['Velocity (m/s)'], 
                color='blue', linewidth=2)
        ax1.set_ylabel('Velocity (m/s)')
        ax1.set_title('Drive Performance Metrics')
        ax1.grid(True, alpha=0.3)
        
        # Acceleration plot
        ax2.plot(self.data['Time (s)'], self.data['Acceleration (m/s²)'], 
                color='red', linewidth=2)
        ax2.set_ylabel('Acceleration (m/s²)')
        ax2.grid(True, alpha=0.3)
        
        # Distance plot
        ax3.plot(self.data['Time (s)'], self.data['Distance (m)'], 
                color='green', linewidth=2)
        ax3.set_ylabel('Distance (m)')
        ax3.set_xlabel('Time (s)')
        ax3.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()

def quick_demo():
    """
    Run a quick demonstration of the drive analyzer.
    """
    print("=== Drive Integration Demo ===\n")
    
    # Create analyzer instance
    analyzer = DriveAnalyzer()
    
    # Generate sample data
    print("Generating sample drive data...")
    data = analyzer.generate_sample_data()
    print(f"Generated {len(data)} data points")
    
    # Analyze data
    print("\nAnalyzing data...")
    results = analyzer.analyze_data()
    
    # Print results
    for key, value in results.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")
    
    # Create plots
    print("\nCreating visualizations...")
    analyzer.plot_velocity()
    analyzer.plot_comprehensive()
    
    return analyzer

if __name__ == "__main__":
    quick_demo()