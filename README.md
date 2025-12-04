# Ex03 Time Table
## Date: 28/11/2025
## Reg. no: 25019029

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
~~~
<html>
    <head>
        <title>Time Table</title>
        <style>
            table, th, td {
                border: 1px solid black;
             }
        </style>
    </head>
    <body>

        <h3 colspan="4">SLOT TIME TABLE - SASMINA S (25019029)</h3>
        <table id="1" border="50%" width="600" bgcolor="blue">
            <tr class="header-row">
                <th bgcolor="pink">Day/Time</th>
                <th bgcolor="pink">Monday</th>
                <th bgcolor="pink">Tuesday</th>
                <th bgcolor="pink">Wednesday</th>
                <th bgcolor="pink">Thursday</th>
                <th bgcolor="pink">Friday</th>
            </tr>
            <tr>
                <td align="center" bgcolor="purple">8-10</td>
                <td align="center">FWAD</td>
                <td colspan="2" align="center">PHY</td>
                <td colspan="2" align="center">EDM</td>
            </tr>
            <tr>
                <td align="center" bgcolor="purple">10-12</td>
                <td align="center">MAT</td>
                <td align="center">PHY</td>
                <td align="center">FREE SLOT</td>
                <td align="center">FWAD</td>
                <td align="center">PHY</td>
            </tr>
            <tr>
                <td align="center" bgcolor="purple">12-1</td>
                <td colspan="5", align="center">LUNCH</td>
            </tr>
            <tr>
                <td align="center" bgcolor="purple">1-3</td>
                <td align="center">EDM</td>
                <td align="center">MAT</td>
                <td colspan="2" align="center">EDM</td>
                <td align="center">CHE</td>
            </tr>
            <tr>
                <td align="center" bgcolor="purple">3-5</td>
                <td colspan="2" align="center">FREE SLOT</td>
                <td colspan="2" align="center">CHE</td>
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
                <td>19AI302</td>
                <td>Engineering Design and Modelling(EDM)</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>19PH814</td>
                <td>Physics for Engineering(PHY)</td>
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
          </table>
    </body>
</html>
~~~

## OUTPUT


<img width="758" height="612" alt="Screenshot 2025-12-04 113517" src="https://github.com/user-attachments/assets/79f33283-a286-4e52-b441-91b9aa10a035" />


## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
