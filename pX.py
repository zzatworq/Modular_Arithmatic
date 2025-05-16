import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['text.usetex'] = True  # For pretty labels

# Parameters
N = 50
MODULO = 100
x_values = range(1, MODULO)

# Ensure output folder exists
os.makedirs("imgs", exist_ok=True)

cycle_lengths = []

# Get distinct strong colors (tab10 reused per last digit)
base_colors = plt.get_cmap('tab10').colors

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
    plt.figure(figsize=(20, 6))

    color = base_colors[x % 10]  # Use same color for same last digit

    # Full line for visualization
    plt.plot(n_values, y_values, 
             linestyle='-', 
             color=color, 
             alpha=0.7, 
             linewidth=1.5)

    # Squares for actual cycle values only (in same color)
    plt.scatter(n_values[:cycle_len], y_values[:cycle_len], 
                color="black", 
                marker='s', 
                s=60, 
                zorder=3, 
                edgecolors='black', 
                linewidths=0.5)

    # Labels & Axis
    plt.title(rf"Cycle of $x^n \bmod {MODULO}$ for $x = {x}$", fontsize=20)
    
    plt.xlabel(r"Exponent $n$", fontsize=16)
    plt.ylabel(rf"$x^n \bmod {MODULO}$", fontsize=16)

    # Y-axis ticks limited to seen values only
    plt.yticks(seen)
    plt.ylim(-0.5, MODULO - 0.5)
    plt.xticks(range(1, N + 1, 1))
    plt.grid(True, linestyle='--', alpha=0.4)

    # Annotate cycle values as text in the plot
    cycle_str = ", ".join(map(str, seen))
    plt.annotate(rf"\textbf{{Cycle}}: $\{{ {cycle_str} \}}$", 
             xy=(0.98, 0.02), 
             xycoords='axes fraction',
             fontsize=14, 
             color='white', 
             bbox=dict(facecolor='black', alpha=0.8, edgecolor='white'),
             ha='right', va='bottom')

    # Save plot
    filename = f"images/{str(x).zfill(5)[::-1]}_mod{MODULO:05d}_cyclesfor_{x}.png"
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

# Final summary plot: Cycle length vs x
plt.figure(figsize=(14, 6))
plt.plot(x_values, cycle_lengths, 
         marker='o', 
         color='tab:green', 
         linestyle='-', 
         linewidth=2)

plt.title(rf"Cycle Length vs $x$ (mod {MODULO})", fontsize=20)
plt.xlabel(r"$x$", fontsize=16)
plt.ylabel("Cycle Length", fontsize=16)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(x_values)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f"imgs/cycle_length_vs_x_mod{MODULO:05d}.png", dpi=300)
plt.close()

print("All cycle plots + summary generated!")
