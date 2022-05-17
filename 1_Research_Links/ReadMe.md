<style>

/* Full Body */
body {          font-family: "Helvetica", Sans-Serif; color:lightgrey; background-color: black;}
/* command bash */
.bash{          font-family: "Helvetica", Sans-Serif; color:darkgreen; background-color: black;}
.bashcomment{  color:lightblue; font-style: oblique 20deg;}
/* code coloring */
.code{         font-family: "Helvetica", Sans-Serif;  color:white;     background-color: black;}
.codecomment{  color:purple; font-style: oblique 20deg;}

/* Fichiers */
.confFile{     font-family: "Helvetica", Sans-Serif;  color:lightgrey; background-color: black;}
.FileName{     font-family: "Helvetica", Sans-Serif;  color:yellow;    background-color: black;}
/* Table */
table{
    width:  95%;
    border: 1px solid black;
    }
/* Table Title */
table caption { font-size:20Px;}
/* Heading */
table th {
    color:black;
    background-color: #4d4dff;
    border: 1px solid black;
    }
/* Column Width */
table td:nth-child(1){width: 170Px; word-wrap: break-word;border: 1px solid black; font-weight: bold;}
table td:nth-child(2){              word-wrap: break-word;border: 1px solid black;}
table td:nth-child(3){width: 100Px; word-wrap: break-word;border: 1px solid black;}
table td:nth-child(4){width: 50Px;  word-wrap: break-word;border: 1px solid black;}
/* Style line pair */
table tr:nth-child(even) {  color:black; background-color: #e6e6ff;border: 1px solid black;}
table tr:nth-child(odd) {   color:black; background-color: #b3b3ff;border: 1px solid black;}
/* Basic coloring */
.green{ color:green;    font-weight: bold;}
.red{   color:red;      font-weight: bold;}
.orange{color:orange;   font-weight: bold;}
.blue{  color:blue;     font-weight: bold;}
.image{  border:1px solid black;}

/*Titles*/
h1{     color:#00dabf;    font-weight: bold; font-size: 21Px;}
h2{     color:#00c2ab;    font-weight: bold; font-size: 19Px;}
h3{     color:#00af99;    font-weight: bold; font-size: 17Px;}
h4{     color:#00a08d;    font-weight: bold; font-size: 15Px;}
</style>

<h1>Research links</h1>
This is a "basic" but huge link list (thanks to <a href="https://i-intelligence.eu/resources/osint-toolkit">i-intelligence.eu osint-toolkit</a>) to let you the rabbit osint hole.<br>
<br>
This is originaly a PDF, wich is great, but not easy for your daily research.<br>
<hr>
<h2>PDF 2 JSON</h2>
This pdf, is quite easy to parse. let's use PyMuPDFfitz
<div class="bash">pip install PyMuPDF</div>
You just have to download the file and
More infos here: <a href="https://github.com/pymupdf/pymupdf">PyMuPDF</a><br>
The code <font class="FileName">PDF_To_JSON.py</font> is a very simple parsing, it retreive link and sections to make a quite simple JSON file...<br>
<br>
<div class="bash">wget https://i-intelligence.eu/uploads/public-documents/OSINT_Handbook_2020.pdf </div>
<div class="bash">python3 PDF_To_JSON.py</div>

<hr>
<h2>Clean Disapeared</h2>
One big problem with those link, is that some are dead or disapeared, so here is a way to exclude dead one. This code, oper the JSON, check if domain still exist, and can alos open the url to see if a error occur, but I strongly disapprouve that usage (because if the domain still exist, it's probably a network trouble)...<br>
<div class="bash">python3 CleanDisapeared.py</div>

<hr>
<h2>To Favorites</h2>
We now have a cleaned JSON with thousands of links. Let's make a cool folder in favorite, with all of them.<br>
Why Favorite Folder, we god damn doesn't use IE ????? Yes but's it easy to import in any browser :)<br>
<br>
If you look inside the code, you'll some work/grouping to limit a bit folder's number...<br>
<br>
Just run:<br>
<div class="bash">python3 ToFavorites.py</div>


<hr>
<h2>All In One commands</h2>
<div class="bash">
wget https://i-intelligence.eu/uploads/public-documents/OSINT_Handbook_2020.pdf<br>
python3 PDF_To_JSON.py<br>
python3 CleanDisapeared.py<br>
python3 ToFavorites.py</div>
And you got all this marvellous link directly in your browser order, checked, and classified. :)