AUTOMATED_TEST_PROJECT

Unfortunately I chose to check 3 websites,and not 1, on simple functionalities. The evaluation of searching prosucts, login and page check were my main concern. To make sure that all these functions work properly, I checked functionalities such as: sending text, validating error messages, using an invalid email address, etc.

LANGUAGE

I chose to perform the testing using the Python programming language and the PyCharm IDE. I used the Selenium, webdriver-manager, behave and behave-html-formatter libraries to automate the interaction with Emag , Carturesti and TheInternetHerokuapp pages. The "Python Packages" section of PyCharm can be accessed to install these libraries, and after you write the name of the library you nwant to acces, you only need to click the install button above.

THE CHOSEN METHODOLOGY
The software development methodology called BDD (Behavior-Driven Development) focuses on the collaboration of team members and on describing the behavior of the application in a simple language, such as Gherkin. I chose BDD because we can easily create automated tests that reflect the behavior specified by the stakeholders and because we can facilitate comunication between all people interested and working in the project.



USE OF THE PROJECT

Using the project starts by cloning it from GitHub. Access the project, press the green "Code" button, copy the link, navigate on the computer to the desired folder, open Git Bash, write the command "git clone" followed by the link and press "Enter". The cloned project can be opened in PyCharm. To run tests, use the command "behave -f html -o behave-report.html" in the terminal. To view the generated report, open the "behave-report.html" file in Chrome.


STRUCTURE OF THE PROJECT

The project has a structure consisting of a series of files and directories. We find settings for opening Chrome, maximizing the window , coockie accept. We have the structure of the pages tested in the "environment". "features", "pages" and "steps" are the three folders that make up the  structure. The test scenarios are written in Gherkin and can be found in the "features" category. We have general methods for actions such as clicking, finding the element, typing, etc. defined in "pages". The other files contain locators and specific methods for the suggested scenarios. The Gherkin syntax defines the functions of the "steps" directory. This structure organizes the code for automated tests.


![image](https://github.com/Alex980511/automation_testing_framework_limbaj_aplicatie/assets/158834047/2a9cf765-963b-4d34-b90b-2f66d97f0314)
![image](https://github.com/Alex980511/automation_testing_framework_limbaj_aplicatie/assets/158834047/34fbb235-33be-42e7-978d-3bf2ce9f845c)
![image](https://github.com/Alex980511/automation_testing_framework_limbaj_aplicatie/assets/158834047/90d9c33e-add0-454d-946d-b36a5d328554)
![image](https://github.com/Alex980511/automation_testing_framework_limbaj_aplicatie/assets/158834047/162dd178-33a8-44f0-b204-4ebd029dec1e)
![image](https://github.com/Alex980511/automation_testing_framework_limbaj_aplicatie/assets/158834047/c73b5cbd-c5bf-4829-bcb4-9f54ed0a69b5)









SCENARIOS

The scenarios i have tested include :

-Login with invalid email and password

-Login with valid email and passowrd

-Return message check

-Valid product search

-Product title appear check

-Search invalid product

-Check page number

![image](https://github.com/Alex980511/automation_testing_framework_limbaj_aplicatie/assets/158834047/287b8273-c2a2-4fc9-be9b-ced8133fe964)

