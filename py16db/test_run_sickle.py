from .run_sickle import run_sickle
import os
import shutil
import unittest
from Bio import SeqIO
from nose.tools.nontrivial import with_setup

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

class test_run_sickle(unittest.TestCase):
    '''test for the run sickle function
    '''
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "testsickle", "")

        self.fastq1 = os.path.join(os.path.dirname(__file__), "test_data", "test_reads1.fq")
        self.fastq2 = os.path.join(os.path.dirname(__file__), "test_data", "test_reads2.fq")
                                   
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
            
    def tearDown(self):
        "tear down test fixtures"
        shutil.rmtree(self.test_dir)

   
    @unittest.skipIf("TRAVIS" in os.environ and os.environ["TRAVIS"] == "true",
                     "skipping this test on travis.CI")
    def test_sickle_SE(self):
        sickle_test_dir = (self.test_dir)
        fastq1 = self.fastq1
        fastq2 = None
        new_fastq1, new_fastq2 = run_sickle(fastq1=self.fastq1, fastq2 = None,
                                            output_dir=self.test_dir)

        assert file_len(fastq1) == file_len(new_fastq1)
        assert fastq2 == None

    #assert equal, as these reads don't need to be trimmed, the output is no trimmed reads.
    @unittest.skipIf("TRAVIS" in os.environ and os.environ["TRAVIS"] == "true",
                     "skipping this test on travis.CI")
    def test_sickle_singles_PE(self):
        sickle_test_dir = self.test_dir
        fastq1 = self.fastq1
        fastq2 = self.fastq2
        new_fastq1, new_fastq2 = run_sickle(fastq1=self.fastq1, fastq2 = self.fastq2,
                                            output_dir=self.test_dir)
        assert file_len(fastq1) == file_len(new_fastq1)
        assert file_len(fastq2) == file_len(new_fastq2)
        #assert equal, as these reads don't need to be trimmed, the output is no trimmed reads.
