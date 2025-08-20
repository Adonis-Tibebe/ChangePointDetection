import ruptures as rpt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def find_change_points(series, penalty, cost_func, min_size, jump):
    """Find change points for given parameters"""
    model = rpt.Pelt(model=cost_func, min_size=min_size, jump=jump).fit(series)
    breakpoints = model.predict(pen=penalty)
    return breakpoints[:-1]  # Remove the last point (end of series)
def plot_change_points(price_df, change_point_dates, events_df=None):
    """Comprehensive visualization of change points and events"""
    fig, axes = plt.subplots(2, 1, figsize=(16, 14))

    # Plot 1: Price with change points
    axes[0].plot(price_df['Date'], price_df['Price'], linewidth=1.5, color='steelblue', alpha=0.9)
    for cp_date in change_point_dates:
        axes[0].axvline(x=cp_date, color='red', linestyle='--', alpha=0.7, linewidth=1.5)
    axes[0].set_title('Brent Price with Detected Change Points', fontsize=16, fontweight='bold')
    axes[0].set_ylabel('Price ($)', fontsize=12)
    axes[0].grid(True, alpha=0.3)

    # Plot 2: Log returns with change points
    axes[1].plot(price_df['Date'], price_df['Log_Return'], linewidth=0.5, color='forestgreen', alpha=0.6)
    axes[1].axhline(y=0, color='black', linestyle='-', alpha=0.3)
    for cp_date in change_point_dates:
        axes[1].axvline(x=cp_date, color='red', linestyle='--', alpha=0.7, linewidth=1.5)
    axes[1].set_title('Log Returns with Change Points', fontsize=16, fontweight='bold')
    axes[1].set_ylabel('Log Return', fontsize=12)
    axes[1].grid(True, alpha=0.3)

    # Add events if provided
    if events_df is not None:
        for _, event in events_df.iterrows():
            axes[0].axvline(x=event['start_date'], color='orange', linestyle=':',
                           alpha=0.8, linewidth=2, label='Geopolitical Event')

    # Create custom legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='red', linestyle='--', linewidth=1.5, label='Detected Change Point'),
        Line2D([0], [0], color='orange', linestyle=':', linewidth=2, label='Geopolitical Event')
    ]
    axes[2].legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()
    plt.show()


def calculate_segment_statistics(price_df, breakpoint_indices):
    """Calculate statistics for each segment between change points"""
    segments = []
    all_indices = [0] + breakpoint_indices + [len(price_df)]

    for i in range(len(all_indices) - 1):
        start_idx = all_indices[i]
        end_idx = all_indices[i + 1]
        segment_data = price_df.iloc[start_idx:end_idx]

        if len(segment_data) < 5:  # Skip very short segments
            continue

        segment_stats = {
            'segment_id': i + 1,
            'start_date': segment_data['Date'].iloc[0],
            'end_date': segment_data['Date'].iloc[-1],
            'duration_days': (segment_data['Date'].iloc[-1] - segment_data['Date'].iloc[0]).days,
            'mean_price': segment_data['Price'].mean(),
            'median_price': segment_data['Price'].median(),
            'mean_log_return': segment_data['Log_Return'].mean() * 100,  # Convert to percentage
            'volatility': segment_data['Log_Return'].std() * np.sqrt(252) * 100,  # Annualized percentage
            'n_observations': len(segment_data)
        }
        segments.append(segment_stats)

    return pd.DataFrame(segments)

def match_events_with_change_points(change_point_dates, events_df, max_days_window=90):
    """Match detected change points with historical events"""
    matches = []

    for cp_date in change_point_dates:
        # Find closest event
        time_diffs = (events_df['start_date'] - cp_date).abs()
        closest_idx = time_diffs.idxmin()
        closest_event = events_df.loc[closest_idx]
        days_diff = time_diffs.iloc[closest_idx].days

        if days_diff <= max_days_window:
            match_status = "✅ STRONG MATCH" if days_diff <= 30 else "⚠️ WEAK MATCH"
        else:
            match_status = "❌ NO MATCH"

        match_info = {
            'change_point_date': cp_date,
            'event_title': closest_event['title'],
            'event_date': closest_event['start_date'],
            'days_difference': days_diff,
            'event_category': closest_event['category'],
            'event_impact': closest_event['impact_direction'],
            'match_status': match_status
        }
        matches.append(match_info)

    return pd.DataFrame(matches)


def analyze_strong_matches(strong_matches_df, changes_df, events_df):
    """Detailed analysis of strongly matched events"""
    strong_analysis = []

    for _, match in strong_matches_df.iterrows():
        cp_date = match['change_point_date']

        # Find the corresponding change point impact
        change_point_impact = changes_df[changes_df['change_point_date'] == cp_date]

        if not change_point_impact.empty:
            impact = change_point_impact.iloc[0]

            # Get the full event details
            event_details = events_df[events_df['title'] == match['event_title']].iloc[0]

            analysis = {
                'change_point_date': cp_date,
                'event_title': match['event_title'],
                'event_date': match['event_date'],
                'days_difference': match['days_difference'],
                'event_category': match['event_category'],
                'event_impact_direction': match['event_impact'],
                'price_change_pct': impact['price_change_pct'],
                'volatility_change_pct': impact['volatility_change_pct'],
                'price_before': impact['from_price'],
                'price_after': impact['to_price'],
                'volatility_before': impact['from_volatility'],
                'volatility_after': impact['to_volatility'],
                'event_description': event_details['description'],
                'influence_level': event_details['influence_level']
            }
            strong_analysis.append(analysis)

    return pd.DataFrame(strong_analysis)

def export_results(price_df, results_df, segment_stats_df, changes_df, event_matches_df, strong_matches_analysis_df=None):
    """Export all results to CSV files"""
    # Add price at change point for reference
    results_df['price_at_cp'] = price_df['Price'].iloc[results_df['breakpoint_index']].values

    # Export all dataframes
    results_df.to_csv('../data/processed/change_point_detection_results/change_point_results.csv', index=False)
    segment_stats_df.to_csv('../data/processed/change_point_detection_results/segment_statistics.csv', index=False)
    changes_df.to_csv('../data/processed/change_point_detection_results/change_impact_analysis.csv', index=False)
    event_matches_df.to_csv('../data/processed/change_point_detection_results/event_matching_results.csv', index=False)

    if strong_matches_analysis_df is not None and len(strong_matches_analysis_df) > 0:
        strong_matches_analysis_df.to_csv('strong_matches_analysis.csv', index=False)
        print("💾 Strong matches analysis exported")

    print("💾 All results exported to CSV files")