# 16db
## High resolution 16S database construction from correctly assembled rDNA operons

## Description
16db is a package built for the construction of species-specific, high-resolution 16S rDNA databases.
It does so with through the use of riboSeed, a pipeline for the use of ribosomal flanking regions to improve bacterial genome assembly.
riboSeed allows the correct assembly of multiple rDNA operons within a single genome. 16db uses various tools around and including
riboSeed to take an input of arguments listed below and produces a file containing all 16S sequences from draft full genomes available for that species.


## Installation
###### Installing 16db
TODO: get pip install worrking
```
pip install 16db
```

###### Packages required for 16db:
```
conda install python=3.5 seqtk sickle-trim sra-tools riboseed mash skesa barrnap parallel-fastq-dump iqtree
```
Optionally, to use the trimming alignment feature, TrimAl must be installed from github https://github.com/scapella/trimal


## Usage
###### Example
```
# reassemble SRAs and extract potentially novel 16S sequnces
16db --output_dir ./escherichia/ -g ./escherichia_genomes/ --n_SRAs 5 --n_references 30 --memory 8 --cores 4 --organism_name "Escherichia coli"
# build E. coli specific DB from E colis in Silva and our new seqeunces
combine-focusdb-and-silva
```



##### `16db`
This will go through the process of getting the list of assemblies that are associated with SRAs, downloading up to 5 SRAs,  finding the closes referece for each of the 5 SRAs, assembling, and extracting the 16S sequences.



###### Required Arguments
```
[--organism_name]: The species of interest, input within quotes.
[--nstrains]: The number of reference genomes and the number of SRAs the user wishes to download.
[--output_dir]: The output directory.
[--genomes_dir]: The output directory for which to store reference genomes, or a preexisting directory containing genomes the user wishes to use as reference genomes.
```
###### Optional Arguments:
```
[--sra_list]: Uses a user-given list of SRA accessions instead of obtaining SRA accessions from the pipeline.
[--version]: Returns 16db version number.
[--approx_length]: Uses a user-given genome length as opposed to using reference genome length.
[--sraFind_path]: Path to pre-downloaded sraFind-All-biosample-with-SRA-hits.txt file.
[--prokaryotes]: Path to pre-downloaded prokaryotes.txt file.
[--get_all]: If one SRA has two accessions, downloads both.
[--cores]: The number of cores the user would like to use for 16db. Specifically, riboSeed and plentyofbugs can be optimized for thread usage.
[--memory]: As with [--cores], RAM can be optimized for 16db.
[--maxcov]: The maximum read coverage for SRA assembly. Downsamples to this coverage if the coverage exceeds it.
[--example_reads]: Input of user-given reads.
[--subassembler]: Choice of mash or skesa for subassembly in riboSeed.
```

### Included Utilities:
#### `combine-focusdb-and-silva`
Use this script to combine silva  and 16db seqeunces for a given organism name.
#### `align-and-trim-focusdb`
This script  uses mafft and TrimAl to provide a trimmed and aligned MSA.
#### `calculate-shannon-entropy`


## Test Data
### Unit tests
Testing is done with the `nose` package. Generate the test data with
```
nosetests  py16db/generator.py
```
and run the unit tests with

```
nosetests py16db/ -v
```

Note  that `generator.py` requires ART to generate synthetic.
{https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm}

### Running on test datasets




## Bugs

### OpenBlas on MacOS
If you get a failure running riboSeed about `dependencies not installed:["numpy"]`, try running `python -c "import numpy as np"`. If you get an error about openblas, try upgrading the one chosen by conda with:
```
conda install openblas=0.2.19
```
