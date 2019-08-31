import pytest

from datapoint_client.client import DatapointClient


@pytest.fixture
def dp_client():
    """Returns a DatapointClient with a fake API key"""
    return DatapointClient("api-key")
