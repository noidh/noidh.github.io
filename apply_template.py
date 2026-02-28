#!/usr/bin/env python3
"""Apply the portfolio template to all nested HTML sub-pages."""

import os
import re

# (path from repo root, root prefix for assets/links, page title, has MathJax)
PAGES = [
    # pages/sw (R = ../../../)
    ("pages/sw/ximagetool/ximagetool.html", "../../../", "XImage Tool", False),
    ("pages/sw/ximage2text/ximagetotext.html", "../../../", "XText", False),
    ("pages/sw/ximage_trainer/ximage_trainer.html", "../../../", "XImage Trainer", False),
    # pages/notes/ip (R = ../../../../)
    ("pages/notes/ip/gaussian/gaussian.html", "../../../../", "Gaussian Filter", True),
    ("pages/notes/ip/fast_median_sorting_network/fast_median.html", "../../../../", "Fast Median Filter", False),
    ("pages/notes/ip/canny/canny.html", "../../../../", "Canny Edge Detector", True),
    ("pages/notes/ip/harris/harris.html", "../../../../", "Harris Corner Detector", True),
    ("pages/notes/ip/simple_feature_matching/simple_feature_matching.html", "../../../../", "Simple Feature Matching", False),
    ("pages/notes/ip/color_model/color_model.html", "../../../../", "Color Model", True),
    ("pages/notes/ip/integral/integral.html", "../../../../", "Integral Image", True),
    ("pages/notes/ip/hough_line/hough_line.html", "../../../../", "Hough Line Transform", True),
    ("pages/notes/ip/dibr/dibr.html", "../../../../", "Depth Image Based Rendering", True),
    ("pages/notes/ip/mean_filter/mean_filter.html", "../../../../", "Mean Filter", True),
    ("pages/notes/ip/leastsquare_matrix/leastsquare_matrix.html", "../../../../", "Linear Least Square", True),
    ("pages/notes/ip/hist_equalization/hist_equalization.html", "../../../../", "Histogram Equalization", True),
    ("pages/notes/ip/hog/hog.html", "../../../../", "HOG", True),
    ("pages/notes/ip/camera_calibration/camera_calibration.html", "../../../../", "Camera Calibration", True),
    ("pages/notes/ip/interpolation/interpolation.html", "../../../../", "Interpolation", True),
    ("pages/notes/ip/ncc/ncc.html", "../../../../", "Fast NCC", True),
    # pages/notes/ml
    ("pages/notes/ml/pca/pca.html", "../../../../", "PCA", True),
    ("pages/notes/ml/logistic_regression/logistic_regression.html", "../../../../", "Logistic Regression", True),
    ("pages/notes/ml/linear_regression/linear_regression.html", "../../../../", "Linear Regression", True),
    ("pages/notes/ml/svm/svm.html", "../../../../", "SVM", True),
    # pages/notes/gl
    ("pages/notes/gl/simple_lighting/simple_lighting.html", "../../../../", "Simple Lighting", False),
    ("pages/notes/gl/simple_rendering_3d/opengl_notes_simple_rendering_3d.html", "../../../../", "Simple 3D Rendering", False),
    ("pages/notes/gl/simple_3d_web_threejs/simple_lighting.html", "../../../../", "Three.js Lighting", False),
    ("pages/notes/gl/simple_earth_3d/simple_earth_3d.html", "../../../../", "Simple 3D Earth", True),
    # pages/notes/miscellanseous (R = ../../)
    ("pages/notes/miscellanseous/notes_c.html", "../../", "Notes C", False),
    ("pages/notes/miscellanseous/notes_cuda.html", "../../", "Notes CUDA", False),
    ("pages/notes/miscellanseous/notes_simd.html", "../../", "Notes SIMD", False),
    # pages/basic
    ("pages/basic/fast_sobel/fast_sobel.html", "../../", "Fast Sobel", False),
]

HEAD_TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Doan Huu Noi</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{root}index_css.css">
    <script src="{root}index.js"></script>
{mathjax}
</head>
<body>
    <div id="header" class="site-header"></div>
    <script>Header("header");</script>

    <div class="layout">
        <aside class="sidebar" aria-label="Site navigation">
            <nav class="nav">
                <div class="nav_item">
                    <a href="{root}index.html" class="nav_link">Home</a>
                </div>
                <div class="nav_item nav_item--dropdown">
                    <a href="{root}project.html" class="nav_link">Personal Projects</a>
                    <ul class="nav_dropdown">
                        <li><a href="{root}pages/sw/ximagetool/ximagetool.html">XImage Tool</a></li>
                        <li><a href="{root}pages/sw/ximage2text/ximagetotext.html">XText</a></li>
                    </ul>
                </div>
                <div class="nav_item nav_item--dropdown">
                    <a href="{root}blog.html" class="nav_link nav_link--current">Technical Blog</a>
                    <ul class="nav_dropdown">
                        <li><a href="{root}notes_ip.html">Image Processing</a></li>
                        <li><a href="{root}notes_cv.html">Computer Vision</a></li>
                        <li><a href="{root}notes_ml.html">Machine Learning</a></li>
                        <li><a href="{root}opengl_notes.html">3D Rendering</a></li>
                        <li><a href="{root}notes_miscellaneous.html">Miscellaneous</a></li>
                    </ul>
                </div>
            </nav>
        </aside>

        <main class="content">
            <section class="section page-prose">
'''


def make_mathjax():
    return '    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>\n    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js"></script>'


def extract_content(text):
    """Extract content between introduction div and </body>."""
    # Find start: after <div class="introduction"> (with optional attributes/whitespace)
    intro_match = re.search(r'<div\s+class="introduction"[^>]*>\s*\n', text, re.IGNORECASE)
    if not intro_match:
        # Some pages have custom header then navigation then introduction
        intro_match = re.search(r'<div\s+class="introduction">\s*\n', text)
    if not intro_match:
        # Fallback: after first occurrence of class="introduction"
        idx = text.find('class="introduction"')
        if idx == -1:
            return None
        # Find the end of this opening tag (next >)
        end_tag = text.index('>', idx)
        # Content starts after the newline following
        start = end_tag + 1
        content_start = text.find('\n', start) + 1 if '\n' in text[start:start+10] else start
    else:
        content_start = intro_match.end()

    body_idx = text.find('</body>')
    if body_idx == -1:
        return None
    content_end = body_idx
    # Back up past trailing whitespace and optional closing </div>
    content = text[content_start:content_end]
    content = content.rstrip()
    if content.endswith('</div>'):
        content = content[:-6].rstrip()
    return content


def apply_template(repo_root, rel_path, root_prefix, title, has_mathjax):
    path = os.path.join(repo_root, rel_path)
    if not os.path.isfile(path):
        print("Skip (not found):", rel_path)
        return False
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    content = extract_content(text)
    if content is None:
        print("Skip (no introduction):", rel_path)
        return False
    mathjax_block = '\n' + make_mathjax() + '\n' if has_mathjax else ''
    head = HEAD_TEMPLATE.format(
        root=root_prefix,
        title=title,
        mathjax=mathjax_block,
    )
    closing = '''
            </section>
        </main>
    </div>
</body>
</html>
'''
    new_text = head + content + closing
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("OK:", rel_path)
    return True


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    for rel_path, root, title, has_mathjax in PAGES:
        apply_template(repo_root, rel_path, root, title, has_mathjax)


if __name__ == '__main__':
    main()
