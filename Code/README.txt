Our code is divided into 3 sections:

1. DFDisplay
	i. DFDisplay is a GUI for exploring csv data that is generalized and nonspecific to our data. 
	ii. To run it, open DFDisplay/bin/run_DFDisplay.py in spyder and run the file.
2. Exploratory_Results_and_Visualizations.ipynb
	i. Exploratory analysis and plot of trends in the data
	ii. It should be opened in Jupyter Notebook to run it and/or see the existing results
	iii. PDF of the file included, but misses interactive graphs
3. project.py
	i. Project.py hosts the application of many of the advanced techniques we used such as csv merging, vector calculations, KNN applications
	ii. Contains a flag in the main method called: do_optimal_radius_calc
		a. When set to True, will find the optimal starbucks radius, this will require some computational time
		b. When set to False, will not find the optimal starbucks radius