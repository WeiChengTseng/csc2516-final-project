import matplotlib.pyplot as plt
plt.style.use('seaborn')

approach = ['NeRF', 'Mip-NeRF', 'DirectVoxGO']
psnr = {
    'NeRF': [30.9, 27.9, 25.9, 22.0],
    'Mip-NeRF': [33.2, 28.2, 23.2, 21.0],
    'DirectVoxGO': [32.07, 30.07, 22.5, 20.57]
}
ssim = {
    'NeRF': [0.947, 0.917, 0.847, 0.801],
    'Mip-NeRF': [0.957, 0.908, 0.827, 0.807],
    'DirectVoxGO': [0.960, 0.92, 0.868, 0.782]
}
lpips = {
    'NeRF': [0.081, 0.131, 0.139, 0.147],
    'Mip-NeRF': [0.047, 0.129, 0.145, 0.162],
    'DirectVoxGO': [0.057, 0.107, 0.127, 0.187]
}
error = [0, 0.01, 0.05, 0.1]
perf_name = ['PSNR ↑', 'SSIM ↑', 'LPIPS ↓']
perf = [psnr, ssim, lpips]
lines = []

fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
fig.suptitle('Performance under Rotation Error')

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
fig.savefig('translation_error_rot.png', dpi=300)