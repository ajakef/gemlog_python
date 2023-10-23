__version__ = '1.7.4' # additional bug fixes on GPS timing 
#__version__ = '1.7.3' # improvements to how GPS timing issues are handled 
#__version__ = '1.7.2' # minor improvements to data read functions (not important to most users), and dependency updates (scipy security issue, Python 3.11, build wheels on Ubuntu 22.04) 
#__version__ = '1.7.1' # fixed verify_huddle_test bug with Axes.set_ticks 
#__version__ = '1.7.0' # new command-line tool to make sensor network info, including a stationXML file 
#__version__ = '1.6.9' # added command-line tools to cross-correlate data and invert time lags for slowness and backazimuth, fixed for pypi 
#__version__ = '1.6.8' # added command-line tools to cross-correlate data and invert time lags for slowness and backazimuth 
#__version__ = '1.6.7' # bug fix in verify_huddle_test 
#__version__ = '1.6.6' # version described by JOSS paper 
#__version__ = '1.6.5' # bug fixes and other minor improvements 
#__version__ = '1.6.4' # upgrades dependencies due to moderate security issue in numpy: https://github.com/advisories/GHSA-fpfv-jqm9-f5jm 
#__version__ = '1.6.3' # minor improvements/bug fixes for verify_huddle_test 
#__version__ = '1.6.2' # bug fix 
#__version__ = '1.6.1' # added new tools to convert data with no gps or inadequate gps (at user's own risk!) 
#__version__ = '1.6.0' # now supports raw format 1.10 (compact) 
#__version__ = '1.5.15' # another bug fix affecting edge case (many bad files at beginning) 
#__version__ = '1.5.14' # bug fix affecting edge case 
#__version__ = '1.5.13' # added executable and automated test for verify_huddle_test 
#__version__ = '1.5.12' # requires pandas<1.4 due to new conflict introduced in this version; fixed previous gemlog version name 
#__version__ = '1.5.11' # no longer supporting python 3.10 until the obspy-numpy conflict gets resolved. bug fixed with spurious data gaps/timing issues. 
#__version__ = '1.5.10' # more changes to support python 3.10 
#__version__ = '1.5.9' # improvements to installation process, cython now required 
#__version__ = '1.5.8' # new updates to support python 3.10 
#__version__ = '1.5.7' # support python 3.10 
#__version__ = '1.5.6' # added automated tests for minimum and newest versions to detect dependency incompatibilities 
#__version__ = '1.5.5' # allow deconvolve_gem_response to use non-standard response files, just like get_gem_response 
#__version__ = '1.5.4' # 'new checks for malformed files, added response files for older gems, test improvements' 
#__version__ = '1.5.3' # avoids timing problems caused by insufficient GPS lines in a file 
#__version__ = '1.5.2' # improved user interface to responses and noise specs 
#__version__ = '1.5.1' # added new version/platform info to gemconvert output and logs; improved elevation handling in metadata 
#__version__ = '1.4.3' # removed overlapping samples in output mseed files 
#__version__ = '1.4.2' # 'more flexibility in station_info.txt format' 
#__version__ = '1.4.1' # now uses default 24-hour miniSEED output files 
#__version__ = '1.4.0' # implemented timing corrections 
#__version__ = '1.3.13' # implemented cubic pps interpolation, but not timing correction (yet) 
#__version__ = '1.3.11' # fix bug in make_gem_inventory that affected surveys, where a sensor can move around and become multiple stations 
#__version__ = '1.3.10' # implement .wav file outputs 
#__version__ = '1.3.9' # still trying to get the pypi upload set right 
#__version__ = '1.3.8' # even more workflow fixes 
#__version__ = '1.3.7' # huddle_test improvements, minor change to make_db 
#__version__ = '1.3.6' # minor fix for inventory compliance with IRIS requirements 
#__version__ = '1.3.5' # updated gem_network, demo, and test so that inventory is written with elevation, start/end times for station/network, and azimuth/dip, satisfying IRIS requirements 
#__version__ = '1.3.4' # now supports format 0.91 (same, but with float pps-milliseconds for better clock drift estimation) 
#__version__ = '1.3.3' # bug fixes 
#__version__ = '1.3.2' # new code to merge day-long traces and change file naming format 
#__version__ = '1.3.1' # 'bug fix, and improvements to huddle test' 
#__version__ = '1.3.0' # improvements to gemconvert, added support for older raw file formats, and fixed bugs 
#__version__ = '1.2.7' # more bug fixes 
#__version__ = '1.2.6' # bug fixes to improve support for raw formats 0.8 and 0.85 and to make converting large datasets more reliable 
#__version__ = '1.2.5' # added support for raw format version 0.8 
#__version__ = '1.2.4' # bug fix in convert 
#__version__ = '1.2.3' # Changes to installation procedure (PyPI now available) and minor improvements to gemconvert 
#__version__ = '1.2.2' # debugging deployment code 
#__version__ = '1.2.1' # Run on mix of good raw files, no-gps raw files, and empty files without errors 
#__version__ = '1.2.0' # Handle missing GPS data more gracefully 
#__version__ = '1.1.2' # added output file length option to gemconvert, and fixed some missing_gps issues
#__version__ = '1.1.1' # moved drift correction from block-level to file-level
#__version__ = '1.1.0' # added new gem_cat feature for combining no-GPS files
#__version__ = '1.0.2' # changed make_gem_inventory so that output stationXML passes the stationXML validator: https://github.com/iris-edu/StationXML-Validator/
#__version__ = '1.0.1' # changed 'master' branch to 'main'
#__version__ = '1.0.0' # function name changes (some with aliases) to follow python standards
#__version__  = '0.3.2' # added demo with inventory functions
#__version__  = '0.3.1' #  more helpful logging output
#__version__  = '0.3.0' # 2020-09-04, cython added
#__version__  = '0.2.3' # improving testing, including empty/bad files
#__version__  = '0.2.2' # automated github tests, setup.py improvements, and modelst speed-up
#__version__  = '0.2.1' # 
#__version__ = '0.0.5' # added new functions to make network map from gps data and rename mseeds from serial_number.channel to network.station.location.channel codes
## List of old versions is not comprehensive###########################################################
