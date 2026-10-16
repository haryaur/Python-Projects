# Architectural Documentation & Assumptions

## Systems Assertions & Rules
1. **Static Member Registrations**: Members can only register before the financial cycle begins. Once `Main.py` advances past the declaration phase, the community size is locked to protect distribution metrics.
2. **String Formatting Constraints**: All money data formats cleanly to 2 decimal places to maintain string display accuracy for Ghanaian Cedi (GHS) metrics within logs.
3. **Sequential Receivers**: The order of weekly pot distribution strictly mirrors the original order of creation inside the initialization array.

## Core System Choices
* **Isolated Script Architecture**: Splitting calculation loops from registration fields prevents accidental context leakage and keeps runtime logs readable.
* **Validation Bounds**: The internal script uses boundary restrictions `0 <= entry <= maximum` to filter out negative values and prevent users from overpaying beyond what they owe.

## Future Engineering Optimization Plans
1. **Incorporate Decimal Objects**: Swap all baseline float representations over to Python's dedicated `decimal.Decimal` module to remove binary floating-point roundoff behaviors entirely.
2. **Persistent Storage Layouts**: Integrate a native `json` data layer so transactions are securely saved instead of wiping from RAM when terminal contexts drop.