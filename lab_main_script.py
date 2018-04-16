# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:49:39 2018

@author: mchini
"""

import scipy.io as scio
from fooof import FOOOF
import numpy as np
import matplotlib.pyplot as plt

path_load = "Q:\\Personal\\Mattia\\PyrProject\\analysis\\fooof\\test_data\\" ## the folder where you have the files you want to analyze
path_save = "Q:\\Personal\\Mattia\\PyrProject\\analysis\\fooof\\test_data\\" ## the folder where you want to save your data
name_file_spectra = "spectra"
name_matlab_variable_spectra = 'Spectrumpost'
name_file_freqs = "freqs"
name_matlab_variable_freqs = 'freqs'

spectra = scio.loadmat(path_load + name_file_spectra)[name_matlab_variable_spectra]
freqs = scio.loadmat(path_load + name_file_freqs)[name_matlab_variable_freqs]

freq_range = [4, 50]
peak_width_limits=[1.0, 3.0]
max_n_peaks = 10


peaks_params = np.zeros((np.shape(spectra)[0], max_n_peaks, 3))

for spectra_idx in np.arange(0, np.shape(spectra)[0]):
    fm = FOOOF(max_n_peaks=max_n_peaks, peak_width_limits=peak_width_limits)
    fm.fit(freqs, np.squeeze(spectra[spectra_idx, :]), freq_range)
    peaks_param = fm.peak_params_
    peaks_params[spectra_idx, 0 : np.shape(peaks_param)[0], 0 : np.shape(peaks_param)[1]] = peaks_param

plt.figure() 
plt.scatter(peaks_params[:, :, 0], peaks_params[:, :, 1])


power_spectrum = np.zeros(50,)
for spectra_idx in np.arange(0, np.shape(spectra)[0]):
    power_spectrum[np.round(peaks_params[spectra_idx, :, 0]).astype(int)] = np.shape(peaks_param)[1] + \
        power_spectrum[np.round(peaks_params[spectra_idx, :, 0]).astype(int)]