### Weave Declarations -- C++ Implementation ###

def PSFModel_Weave(xy, cen, Param, der = []):
    from copy import deepcopy
    '''
    Routine that produces the PSF profile and its derivatives using C++ code called through Weave inline.
    
    Note: As the code is compiled for the first run and then run from precompiled code, it may be the case that the code will be quickest when compiled in seperate routines
    
    Param can have two possible interpreatations: one is a list or parameters, the other is a generic dictionary or individual parameters. This version takes the former, where der is a logical

    To Do:
    Comment
    Introduce Checks for the existence 
    
    '''
    
    from scipy import weave
    import numpy as np
    
    nX = xy[0].shape[0]; nY = xy[1].shape[0]
    
    dx = xy[0]-cen[0]
    dy = xy[1]-cen[1]
    SB = np.zeros((xy[0].shape[0], xy[1].shape[0]))
    
    if(cen[0] > xy[0].max() or cen[0] < xy[0].min()):
        raise ValueError('gaussian_SBProfile_Weave - Centroid (x) lies outwith the range of the PS, FATAL :'+str(cen))
    if(cen[1] > xy[1].max() or cen[1] < xy[1].min()):
        raise ValueError('gaussian_SBProfile_Weave - Centroid (y) lies outwith the range of the PS, FATAL :'+str(cen))

    iParam = deepcopy(Param)

    ##Set up initial bit of code, generic for all PSF models
    #Pos here accounts for the fact that apparently weave works on flattened arrays
    code = r"""
    int i;
    int j;
    int Pos;
    for(i = 0; i < nX; i++){
    for(j = 0; j < nY; j++){
    Pos = i*nX + j;
    SB[Pos] = """
    
    codeTail = r"""}}"""


    if(iParam['PSF_Type'] == 1 or str(iParam['PSF_Type']).lower() == 'gaussian'):
        ## Elliptical Gaussian PSF: Use known output for SB profile
        ##Rename variables to fit in with Sympy output

        ''' These variables are not used, as the Guassian SB profile routines are instead used, but are left here as instructional
        e1 = ie1
        e2 = ie2
        size = isigma
        flux = 1.0 #Set to one to enusre int(P) = 1 (normalised)
    
        weaveVar = ['SB', 'flux', 'e1', 'e2', 'size', 'dx', 'dy', 'nX', 'nY']

        weaveArgs = [SB, flux, e1, e2, size, dx, dy, nX, nY, weaveVar, code, codeTail]
        '''

        ##Use SB profile code
        from surface_Brightness_Profiles import gaussian_SBProfile_Weave
            
        psf = gaussian_SBProfile_Weave(xy, cen, iParam['PSF_size'], iParam['PSF_Gauss_e1'], iParam['PSF_Gauss_e2'], 1.0, der = der)


    return psf.copy()
        

