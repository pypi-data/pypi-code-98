
import os
import numpy as np
import pandas
from . import spectroscopy, lightcurve

class Sample( object ):
    
    def __init__(self, data, use_dask=True):
        """ """
        self._data = data
        self._use_dask = use_dask
        
    @classmethod
    def from_directory(cls, directory, load_spectra=True, load_lightcurves=True, use_dask=True):
        """ """
        data = pandas.read_csv( os.path.join(directory, "ztfIa_tnsinfo.csv"))
        this = cls(data, use_dask=use_dask)
        this._names = pandas.read_csv( os.path.join(directory, "full_ztfIalist.csv") )
        this._specinfo = pandas.read_csv( os.path.join(directory, "ztf_tns_spectra_list.csv") )
        this._directory = directory
        if load_lightcurves:
            this.load_lightcurves()
            
        if load_spectra:
            this.load_spectra()
            
        return this
        
        
    # =============== #
    #  Methods        #
    # =============== #
    # -------- #
    #  LOADER  #
    # -------- #
    def load_spectra(self, directory=None):
        """ """
        if directory is None:
            if not hasattr(self, "_directory"):
                raise AttributeError("Sample Instance not loaded from a directory, please provide the spectra directory")
            directory = os.path.join(self._directory,"spectra")
            
        self._spectra = spectroscopy.Spectra.from_directory(directory, use_dask=self._use_dask)
        
    def load_lightcurves(self, directory=None):
        """ """
        if directory is None:
            if not hasattr(self, "_directory"):
                raise AttributeError("Sample Instance not loaded from a directory, please provide the spectra directory")
            directory = os.path.join(self._directory,"lightcurves")
            
        self._lightcurves = lightcurve.LightCurveCollection.from_directory(directory, use_dask=self._use_dask)
        
    # -------- #
    #  GETTER  #
    # -------- #
    def get_target_data(self, name):
        """ """
        return self.data.query(f"ztfname == '{name}'").iloc[0]
        
    def show_target(self, name):
        """ """
        import matplotlib.pyplot as mpl
        from astropy.time import Time
        fig = mpl.figure(figsize=[9,3.5])
        axlc = fig.add_axes([0.09, 0.2, 0.35, 0.65])
        axsp = fig.add_axes([0.51, 0.2, 0.45, 0.65])
        # - Plotting
        # -- LC
        self.lightcurves.show_target(name, ax=axlc)
        # -- Spectra    
        targetspectra = self.spectra.get_target_spectra(name)
        targetspectra.show(ax=axsp, sortby="date", topfirst=True, 
                            label="_meta_noname_")
        # -- Spectral Time -> LC plot    
        datetime_spec = Time(targetspectra.meta["date"].sort_values()).datetime
        [axlc.axvline(d_, color=f"C{i}", lw=2, ymin=1.01, ymax=1.02, clip_on=False, zorder=10) 
         for i, d_ in enumerate(datetime_spec)]

        fig.text(0.09,0.95, self._get_target_label_(name), 
                va="top", ha="left", weight="bold", color="0.7", 
                fontsize="small")
        axlc.tick_params(labelsize="small")
        axsp.tick_params(labelsize="small")
        
        return fig
    
    def _get_target_label_(self, name):
        """ """
        data_ = self.get_target_data(name)
        if data_.iau is np.NaN:
            info = name
        else:
            info = f"{name} ({data_.iau})"
        
        info += f" | {data_.ra} {data_.dec} | z={data_.z}"
        return info
        
    # =============== #
    #  Properties     #
    # =============== #
    @property
    def data(self):
        """ """
        return self._data
    
    @property
    def lightcurves(self):
        """ """
        if not hasattr(self,"_lightcurves"):
            return None
        
        return self._lightcurves
    
    @property
    def spectra(self):
        """ """
        if not hasattr(self,"_spectra"):
            return None
        
        return self._spectra
    
    @property
    def names(self):
        """ """
        return self.data["ztfname"].values
