This repository contains the code for TestAI, a system designed to accept detailed API calls, execute testing steps using Robot Framework, and return the test results. Below you will find instructions on setting up and using the TestAI API.
First of to run this in your machine do the following steps provided:
1.Clone the Repository: Clone this repository to your local machine using the following command:
git clone https://github.com/your-username/testai.git
2.After completing the clone we have to run by activating the virtualenvironment by following command:
cd myenv/scripts
3.Activate the virtualenvironment by the command:
activate
4.Database Migration: If using a database, perform migrations to set up the database schema:
python manage.py migrate
Run the Server: Start the Django development server:
python manage.py runserver



API ENDPOINT:
The TestAI API endpoint is located at http://127.0.0.1:8000/testai/tests/v1/execute. Below are the details of the endpoint:

Method: POST
Headers: Content-Type: application/json
Body:
 
{
 "tests":[
 {
 "title":"Open google.com with Chrome",
 "steps":[
 "Open Browser   https://google.com   Chrome"
 
 ]
 }
 ]
}



Usage
To use the TestAI API, send a POST request to the endpoint with the test details in the JSON payload. Each test case should have a title and an array of steps to be executed by the Robot Framework. Upon receiving the request, the system will execute the tests and return the results.

Technologies Used
Python: The main programming language used for the project.
Django: The web framework used to create the API endpoint.
Robot Framework: The test automation framework used for executing test steps.



Some Screenshots after hitting the apiendpoint:

1.
![Screenshot (13)](https://github.com/harikrishnanakka/robot-framework/assets/152170400/136fe6ca-ea59-4641-bfee-948f804eca8e)
I just tested the apiendpoint by the Postman by sending the POST request as shown above and it successfully created the record.


2.
![Screenshot (14)](https://github.com/harikrishnanakka/robot-framework/assets/152170400/4598355e-fa7a-4c5f-8997-f9b151841ea2)
After the completing the hitting the endpoint sending post request i used following command whether it was working or not by following command:
robot temp_test_suite.robot
The above command will execute the robot file and shows the above output and testcase will get passed.
NOTE:Make sure before running the the .robot file you have to import the module like:

***settings***
Library SeleniumLibrary

The  above import will have the class of Open Browser so we should definitely import that library.



3.
![Screenshot (15)](https://github.com/harikrishnanakka/robot-framework/assets/152170400/6daed2b9-55aa-4832-b230-001d84ac8199)
You can see the output after runnig the robot file by the above figure


Contributing
If you'd like to contribute to TestAI, please fork the repository, make your changes, and submit a pull request. We welcome any contributions, including bug fixes, feature enhancements, and documentation improvements.
