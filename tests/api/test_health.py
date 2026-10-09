import requests


def test_api_health():
	url = "https://docs.oracle.com/en-us/iaas/api/#/en/healthchecks/20180501/HttpMonitor/"

	response = requests.get(url)
	assert response.status_code==200
