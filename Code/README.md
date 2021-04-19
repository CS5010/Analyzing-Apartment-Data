Our code is divided into 3 sections:

1. DFDisplay
   1. DFDisplay is a GUI for exploring csv data that is generalized and nonspecific to our data. 
   2. To run it, open DFDisplay/bin/run_DFDisplay.py in spyder and run the file.
2. Exploratory_Results_and_Visualizations.ipynb
   1. Exploratory analysis and plot of trends in the data
   2. It should be opened in Jupyter Notebook to run it and/or see the existing results
   3. PDF of the file included, but misses interactive graphs
3. project.py
   1. Project.py hosts the application of many of the advanced techniques we used such as csv merging, vector calculations, KNN applications
   2. Contains a flag in the main method called: do_optimal_radius_calc
      1. When set to True, will find the optimal starbucks radius, this will require some computational time
      2. When set to False, will not find the optimal starbucks radius
