from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all domains on all routes.
CORS(app)

# Configuration
# We'll assume the CSV files are in a 'data' folder next to this app.py file.
DATA_DIR = os.path.join("../../", 'data/processed')

# Helper function to load and prep CSV data
def load_data(filename):
    """Loads a CSV file from the data directory and converts date columns."""
    filepath = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(filepath)
    
    # Convert any column with 'date' in its name to datetime
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col])
    return df

# Load all the data once when the server starts
# This is efficient for static data that doesn't change.
try:
    price_df = load_data('BrentOilPrices_transformed.csv')  
    change_points_df = load_data('change_point_detection_results/change_point_results.csv')
    segment_stats_df = load_data('change_point_detection_results/segment_statistics.csv')
    change_impact_df = load_data('change_point_detection_results/change_impact_analysis.csv')
    event_matches_df = load_data('change_point_detection_results/event_matching_results.csv')
    strong_matches_df = load_data('change_point_detection_results/strong_matches_analysis.csv')
    print("✅ All data loaded successfully!")
except FileNotFoundError as e:
    print(f"❌ Error: Could not find a data file: {e}")
    print("Please make sure your CSV files are in the 'data' directory.")
    # Exit if data loading fails
    exit(1)

# Define API Routes
@app.route('/')
def hello():
    
    return jsonify({"message": "Brent Oil Analysis API is running!"})

@app.route('/api/price_data', methods=['GET'])
def get_price_data():
    """Returns the main price series with dates, prices, and log returns."""
    # Convert DataFrame to a list of dictionaries for JSON serialization
    price_data_json = price_df.where(pd.notnull(price_df), None).to_dict('records')
    return jsonify(price_data_json)

@app.route('/api/change_points', methods=['GET'])
def get_change_points():
    """Returns the list of detected change points."""
    change_points_json = change_points_df.where(pd.notnull(change_points_df), None).to_dict('records')
    return jsonify(change_points_json)

@app.route('/api/segments', methods=['GET'])
def get_segments():
    """Returns the statistics for each segment between change points."""
    segment_stats_json = segment_stats_df.to_dict('records')
    return jsonify(segment_stats_json)

@app.route('/api/events', methods=['GET'])
def get_events():
    """Returns the event matching results."""
    event_matches_json = event_matches_df.to_dict('records')
    return jsonify(event_matches_json)

@app.route('/api/strong_matches', methods=['GET'])
def get_strong_matches():
    """Returns the detailed analysis for strongly matched events."""
    strong_matches_json = strong_matches_df.to_dict('records')
    return jsonify(strong_matches_json)

@app.route('/api/impact_analysis', methods=['GET'])
def get_impact_analysis():
    """Returns the impact analysis for all change points."""
    impact_analysis_json = change_impact_df.to_dict('records')
    return jsonify(impact_analysis_json)

# This if statement ensures the app only runs when this file is executed directly,
# not when it's imported as a module.
if __name__ == '__main__':
    app.run(debug=True, port=5000) 