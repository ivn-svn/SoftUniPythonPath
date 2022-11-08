# Submission Advisory

#### To Do list on files submission @ SoftUni Judge

## First do...
- Read the JetBrains documentation on Source Roots, Resource roots & other folder types in PyCharm CE & Pro. 
The JetBrains documentation describes it well and I have taken some of the descriptions from this [link](https://www.jetbrains.com/help/pycharm/configuring-project-structure.html)
- Set lab or exercise folder as a Resources root folder
- Set the folder containing your project as a Sources root folder

##### Or

### Circumvent the described above

by creating `__init__.py` file. You should add it in each subdirectory to mark it as a package. By adding it,
Python would treat the dirs as containing packages, making modules visible to other directories 
and available for import. 

## Final Step

- Make a ZIP file
- Submit in JUDGE

------


# PyCharm Term Definitions

### Source root
contains the actual source files and resources PyCharm uses the source roots as the starting point for resolving imports.
### Excluded
Those are all the files that are about to be excluded, ignored when searching, parsing indexing, etc. 
### Test Sources Roots
contains code related to testing. It has to be separated from the production code. 
### Resources Roots
are intended for resources such as images, stylesheets, etc. 
* The tricky here is that those are only available in PyCharm Pro, which some lecturers forget or avoid mentioning.
