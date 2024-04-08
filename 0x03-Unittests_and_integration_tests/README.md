0x03. Unittests and Integration Tests

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

TASKS:

 1. Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

 2. Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand)

 3. Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

 4. Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.

 5. In a new test_client.py file, declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.

6. Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.

Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.

Test that the result of _public_repos_url is the expected one based on the mocked payload.

 7. Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

Use @patch as a decorator to mock get_json and make it return a payload of your choice.

Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

 8. We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.

Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.

Use @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py
