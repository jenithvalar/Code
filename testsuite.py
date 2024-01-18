import pytest

from Testrun.dashboardrunner import TestDashboard



test_timesheet = pytest.mark.login

test_timesheet(TestDashboard.test_dashboard)

