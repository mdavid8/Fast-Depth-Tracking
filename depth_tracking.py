import numpy as np
from scipy import signal, ndimage
import time

datapath = "sample.dat"
frames, height, width = 1000, 424, 512 
noise, threshold, ksize = 3, 100, 25
outfile = 'positions.npy'

def load_all_frames(path, frames=frames, height=height, width=width):
    raw = np.fromfile(path, dtype='uint16')
    raw.shape = frames, height, width
    return raw

raw = load_all_frames(datapath)

def track_position(cframe):
    """return xy position of 2D projected center of detected object"""
    labeled_array, num_features = ndimage.label(cframe>=np.percentile(cframe, 99.5))
    m = [np.sum(labeled_array==i+1) for i in range(num_features)]
    x,y = ndimage.measurements.center_of_mass(cframe, labels=labeled_array, index=m.index(max(m))+1)
    return int(x), int(y)

start_time = time.time()

base = np.median(raw, axis=0) - raw
base[(base>threshold)|(base<=noise)] = 0

denoised = base.copy()
denoised[signal.convolve(denoised>0, np.ones((1,3,3)), mode='same')<9]=0
cu = signal.convolve(denoised>0, np.ones((1,ksize,ksize)), mode='same')

positions = np.array([track_position(cu[i]) for i in range(frames)])

elapsed = time.time() - start_time
print("%.1f FPS: %d frames processed in %.2f seconds" % ( frames/elapsed, frames, elapsed))

print ('saving mouse positions to', outfile)
np.save(outfile, positions)
