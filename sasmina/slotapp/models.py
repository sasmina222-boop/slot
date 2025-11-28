from django.db import models
from django.contrib import admin

<html>
    <head>
        <title>Time Table</title>
        <style>
            table, th, td {
                border: 2px solid black;
             }
        </style>
    </head>
    <body>

        <h3 colspan="4" align="center">SLOT TIME TABLE - SASMINA (25019029)</h3>
        <table id="1" border="50%" width="600" bgcolor="cyan">
            <tr class="header-row">
                <th bgcolor="yellow">Day/Time</th>
                <th bgcolor="yellow">Monday</th> 
                <th bgcolor="yellow">Tuesday</th>
                <th bgcolor="yellow">Wednesday</th>
                <th bgcolor="yellow">Thursday</th>
                <th bgcolor="yellow">Friday</th>
            </tr>
            <tr>
                <td align="center" bgcolor="yellow">8-10</td>
                <td colspan="3" align="center" >FREE SLOT</td>
                <td align="center">PHY</td>
                <td align="center">CHE</td>
            </tr>
            <tr>
                <td align="center" bgcolor="yellow">10-12</td>
                <td align="center">GER</td>
                <td align="center">FREE SLOT</td>
                <td align="center">FWAD</td>
                <td align="center">FWAD</td>
                <td align="center">PHY</td>
            </tr>
            <tr>
                <td align="center" bgcolor="yellow">12-1</td>
                <td colspan="5", align="center">LUNCH</td>
            </tr>
            <tr>
                <td align="center" bgcolor="yellow">1-3</td>
                <td colspan="2" align="center">FREE SLOT</td>
                <td align="center">MAT</td>
                <td align="center">MAT</td>
                <td align="center">SS</td>
            </tr>
            <tr>
                <td align="center" bgcolor="yellow">3-5</td>
                <td colspan="2" align="center">FREE SLOT</td>
                <td align="center">GER</td>
                <td align="center">CHE</td>
                <td align="center">FWAD</td>
            </tr>
        </table>

        <br>

        <table id="2" width="600">
            <tr class=""header-row>
                <th>S. No.</th>
                <th>Subject Code</th>
                <th>Subject Name</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>19AI414</td>
                <td>Fundamentals of Web Application Development (FWAD)</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>19EN612</td>
                <td>German Basic (GER)</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>19PH206</td>
                <td>Physics for Information Technology (PHY)</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>19CY205</td>
                <td>Principles of Chemistry in Engineering (CHE)</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>19MA201</td>
                <td>Calculus and Matrix Algebra (MAT)</td>
            </tr>
            <tr>
                <td>6.</td>
                <td>19EY701</td>
                <td>Soft Skills (SS)</td>
            </tr>
        </table>
    </body>
</html>