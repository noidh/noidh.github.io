function Header(headerId)
{
    document.getElementById(headerId).innerHTML = `
<div  style="width: 270px; float: left;">
    <h2>Doan Huu Noi</h2>
    <h4></h4><p><a><< doanhuunoi@gmail.com >></a></p></h4>
    <p style="word-wrap: break-word;">I'm an enthusiastic researcher in Image Processing and Computer Vision. Learning new theories and bringing them to practice is my hobby. My research topics are Pattern Matching, Stereo-Vision Reconstruction, and other Miscellaneous.</p>
</div>
<div style="float: left;">
    <img style="height: 220px;" src="https://noidh.github.io/header.jpg">
</div>`;
}

function BlogImageProcessing(elementId)
{
    document.getElementById(elementId).innerHTML = `
<p>
    <ol>
        <li><a href="./pages/notes/ip/gaussian/gaussian.html">Gaussian Filter</a></li>
        <li><a href="./pages/notes/ip/fast_median_sorting_network/fast_median.html">Fast Median Fiter by using Sorting Network</a></li>
        <li><a>Fast Median Filter By Histogram</a></li>	
        <li><a href="./pages/notes/ip/integral/integral.html">Integral Image, Integral Histogram</a></li>	
        <li><a href="./pages/notes/ip/hist_equalization/hist_equalization.html">Histogram Equalization</a></li>	
        <li><a>Adaptive Histogram Equalization</a></li>
        <li><a>In-Painting</a></li>	
        <li><a>Fourier Transform</a></li>	
        <li><a>Color Model</a></li>	
        <li><a>Interpolation</a></li>
    </ol>
</p>
    `;
}

function BlogComputerVision(elementId)
{
    document.getElementById(elementId).innerHTML = `
<p>
    <ol>
        <li><a href="./pages/notes/ip/harris/harris.html">Harris Corner Detector</a></li>
        <li><a href="./pages/notes/ip/canny/canny.html">Canny Edge Detector</a></li>
        <li><a href="./pages/notes/ip/hough_line/hough_line.html">Hough Line Transform</a></li>
        <li><a>Hough Circle Transform </a></li>
        <li><a href="./pages/notes/ip/leastsquare_matrix/leastsquare_matrix.html">Linear Least Square Approximation by Matrix Method</a></li>
        <li><a href="./pages/notes/ip/ncc/ncc.html">Fast Normalized Cross Correlation</a></li>
        <li><a>Feature-based Template Matching </a></li>
        <li><a href="./pages/notes/ip/hog/hog.html">Histogram of Oriented Gradient Transform</a></li>	
        <li><a>SIFT </a></li>
        <li><a>Grapth Cut Segmentation </a></li>
        <li><a>3D Warping </a></li>
        <li><a>Camera Calibration </a></li>
        <li><a>K-Mean Segmentation </a></li>
        <li><a>Background subtraction by Code Book </a></li>
        <li><a>Optical Flow </a></li>
        <li><a>Contour Approximation </a></li>
        <li><a>Kalman Filter </a></li>
        <li><a>Find Homography Matrix </a></li>
    </ol>
</p>
    `;
}

function Blog3DRendering(elementId)
{
    document.getElementById(elementId).innerHTML = `
<p>
    <ol>
        <li><a href="./pages/notes/gl/simple_rendering_3d/opengl_notes_simple_rendering_3d.html">A Simple 3D Rendering by QT and OpenGL</a></li>
        <li><a href="./pages/notes/gl/simple_earth_3d/simple_earth_3d.html">A Simple 3D Earth by QT and OpenGL</a></li>
        <li><a href="./pages/notes/gl/simple_lighting/simple_lighting.html">Basic of Lighting Model in OpenGL</a></li>
        <li><a href="./pages/notes/gl/simple_3d_web_threejs/simple_lighting.html">Simple 3D Rendering on Web by using Threejs</a></li>
    </ol>
</p>
    `;
}

function BlogMachineLearning(elementId)
{
    document.getElementById(elementId).innerHTML = `
<p>
    <ol>
        <li><a href="./pages/notes/ml/linear_regression/linear_regression.html">Linear Regression</a></li>	
        <li><a href="./pages/notes/ml/logistic_regression/logistic_regression.html">Logistic Regression</a></li>		
        <li><a href="./pages/notes/ml/pca/pca.html">Principal Component Analysis</a></li>		
        <li><a href="./pages/notes/ml/svm/svm.html">Support Vector Machine</a></li>	
        <li><a>Naive Bayes Classification</a></li>	
        <li><a>Ransac Clustering</a></li>	
        <li><a>K-Mean Clustering</a></li>	
        <li><a>Background Subtraction by Codebook</a></li>	
        <li><a>Background Subtraction by GMM</a></li>
        <li><a>Artificial Neural Networks</a></li>

        <!--The Implicit Values of A Good Hand Shake:
Handheld Multi-Frame Neural Depth Refinement https://arxiv.org/pdf/2111.13738.pdf-->
    </ol>
</p>  
    `;
}