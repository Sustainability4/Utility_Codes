# In windows please use anaconda prompt 

# Determine which environment you are in. The output will contain a star in fornt of the environment you are currently in. 
conda env list 

# create a conda environment. -n : new environment, testenv1 : name of the environment , python version 
conda create -n testenv1 python=3.6

# Activate the environment. After this you are in this environment 
conda activate testenv1

# Listing the packages installed in the environment. We can use both package managers as well. 
conda list 
pip list 

# Installing Packages 
pip install -r requirements.txt
pip install pandas numpy matplotlib 

# Uninstalling 
pip uninstall pandas numpy matplotlib 
conda remove pandas numpy -y 

# Create a new file 
touch package.txt 

# Open the file in the prompt 
vi package.txt 

# Display the contents of the file 
cat packages.txt

#list and freeze the packages 
pip freeze

# Remove an environment 
conda remove --name testenv1 --all

# Export the environment 
conda env export > environment.yml 

# deactivate the environment
conda deactivate testenv1

# Activate the base again 
conda activate base

# list the environment 
conda env list 

# Creating environment using a yml file 
conda env create -f environment.yml

