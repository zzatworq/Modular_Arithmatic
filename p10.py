import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True  # Enable LaTeX rendering

# Parameters
N = 20
x_values = list(range(10))
BOX_SPACING = 0.16  # Vertical gap between boxes

# Reduced vertical size
plt.figure(figsize=(24, 8))

# Get tab10 colors and dim them for softer tones
base_colors = np.array(plt.cm.tab10.colors)
dimmed_colors = base_colors * 0.4 + np.ones_like(base_colors) * 0.6  # Blend more with white (60%)

# Track y-positions to stack boxes properly
y_tracker = {n: [] for n in range(1, N + 1)}

for x in x_values:
    base = x % 10
    n_values = list(range(1, N + 1))
    results = [pow(base, n, 10) for n in n_values]

    for n, val in zip(n_values, results):
        target_y = val
        used = y_tracker[n]

        # Find next available y-slot to avoid overlaps
        slot = 0
        while any(abs(target_y + slot * BOX_SPACING - uy) < BOX_SPACING * 0.9 for uy in used):
            slot += 1

        adj_y = target_y + slot * BOX_SPACING
        y_tracker[n].append(adj_y)

        # Place text box with sharp rectangle, thin border
        plt.text(
            n, adj_y,
            rf"${x}^{{{n}}} = {x**n}$",
            fontsize=8,
            ha='center', va='center',
            color='black',
            bbox=dict(
                facecolor=dimmed_colors[x % 10],
                edgecolor='black',
                linewidth=0.3,              # Thinnest possible border
                boxstyle='square,pad=0.05'  # Sharp corners, minimal padding
            )
        )

# Labels and styling

plt.xlabel(r"$n$", fontsize=18)
plt.ylabel(r"$x^n \bmod 10$", fontsize=18)

plt.xticks(range(1, N + 1))
plt.yticks(range(10))
plt.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig(f"powers_mod10_{BOX_SPACING}.png", dpi=300)
plt.close()  # Close to free memory
