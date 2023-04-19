import matplotlib.pyplot as plt
plt.style.use('seaborn')

approach = ['NeRF', 'Mip-NeRF', 'DirectVoxGO']
psnr = {
    'NeRF': [30.9, 29.9, 27.9, 27.0],
    'Mip-NeRF': [33.2, 29.2, 25.2, 25.0],
    'DirectVoxGO': [32.07, 31.07, 28.07, 23.07]
}
ssim = {
    'NeRF': [0.947, 0.927, 0.877, 0.844],
    'Mip-NeRF': [0.957, 0.928, 0.857, 0.837],
    'DirectVoxGO': [0.960, 0.930, 0.888, 0.80]
}
lpips = {
    'NeRF': [0.081, 0.101, 0.121, 0.131],
    'Mip-NeRF': [0.047, 0.12, 0.129, 0.147],
    'DirectVoxGO': [0.057, 0.087, 0.097, 0.137]
}
error = [0, 0.01, 0.05, 0.1]
perf_name = ['PSNR ↑', 'SSIM ↑', 'LPIPS ↓']
perf = [psnr, ssim, lpips]
lines = []

fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
fig.suptitle('Performance under Translation Error')

for idx, ax in enumerate(axes):
    ax.set_title(perf_name[idx])
    for a in approach:
        line = ax.plot(error, perf[idx][a], 'o-', alpha=0.9)[0]
        lines.append(line)

fig.subplots_adjust(bottom=0.20,
                    top=0.85,
                    left=0.03,
                    right=0.99,
                    wspace=0.18,
                    hspace=0.0)
# fig.tight_layout()
fig.legend(lines[:3], approach, loc='lower center', ncol=3)
fig.savefig('translation_error.png', dpi=300)