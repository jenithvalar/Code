import pytest
import pytest_html

# pytest --junit-xml=junitXMLReport.xml

if __name__ == "__main__":
    pytest.main([
        "-s", r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\Testrun\testsuite.py",
        "--html=htmlReport.html",

    ])
