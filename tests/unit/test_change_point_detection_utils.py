import pytest
import pandas as pd
import numpy as np
from datetime import datetime
from src.utils.change_point_deteciton_utils import (
    calculate_segment_statistics,
    match_events_with_change_points
)


class TestChangePointDetectionUtils:
    """Test cases for change point detection utility functions"""
    
    def setup_method(self):
        """Set up test data before each test"""
        # Create sample price data
        dates = pd.date_range('2020-01-01', periods=100, freq='D')
        prices = np.random.randn(100).cumsum() + 50  # Random walk starting at 50
        log_returns = np.random.randn(100) * 0.02  # Random log returns
        
        self.price_df = pd.DataFrame({
            'Date': dates,
            'Price': prices,
            'Log_Return': log_returns
        })
        
        # Sample breakpoint indices
        self.breakpoint_indices = [25, 50, 75]
        
        # Sample events data
        self.events_df = pd.DataFrame({
            'title': ['Event 1', 'Event 2', 'Event 3'],
            'start_date': [
                datetime(2020, 1, 26),  # Close to breakpoint 25
                datetime(2020, 2, 20),  # Close to breakpoint 50
                datetime(2020, 3, 16)   # Close to breakpoint 75
            ],
            'category': ['test', 'test', 'test'],
            'impact_direction': ['up', 'down', 'up']
        })
    
    def test_calculate_segment_statistics(self):
        """Test segment statistics calculation"""
        result = calculate_segment_statistics(self.price_df, self.breakpoint_indices)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 4  # 4 segments from 3 breakpoints
        
        # Check required columns
        required_cols = [
            'segment_id', 'start_date', 'end_date', 'duration_days',
            'mean_price', 'median_price', 'mean_log_return', 'volatility', 'n_observations'
        ]
        for col in required_cols:
            assert col in result.columns
    
    def test_calculate_segment_statistics_data_types(self):
        """Test that segment statistics have correct data types"""
        result = calculate_segment_statistics(self.price_df, self.breakpoint_indices)
        
        # Check numeric columns
        numeric_cols = ['segment_id', 'duration_days', 'mean_price', 'median_price', 
                       'mean_log_return', 'volatility', 'n_observations']
        for col in numeric_cols:
            assert pd.api.types.is_numeric_dtype(result[col])
        
        # Check date columns
        date_cols = ['start_date', 'end_date']
        for col in date_cols:
            assert pd.api.types.is_datetime64_any_dtype(result[col])
    
    def test_match_events_with_change_points(self):
        """Test event matching with change points"""
        change_point_dates = pd.to_datetime(['2020-01-25', '2020-02-20', '2020-03-15'])
        
        result = match_events_with_change_points(change_point_dates, self.events_df)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3  # One match per change point
        
        # Check required columns
        required_cols = [
            'change_point_date', 'event_title', 'event_date', 'days_difference',
            'event_category', 'event_impact', 'match_status'
        ]
        for col in required_cols:
            assert col in result.columns
    
    def test_match_events_with_change_points_basic_functionality(self):
        """Test basic functionality of event matching"""
        change_point_dates = pd.to_datetime(['2020-01-25'])
        
        result = match_events_with_change_points(change_point_dates, self.events_df)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1
        assert 'match_status' in result.columns
    
    def test_empty_breakpoints(self):
        """Test handling of empty breakpoint list"""
        result = calculate_segment_statistics(self.price_df, [])
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1  # Single segment for entire dataset
