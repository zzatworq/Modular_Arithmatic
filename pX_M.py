import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['text.usetex'] = True  # For pretty labels

# Parameters
N = 50
MODULO = 10
x_values = range(1, MODULO)

# Ensure output folder exists
os.makedirs("imgs", exist_ok=True)

cycle_lengths = []

# Get enough distinct colors (tab20 ensures more variety)
color_map = plt.get_cmap('tab10')
colors = [color_map(i) for i in range(len(x_values))]

for idx, x in enumerate(x_values):
    n_values = np.arange(1, N + 1, dtype=int)
    y_values = [pow(int(x), int(n), int(MODULO)) for n in n_values]

    # Find the cycle
    seen = []
    for val in y_values:
        if val in seen:
            break
        seen.append(val)

    cycle_len = len(seen)
    cycle_lengths.append(cycle_len)

    # Plotting
    fig, ax = plt.subplots(figsize=(20, 6))

    # Main line plot
    ax.plot(n_values, y_values, 
            linestyle='-', 
            color=colors[idx], 
            alpha=0.7, 
            linewidth=2)

    # Square markers for cycle values
    ax.scatter(n_values[:cycle_len], y_values[:cycle_len], 
               color=colors[idx], 
               marker='s', 
               s=70, 
               edgecolor='black', 
               linewidth=0.5, 
               zorder=3)

    # Labels & Axis
    ax.set_title(rf"Cycle of $x^n \bmod {MODULO}$ for $x = {x}$", fontsize=20)
    ax.set_xlabel(r"Exponent $n$", fontsize=16)
    ax.set_ylabel(rf"$x^n \bmod {MODULO}$", fontsize=16)

    # Y-axis ticks limited to cycle values only
    ax.set_yticks(seen)
    ax.set_xticks(range(1, N + 1))

    ax.grid(True, linestyle='--', alpha=0.4)

    # Annotate cycle values inside plot
    cycle_str = ", ".join(map(str, seen))
    ax.annotate(rf"\textbf{{Cycle}}: $\{{ {cycle_str} \}}$", 
                xy=(0.98, 0.02), 
                xycoords='axes fraction',
                fontsize=14, 
                color='black',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'),
                ha='right', va='bottom')

    # Save plot
    filename = f"imgs/{str(x)[::-1].zfill(3)}_mod{MODULO:05d}_cyclesfor_{x}.png"
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave extra space for decorations
    plt.savefig(filename, dpi=300)
    plt.close()

# Final summary plot: Cycle length vs x
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(x_values, cycle_lengths, 
        marker='o', 
        color='tab:blue', 
        linestyle='-', 
        linewidth=2)

ax.set_title(rf"Cycle Length vs $x$ (mod {MODULO})", fontsize=20)
ax.set_xlabel(r"$x$", fontsize=16)
ax.set_ylabel("Cycle Length", fontsize=16)

ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks(x_values)

plt.tight_layout()
plt.savefig(f"imgs/cycle_length_vs_x_mod{MODULO:05d}.png", dpi=300)
plt.close()

print("All cycle plots + summary generated!")
