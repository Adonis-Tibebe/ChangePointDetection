class ChangePointConfig:
    """Configuration for change point detection using ruptures"""
    def __init__(self):
        self.cost_function = "normal"  # Detect changes in mean AND variance
        self.search_method = "Pelt"    # Pruned Exact Linear Time
        self.penalty_values = [2, 5, 10, 15, 20, 30, 35]  # Range to test
        self.min_segment_size = 22     # Minimum 1 month of trading days
        self.jump = 5                  # Speed up computation
        self.primary_penalty = 30      # Starting point