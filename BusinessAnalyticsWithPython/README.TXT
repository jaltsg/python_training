1) Install a distribution of Python:
https://www.anaconda.com/download/
Please install the Python 3.X version
Note: Please check the box that says to add python to system path.
For step by step instructions https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444


2) Ensure the environment has been set up properly:
Go to the terminal or console. 
 For windows, it is windows-r, type `cmd` and enter. 
 For mac/linux, go to spotlight and type in terminal.
Check if Python is working.
 Type `ipython` in the terminal. It should launch the python command prompt.. type exit() to exit from it.
Check if package managers are working (internet required).
 Type `pip install sqlalchemy`


3) Install additional libraries
`pip install pydotplus feedparser flask-restplus mysql-connector-python nltk networkx PyMySQL pymongo requests seaborn Scrapy sklearn-pandas selenium statsmodels twython`
Offline version of the libraries are included in the pypi folder in your project directory.
You can install the offline packages via `pip install pypi/*` from your main project directory


4) Set up Graphviz and include the path to the Graphviz bin folder in your system path. https://www.graphviz.org/ 
Offline version of the installers are found in the installFiles folder in your project directory


5) Start up the Jupyter notebook (previously known as IPython) in your project folder.
double click on the startNotebook.bat (windows) 
or for linux/OSX terminal, change the directory to where your tutorial files are. e.g. `cd /Users/myusername/Desktop/BusinessAnalyticsWithPython`
Type `jupyter notebook` or `ipython notebook` for those that have an older version of the anaconda distribution.
It should launch your default browser and you should be able to see the contents in that folder from your browser.

