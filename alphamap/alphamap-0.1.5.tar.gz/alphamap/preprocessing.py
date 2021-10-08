# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/Preprocessing.ipynb (unless otherwise specified).

__all__ = ['extract_uniprot_id', 'expand_protein_ids', 'pep_position_helper', 'get_peptide_position', 'get_ptm_sites',
           'get_modifications', 'format_input_data']

# Cell
import pandas as pd
def extract_uniprot_id(protein_id:str):
    """
    Extract the Uniprot unique entry id from the unusual formatted protein_id.
    """
    if 'sp' in protein_id:
        return protein_id.split('|')[1]
    elif '__' in protein_id:
        return protein_id.split('__')[-1]
    return protein_id

def expand_protein_ids(df: pd.DataFrame):
    """
    Function to split protein groups in 'all_protein_ids' by ';' into separate rows.
    The resulting dataframe has a new column 'unique_protein_id'.
    Args:
        df (pd.DataFrame): Experimental data that was imported by the 'import_data' function.
    Returns:
        pd.DataFrame: Exploded dataframe with a new column 'unique_protein_id'.
    """
    df = df.copy(deep=True)
    df.all_protein_ids = df.all_protein_ids.str.split(';')
    df["all_protein_ids_all"] = df.all_protein_ids.apply(lambda x: ';'.join(sorted(x)))
    res = df.explode('all_protein_ids').reset_index(drop=True)
    res.columns = ['unique_protein_id','modified_sequence','naked_sequence','all_protein_ids']
    res.unique_protein_id = res.unique_protein_id.apply(lambda x: extract_uniprot_id(x))
    return res

# Cell
import re
import numpy as np
from pyteomics import fasta

def pep_position_helper(seq: str, prot: str, fasta: fasta, verbose: bool = True):
    """
    Helper function for 'get_peptide_position'.

    Args:
        seq (str): Naked peptide sequence.
        prot (str): UniProt protein accession.
        fasta (fasta): Fasta file imported by pyteomics 'fasta.IndexedUniProt'.
        verbose (bool, optional): Flag to print warnings if no matching sequence is found for a protein in the provided fasta. Defaults to 'True'.
    Returns:
        [int, int]: int: peptide start position, int: peptide end position

    """
    try:
        fasta_prot = fasta[prot]
        search_res = re.search(seq,fasta_prot.sequence)
        if search_res is None:
            start, end = np.NaN, np.NaN
            if verbose:
                warnings.warn(f'Peptide sequence {seq} could not be mached to {prot} in the selected fasta.')
        else:
            start, end = search_res.span()
    except:
        start, end = np.NaN, np.NaN
        if verbose:
            warnings.warn(f'No matching entry for {prot} in the selected fasta.')

    return start, end-1

# Cell

import warnings

def get_peptide_position(df: pd.DataFrame, fasta: fasta, verbose:bool = True):
    """
    Function to get start and end position of each peptide in the given protein.

    Args:
        df (pd.DataFrame): Experimental data that was imported by the 'import_data' function and processed by 'expand_protein_ids'.
        fasta (fasta): Fasta file imported by pyteomics 'fasta.IndexedUniProt'.
        verbose (bool, optional): Flag to print warnings if no matching sequence is found for a protein in the provided fasta. Defaults to 'True'.
    Returns:
        pd.DataFrame: Dataframe with a new columns 'start' and 'end', indicating the start and end index position of the peptide sequence.

    """
    res = df.copy(deep=True)
    res[['start','end']] = res.apply(lambda row: pep_position_helper(row['naked_sequence'],
                                                                     row['unique_protein_id'],
                                                                     fasta,
                                                                     verbose=verbose),
                                     axis=1, result_type='expand')

    res_na = res[res.isnull().any(1)]
    prots_na = res_na.unique_protein_id.unique()

    res = res.dropna()
    res['start'] = res['start'].astype('int64')
    res['end'] = res['end'].astype('int64')
    return res

# Cell
import numpy as np

def get_ptm_sites(peptide: str, modification_reg: str):
    """
    Function to get sequence positions of all PTMs of a peptide in the given protein.

    Args:
        peptide (str): Experimental data that was imported by the 'import_data' function and processed by 'expand_protein_ids'.
        modification_reg (str): Regular expression for the modifications.
    Returns:
        list: List of integers with PTM site location indices on the peptide.

    """
    r = re.compile(modification_reg)
    starts=[]
    ends=[]
    for m in r.finditer(peptide):
        starts.append(m.start())
        ends.append(m.end())
    PTM_sites = np.zeros(len(starts))
    for idx in range(0,len(starts)):
        if idx > 0:
            previous_len=previous_len+(ends[idx-1]-starts[idx-1])
        else:
            previous_len=0
        PTM_sites[idx] = starts[idx] - previous_len - 1
    PTM_sites = [int(i)+1 if i < 0 else int(i) for i in PTM_sites]
    return PTM_sites

# Cell
import re

def get_modifications(df: pd.DataFrame, mod_reg: str):
    """
    Function to get sequence positions and modification types of all PTMs of a peptide in the given protein.

    Args:
        df (pd.DataFrame): Experimental data that was imported by the 'import_data' function and processed by 'expand_protein_ids'.
        mod_reg (str): Regular expression for the modifications.
    Returns:
        pd.DataFrame: Dataframe with a new columns 'PTMsites' and 'PTMtypes' containing lists of PTM site indices and modification types, respectively.

    """
    res = df.copy(deep=True)
    res['PTMsites'] = res.apply(lambda row: get_ptm_sites(row['modified_sequence'],
                                                        modification_reg=mod_reg), axis=1)
    res['PTMtypes'] = res.apply(lambda row: re.findall(mod_reg, row['modified_sequence']), axis=1)
    return res

# Cell

def format_input_data(df: pd.DataFrame, fasta: fasta, modification_exp: str, verbose:bool = True):
    """
    Function to format input data and to annotate sequence start and end positions plus PTM sites.

    Args:
        df (pd.DataFrame): Experimental data that was imported by the 'import_data' function.
        fasta (fasta): Fasta file imported by pyteomics 'fasta.IndexedUniProt'.
        modification_exp (str): Regular expression for the modifications.
        verbose (bool, optional): Flag to print warnings if no matching sequence is found for a protein in the provided fasta. Defaults to 'True'.
    Returns:
        pd.DataFrame: Dataframe with unique uniprot accessions, sequence start and end positions, and PTM site information.

    """
    res = df.copy(deep=True)
    res = expand_protein_ids(res)
    res = get_peptide_position(res, fasta = fasta, verbose=verbose)
    res = get_modifications(res, mod_reg = modification_exp)
    return res