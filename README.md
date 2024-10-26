# rule-engine-ATS
The ATS Rule Engine is a Python application designed to evaluate and execute predefined rules on candidate data for automated recruitment processes. It enables organizations to filter and manage candidate applications effectively.

Installation Clone the repository:

git clone cd ats_rule_engine

Install the required dependencies:

pip install -r requirements.txt

Set up the environment variables :

Create a .env file in the project root for configuration.

Run the application:

python main.py

Design Choices

The ATS Rule Engine is designed with modularity in mind, allowing easy addition of new rules and data sources. It employs a simple condition-checking mechanism for evaluating candidate data.

Dependencies List of dependencies required to run the application:

Flask==2.0.1 SQLAlchemy==1.3.23 python-dotenv==0.19.1

Non-Functional Requirements

Security: The application incorporates input validation to prevent injection attacks. 
Performance: Efficient data processing methods are employed to handle large datasets.

Authored By, 
Riya
