# fooof-opatzlab

this very simple script takes in a series of power spectra and fooofs them, according to https://github.com/voytekresearch/fooof

it takes matlab files in, and spits matlab files out

lab_main_script is a ready-to-go script, which you can modify locally and use for whatever you want. as it is, it runs with some test-data that comes from my folder.

to run it, make sure to have installed anaconda -> https://conda.io/docs/index.html
the inpout files are:

	- a .mat file containing your power spectra, in which rows represent different observations (es. a 10x200 matrix, 
		for 10 observations and 200 points in the power spectrum)

	- a.mat file containing the frequencies that correspond to the power spectrum (a 1x200 matrix, in the previous example)

the output file is a .mat file in which:

	- the first column corresponds to the frequency of the identified peak in the power spectrum

	- the second column corresponds to the amplitude of the peak

	- the third column is the width of the peak (not 100% sure about this)

parameters you can control (with self-explanatory names) are:

	- the frequency range that you want to analyze (freq_range) in Hz

	- the min and max width of the peaks (peak_width_limits)

	- the maximum number of peaks (max_n_peaks)

In case you want to plot your results, set plot to 1. Be aware that it will plot one figure for every power spectrum that you feed him.


This is the preprint of reference (a good one!): https://www.biorxiv.org/content/biorxiv/early/2018/04/11/299859.full.pdf

And here is again the repository from which I have taken the code: https://github.com/voytekresearch/fooof