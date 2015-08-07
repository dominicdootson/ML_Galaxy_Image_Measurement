'''
Author: cajd
Touch Date: 14th May 2015
Purpose: Contains the code to implement a maximum-likelihood based estimator for image model parameters

To Do:
Output residuals after ML estimate found

Versions:

Surface Brightness Models Implemented:
Gaussian |N|
Sersic |N|

Model Parameters:
-SB Profile:
Radius |N|
Ellipticity (e) |N|
Centroid (x,y) |N|
Total Flux (It) |N|

-Lensing
Convergence/Magnfication |N|
Shear |N| (g)

-PSF |N|
-Background |N|
'''
import galsim
import numpy as np
import os
from copy import deepcopy

verbose = False
debug = False

def estimate_Noise(image, maskCentroid = None):
    '''
    Routine which takes in an image and estiamtes the noise on the image, needed to accurately calculate the expected bias on profile measurements

    First iteration only looks for the mean varaince in pixel value, not taking into account image subtraction

    In reality, the noise should be estimated after subtraction of the source, which may also be done by masking out the source centre and taking the std on the background only (assuming constant sky backgroun)

    *** Noise is known to be too large when the postage stamps size is not large enough, so that the model makes up a significant percentage of the image. One may therefore expect the noise to be too large for small PS sizes. ***

    Agrees well with GALSIM noise var on all SNR provided masCentroid is accurately placed on source centre (tested for ellipticity = 0.)

    Requires:
    -- image: Image of source (2-dimensional numpy array)
    -- maskCentroid: center of mask - used to iteritively mask out source to get an accurate estimate of the background noise after removing the source. If None, then the noise is returned as the standard deviation of the image without masking applied. If not None, then the noise is minimum of the difference between successive runs where the mask is increased by one pixel each side of the centre as passed in.
    '''
    if(maskCentroid is not None):
        res = np.zeros(max(maskCentroid[0], maskCentroid[1], abs(image.shape[0]-maskCentroid[0]), abs(image.shape[1]-maskCentroid[1])))
    else:
        res = np.zeros(1)
        
    maskRad = 0; con = 0
    tImage = image.copy()
    while True:
        con += 1

        maskRad = (con-1)*1 #Done in pixels

        if(maskCentroid is not None):
            tImage[maskCentroid[0]-maskRad:maskCentroid[0]+maskRad, maskCentroid[1]-maskRad:maskCentroid[1]+maskRad] = 0.

        res[con-1] = tImage.std()

        if(maskCentroid == None):
            break
        elif(con == res.shape[0]):
            break

    if(maskCentroid is not None):
        return res[np.argmin(np.absolute(np.diff(res)))]
    else:
        return res[0]
    
##-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o---- ML Estimation   ----o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-##
def find_ML_Estimator(image, fitParams = None, outputHandle = None, setParams = None, modelLookup = None, **iParams):
    import scipy.optimize as opt
    import model_Production as modPro
    '''
    To Do:
    Pass in prior on model parameters

    KNOWN PROBLEMS:
    
    Requires:
    image: 2d array of pixelised image
    fitParams: tuple of strings which satisfy the keywords of iParams:
    ---size {Y}
    ---ellip {Y}
    ---centroid {Y}
    ---flux {Y}

    ---magnification {N}
    ---shear {N}

    GALSIM image declarations (set by image)
    ---stamp_size {Y}
    ---pixel_scale {Y}

    ---modelType: string which defines the surface brightness model which will be fit:
    -----Gaussian [Default] {Y}
    -----Sersic {N}

    outputHandle: file name or file handle of the output. **Result is always appended**. If not passed in, then result is not output

    Model Parameter entry: Model Parameters can be entered using two methods
    setParams: Full Dictionary of initial guess/fixed value for set of parameters. If None, this is set to default set. May not be complete: if not, then model parameters set to default as given in default_ModelParameter_Dictionary()
    iParams: generic input which allows model parameters to be set individually. Keys not set are set to default as given by default_ModelParameter_Dictionary(). Where an iParams key is included in the default dictionary, or setParams, it will be updated to this value (**therefore iParams values have preferrence**). If key not present in default is entered, it is ignored

    Side Effects:

    Returns:
    Parameters: tuple of length equal to fitParams. Gives ML estimator for each fit parameter
    '''

    ## Exceptions based on input objects
    if(image is None or sum(image.shape) == 0):
        raise RuntimeError('find_ML_Estimator - image supplied is None or uninitialised')

    ## Set up analysis based on input values
    if(fitParams is None):
        print 'find_ML_Estimator - parameters to be fit (/measured) must be specified - using default:'
        fitParams = ['size', 'e1', 'e2']
        print fitParams
        print ' '

        
    if(len(fitParams) > 2 and modelLookup is not None and modelLookup['useLookup']):
        raise RuntimeError('find_ML_Estimator - Model Lookup is not supported for more than double parameter fits')

    ##Set up initial params, which sets the intial guess or fixed value for the parameters which defines the model
    ##This line sets up the keywords that are accepted by the routine
    ## pixle_Scale and size should be in arsec/pixel and arcsec respectively. If pixel_scale = 1., then size can be interpreted as size in pixels
    ## centroid should be set to the center of the image, here assumed to be the middle pixel

    if(setParams is None):
        initialParams = modPro.default_ModelParameter_Dictionary()
    else:
        initialParams = modPro.default_ModelParameter_Dictionary()
        initialParams.update(setParams)

    ## This could be done by initialParams.update(iParams), however theis does not check for unsupported keywords
    failedKeyword = 0
    for kw in iParams.keys():
        if kw not in initialParams:
            print 'find_ML_Estimator - Initial Parameter Keyword:', kw, ' not recognised'
            failedKeyword += 1
        else:
            initialParams[kw] = iParams[kw]
    if(failedKeyword > 0 and verbose):
        ##Remind user of acceptable keywords.
        print '\n Acceptable keywords:'
        print intialParams.keys()
        print ' '

    ## Define dictionary ``Params'', which stores values which are being varied when evaluating the likelihood
    
    modelParams = deepcopy(initialParams)

    ####### Search lnL for minimum
    #Construct initial guess for free parameters by removing them from dictionary
    x0 = modPro.unpack_Dictionary(modelParams, requested_keys = fitParams)

    ##Find minimum chi^2 using scipy optimize routine
    ##version 11+ maxima = opt.minimize(get_logLikelihood, x0, args = (fitParams, image, modelParams))
    #maxima = opt.fmin(get_logLikelihood, x0 = x0, args = (fitParams, image, modelParams, modelLookup, 'sum'), disp = (verbose or debug))

    maxima = opt.fmin_powell(get_logLikelihood, x0 = x0, args = (fitParams, image, modelParams, modelLookup, 'sum'), disp = (verbose or debug))

    ##Output Result
    if(outputHandle is not None):
        np.savetxt(outputHandle, np.array(maxima).reshape(1,maxima.shape[0]))

    if(debug):
        ##Plot and output residual
        fittedParams = deepcopy(modelParams)
        for i in range(len(fitParams)):
            fittedParams[fitParams[i]] =  maxima[i]
 
        model, disc =  modPro.user_get_Pixelised_Model(fittedParams, sbProfileFunc = modPro.gaussian_SBProfile)
        residual = image-model

        import pylab as pl
        ##Plot image and model
        f = pl.figure()
        ax = f.add_subplot(211)
        ax.set_title('Model')
        im = ax.imshow(model, interpolation = 'nearest')
        pl.colorbar(im)
        ax = f.add_subplot(212)
        ax.set_title('Image')
        im = ax.imshow(image, interpolation = 'nearest')
        pl.colorbar(im)

        pl.show()

        ##Plot Residual
        f = pl.figure()
        ax = f.add_subplot(111)
        im = ax.imshow(residual, interpolation = 'nearest')
        pl.colorbar(im)
        pl.show()

        

    ##Return minimised parameters
    return maxima



def get_logLikelihood(parameters, pLabels, image, setParams, modelLookup = None, returnType = 'sum'):
    import math, sys
    import model_Production as modPro
    import generalManipulation
    '''
    Returns the log-Likelihood for I-Im, where Im is image defined by dictionary ``modelParams'', and I is image being analysed.
    Minimisiation routine should be directed to this function

    Requires:
    parameters: flattened array of parameters to vary (allows for external program to set variation in these params)
    pLabels: tuple of length `parameters`, which is used to identify the parameters being varied. These labels should satisfy the modelParameter dictionary keys using in setting up the model
    image: 2d <ndarray> of pixelised image
    setParams: dictionary of fixed model parameters which sets the model SB profile being fit.
    modelLookup: An instance of the model lookup table, as set in model_Production module
    returnType:
    ---`sum`: Total log-likelihood, summing over all pixels
    ---`pix`: log-likelihood evaluated per pixel. Returns ndarray of the same shape as the input image

    Returns:
    lnL <scalar>: -1*log_likelihood evaulated at entered model parameters

    Known Issue: Splitting input parameters set into model does not work if a particular key of the dictionary corresponds to anything other than a scalar (e.g. tuple ofr array)
    '''

    ##Set up dictionary based on model parameters. Shallow copy so changes do not overwrite the original
    modelParams = deepcopy(setParams)

    if(setParams['stamp_size'] != image.shape):
        raise RuntimeError('get_logLikelihood - stamp size passed does not match image:', str(setParams['stamp_size']), ':', str( image.shape))

    parameters = generalManipulation.makeIterableList(parameters); pLabels = generalManipulation.makeIterableList(pLabels)
    if(len(parameters) != len(pLabels)):
        raise ValueError('get_logLikelihood - parameters and labels entered do not have the same length (iterable test): parameters:', str(parameters), ' labels:', str(pLabels))


    ##Vary parameters which are being varied as input
    for l in range(len(pLabels)):
        if(pLabels[l] not in modelParams):
            raw_input('Error setting model parameters in get_logLikelihood: Parameter not recognised. <Enter> to continue')
        else:
            modelParams[pLabels[l]] = parameters[l]

    #Test reasonable model values - Effectively applying a hard prior
    if(math.sqrt(modelParams['e1']**2. + modelParams['e2']**2.) >= 0.99):
        ##Set log-probability to be as small as possible
        return sys.float_info.max/10 #factor of 10 to avoid any chance of memory issues here
        #raise ValueError('get_logLikelihood - Invalid Ellipticty values set')
    if(modelParams['size'] <= 0.):
        return sys.float_info.max/10

    ''' Get Model'''
    if(modelLookup is not None and modelLookup['useLookup']):
        model = np.array(modPro.return_Model_Lookup(modelLookup, parameters)[0]) #First element of this routine is the model image itself
    else:
        model, disc = modPro.user_get_Pixelised_Model(modelParams, sbProfileFunc = modPro.gaussian_SBProfile)

    ''' Model, lookup comparison '''
    '''
    modelEx, disc = modPro.user_get_Pixelised_Model(modelParams, sbProfileFunc = modPro.gaussian_SBProfile)
    print 'Model, lookup Comparison:', (model-modelEx).sum(), parameters
    import pylab as pl
    f = pl.figure()
    ax = f.add_subplot(211)
    im = ax.imshow(modelEx-model); ax.set_title('model - lookup'); pl.colorbar(im)
    ax = f.add_subplot(212)
    im = ax.imshow(modelEx/model); ax.set_title('model/lookup'); pl.colorbar(im)
    pl.show()
    '''

    if(model.shape != image.shape):
        raise ValueError('get_logLikelihood - model returned is not of the same shape as the input image.')
    
    #Construct log-Likelihood assuming Gaussian noise. As this will be minimised, remove the -1 preceeding
    if(verbose):
        print 'Noise in ln-Like evualtion:', modelParams['noise']
    pixlnL =  (np.power(image-model,2.))
    lnL = pixlnL.sum()
    pixlnL *= 0.5/(modelParams['noise']**2.); lnL *= 0.5/(modelParams['noise']**2.)

    ##Model is noise free, so the noise must be seperately measured and passed in
    ## Answer is independent of noise provided invariant across image
    #lnL2 = 0.5*( (np.power(image-model,2.)).sum()/(modelParams['noise']**2.))
    if(returnType.lower() == 'sum'):
        return lnL
    elif(returnType.lower() == 'pix'):
        return pixlnL
    elif(returnType.lower() == 'all'):
        return [lnL, pixlnL]


###---------------- Derivatives of log-Likelihood -----------------------------------------------###

def differentiate_logLikelihood_Gaussian_Analytic(parameters, pLabels, image, setParams, modelLookup = None):
    import generalManipulation
    ## May need returnType passed in

    '''
    Returns the derivative of the Gaussian log-Likelihood (ignoring parameter-independent prefactor) for parameters labelled by pLabels.
    Uses analytic derivative of the pixelised model as given in differentiate_Pixelised_Model_Analytic routine of model_Production routine.

    Note: `noise` as defined in set params must the noise_std, and must accurately describe the noise properties of the image. 

    Requires:
    parameters: flattened array of parameters to vary (allows for external program to set variation in these params)
    pLabels: tuple of length `parameters`, which is used to identify the parameters being varied. These labels should satisfy the modelParameter dictionary keys using in setting up the model
    image: 2d <ndarray> of pixelised image
    setParams: dictionary of fixed model parameters which sets the model SB profile being fit.
    modelLookup: An instance of the model lookup table, as set in model_Production module

    Returns:
    [dlnL/dbeta], repeated for all beta in order <1D ndarray>: derivative of -1*log_likelihood evaulated at entered model parameters


    '''
    
    ##To be useful as part of a minimisation routine, the arguements passed to this function must be the same as those passed to the ln-Likelihood evalutaion also. This suggest possibly two routines: one, like the model differentiation itself should just return the various derivatives, and a wrapper routine which produces only the relevent derivatives required for mimimisation
    ## Third order is ignored for now, as this wold require an edit to the methdo of calculating model derivatives, and it is unlikely that a third order derivative would ever really be necessary (excpet in the case where an analytic derivative of the model is wanted for the calculation of the bias, where simulations over many images are used: usually, the known statistics of the Gaussian lileihood can be used to remove this necessity anyway).


    ### First derivative only are needed, so for now this will be coded only to deal with first derivatives.
    ### Therefore, n = 1, permute = false by default
    ### Note, that this code is unlikely to speed up any computation provided that the derivative is calculated using SymPY. Therefore this must be addressed.

    ### Set up model parameters as input
    ##Set up dictionary based on model parameters. Shallow copy so changes do not overwrite the original
    modelParams = deepcopy(setParams)

    if(setParams['stamp_size'] != image.shape):
        raise RuntimeError('differentiate_logLikelihood_Gaussian_Analytic - stamp size passed does not match image:', str(setParams['stamp_size']), ':', str( image.shape))

    ##Check whether parameters input are iterable and assign to a tuple if not: this allows both `parameters' and `pLabels' to be passed as e.g. a float and string and the method to still be used as it
    parameters = generalManipulation.makeIterableList(parameters); pLabels = generalManipulation.makeIterableList(pLabels)
    if(len(parameters) != len(pLabels)):
        raise ValueError('get_logLikelihood - parameters and labels entered do not have the same length (iterable test)')

    ##Vary parameters which are being varied as input
    for l in range(len(pLabels)):
        if(pLabels[l] not in modelParams):
            raw_input('Error setting model parameters in get_logLikelihood: Parameter not recognised. <Enter> to continue')
        else:
            modelParams[pLabels[l]] = parameters[l]

    ''' Get Model'''
    if(modelLookup is not None and modelLookup['useLookup']):
        model = np.array(modPro.return_Model_Lookup(modelLookup, parameters)[0]) #First element of this routine is the model image itself
    else:
        model, disc = modPro.user_get_Pixelised_Model(modelParams, sbProfileFunc = modPro.gaussian_SBProfile)


    ''' Get model derivatives '''
    modDer = modPro.differentiate_Pixelised_Model_Analytic(modelParams, parameters, pLabels, n = 1, permute = False)
    #modDer stores only the n'th derivative of all parameters entered, stored as an nP*nPix*nPix array.

    ##Construct the result to be returned. This is a scalar array, with length equal to nP, and where each element corresponds to the gradient in that parameter direction
    nP = len(parameters)
    delI = image - model

    res = np.zeros(nP)

    ##Create tdI, which stores dI in the same shape as modDer
    tdelI = np.zeros(modDer.shape); tdelI[:] = delI.copy()
    ##Alternatively: tdelI = np.repeat(delI.reshape((1,)+delI.shape), modDer.shape[0], axis = 0)

    ##Set derivative as sum_pix(delI*derI)/sig^2 for all parameters entered
    res = (tdI*modDer).sum(axis = -1).sum(axis = -1)
    res /= -1.*modelParams['noise']*modelParams['noise']
    ## Note: -ve required as code essentially minimises chi^2

##-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o---- Bias Correction ----o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-##
