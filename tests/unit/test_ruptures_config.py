import pytest
from src.models.ruptures_config import ChangePointConfig


class TestChangePointConfig:
    """Test cases for ChangePointConfig class"""
    
    def test_config_initialization(self):
        """Test that config initializes with expected default values"""
        config = ChangePointConfig()
        
        assert config.cost_function == "normal"
        assert config.search_method == "Pelt"
        assert config.penalty_values == [2, 5, 10, 15, 20, 30, 35]
        assert config.min_segment_size == 22
        assert config.jump == 5
        assert config.primary_penalty == 30
    
    def test_config_attributes_exist(self):
        """Test that all expected attributes exist"""
        config = ChangePointConfig()
        
        expected_attrs = [
            'cost_function', 'search_method', 'penalty_values',
            'min_segment_size', 'jump', 'primary_penalty'
        ]
        
        for attr in expected_attrs:
            assert hasattr(config, attr)
    
    def test_penalty_values_type(self):
        """Test that penalty_values is a list of integers"""
        config = ChangePointConfig()
        
        assert isinstance(config.penalty_values, list)
        assert all(isinstance(x, int) for x in config.penalty_values)
    
    def test_numeric_attributes(self):
        """Test that numeric attributes are integers"""
        config = ChangePointConfig()
        
        assert isinstance(config.min_segment_size, int)
        assert isinstance(config.jump, int)
        assert isinstance(config.primary_penalty, int)
