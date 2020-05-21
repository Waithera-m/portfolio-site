# portfolio-site
#### The web site displays some of the projects that the creator has worked on 
#### By **Waithera-m**
## Description
Partage is a simple django application that allows users to see some of the projects that the creator has worked on

## Setup/Installation Requirements
To use the application, users need internet access and web browsers, preferably  Chrome, Safari, and Firefox.
## Set-Up a Local Project
### Prerequisites
* django
* pip
* pillow
* bootstrap4
* psycopg2
* postgresql account and database

To set up a local project:
* Fork the repository
* Clone the repository using the git clone command
* Activate a virtual environment
* Install all prerequisites
## Known Bugs
* None at the moment.
## Behavior Driven Development (BDD)
#### Landing Page
![image](https://user-images.githubusercontent.com/60571734/82573571-9bd04380-9b8e-11ea-9ca1-c8817818ff05.png)

#### Projects' Page
![image](https://user-images.githubusercontent.com/60571734/82574449-d5557e80-9b8f-11ea-9307-2e3f2abbe282.png)

#### Details' Page
![image](https://user-images.githubusercontent.com/60571734/82574830-5ca2f200-9b90-11ea-9ae3-4841e2944426.png)


|Behavior                |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads |Users scroll | Users see creator's photo and greeting|
|The landing page loads|Users click on project navbar link|Users are directed to projects template where they see all saved projects|
|The projects page loads|Users click on learn more about project link |Users see details particular to a given project|
|The details page loads|Users click on view repo link|Users are directed to the github repo associated with the project|
## Technologies Used
* HTML - HTML dictates the structure of webpages.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [django](https://www.djangoproject.com/) -  django is a Python web framework.The framework's apps and generic views were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the the created app and installed extensions loop through and display saved posts and navigate to different views. 
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
## Demo
You can view changes made to the website by visiting this working live demo: 
### License
*MIT*
MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) 2020 **Waithera-m**