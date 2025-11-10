from astropy.io import fits
import numpy as np


filters = ["f090w", "f115w", "f150w", "f200w", "f277w", "f356w", "f444w"]

with open("FILTER.RES.jwst_nircam", "w") as fout:
    count = 350  # or next available filter ID in your master FILTER.RES
    for f in filters:
        hdu = fits.open(f"jwst_nircam_{f}_throughput.fits")
        data = hdu[1].data
        wave = np.array(data["WAVELENGTH"]) * 1e4  # μm → Å
        thru = np.array(data["THROUGHPUT"])

        N = len(wave)
        lambda_c = np.sum(wave * thru) / np.sum(thru)
        fout.write(f"{N:>5d} JWST_NIRCam_{f.upper()} lambda_c= {lambda_c:.4e}\n")
        for i in range(N):
            fout.write(f"{i+1:<5d} {wave[i]:.5e} {thru[i]:.5e}\n")
        hdu.close()
        count += 1

print("✅ Created FILTER.RES.jwst_nircam")