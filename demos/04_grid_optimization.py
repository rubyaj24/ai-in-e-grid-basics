"""
DEMO 4: Grid Optimization Teaser

A tiny simulated feeder with solar + battery to show where AI-driven
optimization fits beyond forecasting and detection.

This is a "look how deep this rabbit hole goes" demo, not a full
hands-on build. The battery uses simple rules — contrast this with
what a learned policy could do.
"""

from src.egrid_learning.grid_sim.dispatch import build_network, run_power_flow, simulate_day
from src.egrid_learning.visualization.plots import plot_grid_dispatch

print("=" * 55)
print("  DEMO 4: Grid Optimization Teaser")
print("=" * 55)

net = build_network()
bus_results, line_results = run_power_flow(net)

print("\n=== Baseline power flow (midday, solar producing) ===")
print(bus_results.to_string())
print("\nLine loading (%):")
print(line_results.to_string())

results = simulate_day()

print("\n=== Daily dispatch summary ===")
print(f"  Total solar generated: {results['solar_profile'].sum():.3f} MWh")
print(f"  Total load consumed:   {results['load_profile'].sum():.3f} MWh")
print(f"  Total grid import:     {results['grid_import'].sum():.3f} MWh")
print(f"  Battery cycles:        {abs(sum(results['battery_dispatch'])):.2f} MWh throughput")

plot_grid_dispatch(
    results["hours"],
    results["solar_profile"],
    results["load_profile"],
    results["grid_import"],
    results["battery_soc"],
    save_path="assets/images/grid_dispatch_result.png",
)

print("\n--- Key insight ---")
print("This dispatch uses two hardcoded rules (charge when surplus > threshold,")
print("discharge after 5 PM). A learned policy (RL or optimization solver) could")
print("automatically find the dispatch that minimizes cost or grid import,")
print("adapting when the load or solar profile shifts.")
print("\nOpen docs/06-grid-optimization.md for the full walkthrough.")
