<h1 style="color:#00dabf;font-weight:bold;font-size:21Px;">Research links</h1>
This is a "basic" but huge link list (thanks to <a href="https://i-intelligence.eu/resources/osint-toolkit">i-intelligence.eu osint-toolkit</a>) to let you the rabbit osint hole.<br>
<br>
This is originaly a PDF, wich is great, but not easy for your daily research.<br>
<hr>
<h2 style="color:#00c2ab;font-weight:bold;font-size:19Px;">PDF 2 JSON</h2>
This pdf, is quite easy to parse. let's use PyMuPDFfitz
<div style="font-family:'Helvetica, Sans-Serif';color:darkgreen;background-color:black;">pip install PyMuPDF</div>
You just have to download the file and
More infos here: <a href="https://github.com/pymupdf/pymupdf">PyMuPDF</a><br>
The code <font color="yellow">PDF_To_JSON.py</font> is a very simple parsing, it retreive link and sections to make a quite simple JSON file...<br>
<br>
<div style="font-family:'Helvetica, Sans-Serif';color:darkgreen;background-color:black;">wget https://i-intelligence.eu/uploads/public-documents/OSINT_Handbook_2020.pdf </div>
<div style="font-family:'Helvetica, Sans-Serif';color:darkgreen;background-color:black;">python3 PDF_To_JSON.py</div>

<hr>
<h2 style="color:#00c2ab;font-weight:bold;font-size:19Px;">Clean Disapeared</h2>
One big problem with those link, is that some are dead or disapeared, so here is a way to exclude dead one. This code, oper the JSON, check if domain still exist, and can alos open the url to see if a error occur, but I strongly disapprouve that usage (because if the domain still exist, it's probably a network trouble)...<br>
<div style="font-family:'Helvetica, Sans-Serif';color:darkgreen;background-color:black;">python3 CleanDisapeared.py</div>

<hr>
<h2 style="color:#00c2ab;font-weight:bold;font-size:19Px;">To Favorites</h2>
We now have a cleaned JSON with thousands of links. Let's make a cool folder in favorite, with all of them.<br>
Why Favorite Folder, we god damn doesn't use IE ????? Yes but's it easy to import in any browser :)<br>
<br>
If you look inside the code, you'll some work/grouping to limit a bit folder's number...<br>
<br>
Just run:<br>
<div style="font-family:'Helvetica, Sans-Serif';color:darkgreen;background-color:black;">python3 ToFavorites.py</div>


<hr>
<h2 style="color:#00c2ab;font-weight:bold;font-size:19Px;">All In One commands</h2>
<div style="font-family:'Helvetica, Sans-Serif';color:darkgreen;background-color:black;">
wget https://i-intelligence.eu/uploads/public-documents/OSINT_Handbook_2020.pdf<br>
python3 PDF_To_JSON.py<br>
python3 CleanDisapeared.py<br>
python3 ToFavorites.py</div>
And you got all this marvellous link directly in your browser order, checked, and classified. :)