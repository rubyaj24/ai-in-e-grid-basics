"""
Grid simulation teaser using pandapower.

Builds a tiny 5-bus radial feeder with solar generation and a battery,
runs a power flow calculation, then simulates a day of rule-based dispatch.
Positioned as a "where do we go next?" demo — not a full hands-on build.
"""

import pandapower as pp
import numpy as np
import pandas as pd


def build_network():
    """Create a 5-bus radial feeder network."""
    net = pp.create_empty_network()

    b0 = pp.create_bus(net, vn_kv=20.0, name="Substation")
    b1 = pp.create_bus(net, vn_kv=20.0, name="Bus 1")
    b2 = pp.create_bus(net, vn_kv=20.0, name="Bus 2 (Solar)")
    b3 = pp.create_bus(net, vn_kv=20.0, name="Bus 3 (Battery)")
    b4 = pp.create_bus(net, vn_kv=20.0, name="Bus 4 (Load)")

    pp.create_ext_grid(net, bus=b0, vm_pu=1.0, name="Grid Connection")
    pp.create_line(net, b0, b1, length_km=1.0, std_type="NAYY 4x50 SE", name="Line 0-1")
    pp.create_line(net, b1, b2, length_km=0.5, std_type="NAYY 4x50 SE", name="Line 1-2")
    pp.create_line(net, b1, b3, length_km=0.5, std_type="NAYY 4x50 SE", name="Line 1-3")
    pp.create_line(net, b1, b4, length_km=0.8, std_type="NAYY 4x50 SE", name="Line 1-4")
    pp.create_load(net, bus=b4, p_mw=0.25, q_mvar=0.05, name="Neighborhood Load")
    pp.create_sgen(net, bus=b2, p_mw=0.15, q_mvar=0, name="Rooftop Solar")
    pp.create_storage(net, bus=b3, p_mw=0.0, max_e_mwh=0.5, soc_percent=50, name="Battery")

    return net


def run_power_flow(net):
    """Run power flow and print results."""
    pp.runpp(net)
    return net.res_bus[["vm_pu", "va_degree"]], net.res_line[["loading_percent"]]


def simulate_day(
    solar_peak_mw: float = 0.15,
    load_evening_peak_mw: float = 0.25,
    charge_threshold: float = 0.05,
    discharge_hour: int = 17,
):
    """Simulate 24h of rule-based battery dispatch.

    Returns dict with hourly profiles for plotting.
    """
    hours = np.arange(24)
    solar_profile = np.clip(np.sin((hours - 6) / 12 * np.pi), 0, None) * solar_peak_mw
    load_profile = (
        0.10
        + (load_evening_peak_mw - 0.10)
        * np.exp(-((hours - 19) ** 2) / (2 * 3 ** 2))
    )

    battery_soc = [50.0]
    battery_dispatch = []

    for h in hours:
        surplus = solar_profile[h] - load_profile[h]
        if surplus > charge_threshold and battery_soc[-1] < 95:
            action_mw = -min(surplus, 0.1)
        elif h >= discharge_hour and battery_soc[-1] > 15:
            action_mw = min(0.1, load_profile[h])
        else:
            action_mw = 0.0
        battery_dispatch.append(action_mw)
        # Crude SOC update for illustration
        battery_soc.append(
            np.clip(battery_soc[-1] - action_mw / 0.5 * 100 * 0.25, 0, 100)
        )

    grid_import = load_profile - solar_profile - np.array(battery_dispatch)

    return {
        "hours": hours,
        "solar_profile": solar_profile,
        "load_profile": load_profile,
        "grid_import": grid_import,
        "battery_soc": battery_soc,
        "battery_dispatch": battery_dispatch,
    }
